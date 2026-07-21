# 🔒 Pre-Commit Hooks & Code Quality Setup

**Purpose:** Automated code quality enforcement before commits  
**Owner:** Deepak Rao Gaikwad (@deepakraog)  
**Version:** 1.0.0

---

## 📋 Overview

Pre-commit hooks ensure **every commit** follows SOLID principles, DRY, performance standards, and security best practices—before code even reaches CI/CD.

---

## 🚀 Quick Setup

### Installation

```bash
# Install pre-commit framework
npm install --save-dev husky lint-staged

# Initialize husky
npx husky install

# Add to package.json
npm set-script prepare "husky install"
```

### Configuration Files

#### 1. `.husky/pre-commit`

```bash
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

echo "🔍 Running pre-commit checks..."

# Run lint-staged
npx lint-staged

# Custom checks
npm run pre-commit:custom

echo "✅ Pre-commit checks passed!"
```

#### 2. `package.json` - lint-staged configuration

```json
{
  "lint-staged": {
    "*.{ts,tsx,js,jsx}": [
      "eslint --fix",
      "prettier --write",
      "npm run test:affected"
    ],
    "*.{json,md,yml,yaml}": [
      "prettier --write"
    ],
    "*.{ts,tsx}": [
      "npm run type-check"
    ]
  },
  "scripts": {
    "prepare": "husky install",
    "pre-commit:custom": "node scripts/pre-commit-checks.js",
    "test:affected": "jest --bail --findRelatedTests",
    "type-check": "tsc --noEmit"
  }
}
```

#### 3. `scripts/pre-commit-checks.js`

```javascript
#!/usr/bin/env node

/**
 * Custom pre-commit checks
 * Enforces SOLID, DRY, performance, security standards
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Get staged files
const stagedFiles = execSync('git diff --cached --name-only --diff-filter=ACM')
  .toString()
  .trim()
  .split('\n')
  .filter(file => file.match(/\.(ts|tsx|js|jsx)$/));

let errors = [];

console.log('🔍 Running custom quality checks...\n');

// Check 1: No console.log or debugger
console.log('1️⃣ Checking for console.log/debugger...');
stagedFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  if (content.includes('console.log') && !file.includes('.test.')) {
    errors.push(`❌ ${file}: Remove console.log statements`);
  }
  
  if (content.includes('debugger')) {
    errors.push(`❌ ${file}: Remove debugger statements`);
  }
});

// Check 2: No TODO/FIXME in production code
console.log('2️⃣ Checking for TODO/FIXME...');
stagedFiles.forEach(file => {
  if (file.includes('src/') && !file.includes('.test.')) {
    const content = fs.readFileSync(file, 'utf8');
    
    if (content.match(/\/\/\s*(TODO|FIXME)/i)) {
      errors.push(`⚠️  ${file}: TODO/FIXME found - resolve before commit`);
    }
  }
});

// Check 3: File size limits
console.log('3️⃣ Checking file sizes...');
stagedFiles.forEach(file => {
  const stats = fs.statSync(file);
  const lines = fs.readFileSync(file, 'utf8').split('\n').length;
  
  if (lines > 300 && !file.includes('.test.')) {
    errors.push(`❌ ${file}: ${lines} lines exceeds 300 line limit - split into smaller files`);
  }
  
  if (stats.size > 50 * 1024) { // 50KB
    errors.push(`❌ ${file}: ${Math.round(stats.size/1024)}KB exceeds 50KB limit`);
  }
});

// Check 4: Function complexity
console.log('4️⃣ Checking function complexity...');
stagedFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  // Simple heuristic: count if/for/while statements
  const functions = content.match(/function\s+\w+|const\s+\w+\s*=\s*\(/g) || [];
  
  functions.forEach(func => {
    const funcBody = content.substring(content.indexOf(func));
    const complexity = (funcBody.match(/\b(if|for|while|switch|catch)\b/g) || []).length;
    
    if (complexity > 10) {
      errors.push(`⚠️  ${file}: Function complexity ${complexity} exceeds 10 - refactor`);
    }
  });
});

// Check 5: No hardcoded secrets
console.log('5️⃣ Checking for hardcoded secrets...');
const secretPatterns = [
  /['"]?api[_-]?key['"]?\s*[:=]\s*['"][^'"]+['"]/i,
  /['"]?secret['"]?\s*[:=]\s*['"][^'"]+['"]/i,
  /['"]?password['"]?\s*[:=]\s*['"][^'"]+['"]/i,
  /['"]?token['"]?\s*[:=]\s*['"][^'"]+['"]/i,
  /sk_live_[a-zA-Z0-9]+/, // Stripe live key
  /AKIA[0-9A-Z]{16}/, // AWS access key
];

stagedFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  secretPatterns.forEach(pattern => {
    if (pattern.test(content) && !content.includes('process.env')) {
      errors.push(`🔒 ${file}: Potential hardcoded secret detected`);
    }
  });
});

// Check 6: Proper imports (no circular dependencies)
console.log('6️⃣ Checking imports...');
try {
  execSync('npx madge --circular src/', { stdio: 'pipe' });
} catch (error) {
  errors.push('❌ Circular dependencies detected - run `npx madge --circular src/` for details');
}

// Check 7: Test files exist for new source files
console.log('7️⃣ Checking test coverage...');
const newSourceFiles = stagedFiles.filter(f => 
  f.includes('src/') && 
  !f.includes('.test.') && 
  !f.includes('.spec.')
);

newSourceFiles.forEach(file => {
  const testFile = file
    .replace('src/', 'tests/')
    .replace(/\.(ts|tsx|js|jsx)$/, '.test.$1');
  
  if (!fs.existsSync(testFile)) {
    errors.push(`⚠️  ${file}: No test file found at ${testFile}`);
  }
});

// Check 8: TypeScript strict mode violations
console.log('8️⃣ Checking TypeScript strict mode...');
stagedFiles.filter(f => f.match(/\.tsx?$/)).forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  // Check for 'any' type
  if (content.match(/:\s*any\b/) && !file.includes('.test.')) {
    errors.push(`❌ ${file}: Avoid 'any' type - use specific types`);
  }
  
  // Check for @ts-ignore
  if (content.includes('@ts-ignore')) {
    errors.push(`❌ ${file}: Remove @ts-ignore - fix type issues properly`);
  }
});

// Check 9: Proper error handling
console.log('9️⃣ Checking error handling...');
stagedFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  // Find try-catch blocks
  const tryCatches = content.match(/try\s*{[^}]*}\s*catch/g) || [];
  
  tryCatches.forEach(() => {
    // Simple check: ensure catch block does something
    if (content.includes('catch (error) {}') || content.includes('catch {}')) {
      errors.push(`❌ ${file}: Empty catch block - handle errors properly`);
    }
  });
});

// Check 10: Performance anti-patterns
console.log('🔟 Checking performance patterns...');
stagedFiles.forEach(file => {
  const content = fs.readFileSync(file, 'utf8');
  
  // Check for synchronous operations in async context
  if (content.includes('async') && content.match(/fs\.readFileSync|fs\.writeFileSync/)) {
    errors.push(`⚠️  ${file}: Use async file operations (readFile instead of readFileSync)`);
  }
  
  // Check for sequential awaits
  const sequentialAwaits = content.match(/await\s+\w+\([^)]*\);?\s*await\s+\w+\(/g);
  if (sequentialAwaits && sequentialAwaits.length > 2) {
    errors.push(`⚠️  ${file}: Consider using Promise.all for parallel operations`);
  }
});

// Report results
console.log('\n📊 Results:\n');

if (errors.length === 0) {
  console.log('✅ All custom checks passed!\n');
  process.exit(0);
} else {
  console.log('❌ Issues found:\n');
  errors.forEach(error => console.log(`  ${error}`));
  console.log('\n💡 Fix these issues and commit again.\n');
  process.exit(1);
}
```

---

## 🔧 Tool Configurations

### ESLint Configuration (`.eslintrc.json`)

```json
{
  "env": {
    "node": true,
    "es2022": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "plugin:import/recommended",
    "plugin:import/typescript",
    "prettier"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "plugins": [
    "@typescript-eslint",
    "import",
    "sonarjs",
    "security"
  ],
  "rules": {
    // SOLID Principles
    "max-lines": ["error", { "max": 300, "skipComments": true }],
    "max-lines-per-function": ["error", { "max": 50, "skipComments": true }],
    "max-params": ["error", 4],
    "max-depth": ["error", 3],
    "max-nested-callbacks": ["error", 3],
    
    // Code Quality
    "complexity": ["error", 10],
    "sonarjs/cognitive-complexity": ["error", 15],
    "sonarjs/no-duplicate-string": ["error", 3],
    "sonarjs/no-identical-functions": "error",
    
    // Security
    "security/detect-object-injection": "warn",
    "security/detect-non-literal-regexp": "warn",
    "security/detect-unsafe-regex": "error",
    
    // TypeScript Strict
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "error",
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/strict-boolean-expressions": "error",
    
    // Import Order
    "import/order": ["error", {
      "groups": ["builtin", "external", "internal", "parent", "sibling", "index"],
      "newlines-between": "always",
      "alphabetize": { "order": "asc" }
    }],
    
    // Code Style
    "no-console": "error",
    "no-debugger": "error",
    "no-alert": "error",
    "no-var": "error",
    "prefer-const": "error",
    "prefer-arrow-callback": "error",
    "arrow-body-style": ["error", "as-needed"],
    
    // Error Handling
    "no-throw-literal": "error",
    "@typescript-eslint/no-floating-promises": "error",
    "require-await": "error"
  }
}
```

### TypeScript Configuration (`tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "node",
    "outDir": "./dist",
    "rootDir": "./src",
    
    // Strict Type Checking
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    
    // Additional Checks
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    
    // Advanced
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

### Prettier Configuration (`.prettierrc.json`)

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

---

## 🧪 Testing Configuration

### Jest Configuration (`jest.config.js`)

```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/__tests__/**/*.ts', '**/?(*.)+(spec|test).ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/**/*.test.ts',
    '!src/**/index.ts',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  coverageReporters: ['text', 'lcov', 'html'],
  verbose: true,
  testTimeout: 10000,
};
```

---

## 🔐 Security Scanning

### Package Audit Script (`scripts/security-audit.sh`)

```bash
#!/bin/bash

echo "🔒 Running security audit..."

# NPM audit
echo "\n1️⃣ Checking npm packages..."
npm audit --audit-level=moderate

# Dependency check
echo "\n2️⃣ Checking for known vulnerabilities..."
npx snyk test || true

# OWASP dependency check
echo "\n3️⃣ Running OWASP dependency check..."
npx audit-ci --moderate

# Check for secrets in code
echo "\n4️⃣ Scanning for hardcoded secrets..."
npx detect-secrets-launcher --all-files

# License compliance
echo "\n5️⃣ Checking license compliance..."
npx license-checker --onlyAllow "MIT;Apache-2.0;BSD-3-Clause;ISC"

echo "\n✅ Security audit complete!"
```

---

## 🚀 GitHub Actions Integration

### Workflow (`.github/workflows/quality-checks.yml`)

```yaml
name: Code Quality Checks

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  quality:
    name: Code Quality
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Lint
        run: npm run lint
      
      - name: Type Check
        run: npm run type-check
      
      - name: Test
        run: npm test -- --coverage
      
      - name: Security Audit
        run: npm audit --audit-level=moderate
      
      - name: Check Bundle Size
        run: npm run build && npm run size-check
      
      - name: SonarCloud Scan
        uses: SonarSource/sonarcloud-github-action@master
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      
      - name: Upload Coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          name: codecov-umbrella
```

---

## 📊 Code Quality Metrics

### SonarQube Configuration (`sonar-project.properties`)

```properties
sonar.projectKey=your-project-key
sonar.organization=your-org

sonar.sources=src
sonar.tests=tests
sonar.test.inclusions=**/*.test.ts,**/*.spec.ts

sonar.typescript.lcov.reportPaths=coverage/lcov.info

# Quality Gates
sonar.qualitygate.wait=true

# Code Smells
sonar.issue.ignore.multicriteria=e1,e2

# Ignore test files for certain rules
sonar.issue.ignore.multicriteria.e1.ruleKey=typescript:S1186
sonar.issue.ignore.multicriteria.e1.resourceKey=**/*.test.ts

# Coverage
sonar.coverage.exclusions=**/*.test.ts,**/*.spec.ts,**/index.ts
```

---

## 🎯 Code Review Checklist

### Automated Checks (Pre-Commit + CI)

✅ **Formatting**
- [ ] Code formatted with Prettier
- [ ] Consistent indentation
- [ ] No trailing whitespace

✅ **Linting**
- [ ] No ESLint errors
- [ ] No ESLint warnings (or properly suppressed)
- [ ] Import order correct

✅ **Type Safety**
- [ ] TypeScript strict mode passes
- [ ] No `any` types
- [ ] No `@ts-ignore` comments

✅ **Testing**
- [ ] Test coverage ≥ 80%
- [ ] All tests pass
- [ ] No skipped tests without reason

✅ **Security**
- [ ] No hardcoded secrets
- [ ] npm audit passes
- [ ] No known vulnerabilities

✅ **Performance**
- [ ] Bundle size within limits
- [ ] No obvious performance issues
- [ ] Async operations parallelized where possible

✅ **Code Quality**
- [ ] Complexity ≤ 10
- [ ] File size ≤ 300 lines
- [ ] Function size ≤ 50 lines
- [ ] No duplicate code

---

## 🛠️ Setup Instructions for Agents

### What Agents Should Do

When implementing features, agents automatically:

1. **Before Starting:**
   - Check existing pre-commit hooks
   - Ensure all tools installed
   - Run initial quality check

2. **During Implementation:**
   - Follow SOLID principles
   - Apply DRY principle
   - Write performant code
   - Add proper error handling
   - Include security measures

3. **Before Committing:**
   - Run pre-commit hooks locally
   - Fix any issues found
   - Verify all checks pass
   - Only then commit

4. **In PR:**
   - Include all check results
   - Document any suppressions
   - Explain trade-offs made

### Installation Command for New Projects

```bash
# Run this once per project
npm install --save-dev \
  husky \
  lint-staged \
  eslint \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser \
  eslint-plugin-import \
  eslint-plugin-sonarjs \
  eslint-plugin-security \
  prettier \
  eslint-config-prettier \
  typescript \
  jest \
  ts-jest \
  @types/jest \
  madge \
  snyk \
  audit-ci \
  detect-secrets-launcher

# Initialize
npx husky install
npm set-script prepare "husky install"
npx husky add .husky/pre-commit "npx lint-staged"

# Copy configuration files from this directory
```

---

## 📝 Suppression Guidelines

### When to Suppress Warnings

Only suppress when:
1. **False Positive:** Tool incorrectly flags code
2. **Third-Party Code:** External library limitations
3. **Migration:** Temporary during refactoring
4. **Performance:** Proven optimization needed

### How to Suppress

```typescript
// ❌ BAD: No explanation
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const data: any = response;

// ✅ GOOD: With explanation
// External API returns unknown structure, validated at runtime with Zod
// eslint-disable-next-line @typescript-eslint/no-explicit-any
const data: any = response;
const validated = ResponseSchema.parse(data);
```

---

## 🎓 Best Practices

1. **Run Checks Often:** Don't wait for commit
   ```bash
   npm run lint
   npm run type-check
   npm test
   ```

2. **Fix Issues Early:** Don't accumulate technical debt

3. **Understand Errors:** Don't blindly suppress

4. **Keep Tools Updated:** Regular dependency updates

5. **Team Alignment:** Everyone uses same config

---

**Pre-commit hooks ensure every commit meets quality standards. No exceptions.** ✅

---

**Version:** 1.0.0  
**Last Updated:** July 21, 2026  
**Owner:** Deepak Rao Gaikwad (@deepakraog)
