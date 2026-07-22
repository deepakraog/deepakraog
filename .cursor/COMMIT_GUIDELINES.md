# 📝 Branch, Commit & PR Guidelines

**Owner:** Deepak Rao Gaikwad (@deepakraog)  
**Version:** 1.1.0  
**Critical:** All branches, commits, and PRs MUST follow these standards

---

## 🌿 Branch Naming (MANDATORY)

### Rule: Branch names MUST reflect the feature/fix

**Format:** `<type>/<description>`

**Types:**
- `feat/` - New features
- `fix/` - Bug fixes  
- `refactor/` - Code refactoring
- `perf/` - Performance improvements
- `docs/` - Documentation
- `test/` - Tests
- `chore/` - Build/tooling
- `hotfix/` - Production emergency

**Examples:**
```bash
✅ feat/dark-mode-toggle
✅ fix/payment-timeout
✅ refactor/auth-service-solid
✅ perf/database-optimization
✅ hotfix/critical-auth-bug

❌ cursor/docs/agent-workflow-304b  # Generic
❌ feature-123                       # No description
❌ my-branch                         # Vague
```

**Rules:**
- Lowercase only
- Hyphens for spaces (kebab-case)
- Descriptive (max 50 chars)
- No special characters

**JARVIS Auto-Naming:**
```
You: "JARVIS, add dark mode"
JARVIS creates: feat/dashboard-dark-mode

You: "JARVIS, fix payment timeout"  
JARVIS creates: fix/payment-timeout
```

---

## 🔐 GPG Signing (MANDATORY)

### All Commits Must Be GPG-Signed

**Git Configuration:**
```bash
# Set commit author (ONLY Deepak Rao Gaikwad)
git config user.name "Deepak Rao Gaikwad"
git config user.email "gaikwad.dcg@gmail.com"

# Enable GPG signing for all commits
git config commit.gpgsign true
git config tag.gpgsign true

# Set GPG key
git config user.signingkey YOUR_GPG_KEY_ID
```

**Verify Configuration:**
```bash
git config --get user.name
# Output: Deepak Rao Gaikwad

git config --get user.email  
# Output: gaikwad.dcg@gmail.com

git config --get commit.gpgsign
# Output: true
```

### Generate GPG Key (If Needed)

```bash
# Generate new GPG key
gpg --full-generate-key

# List GPG keys
gpg --list-secret-keys --keyid-format=long

# Export public key (add to GitHub)
gpg --armor --export YOUR_GPG_KEY_ID
```

**Add GPG Key to GitHub:**
1. Settings → SSH and GPG keys
2. New GPG key
3. Paste public key
4. Save

---

## 📋 Conventional Commits Format (MANDATORY)

### Format

```
<type>: <subject>

<body>

<footer>
```

### Types (Use These ONLY)

| Type | Description | Example |
|------|-------------|---------|
| **feat** | New feature | `feat: add user authentication` |
| **fix** | Bug fix | `fix: resolve memory leak in websocket` |
| **docs** | Documentation only | `docs: update API documentation` |
| **chore** | Maintenance, no prod code change | `chore: update dependencies` |
| **refactor** | Code refactoring, no behavior change | `refactor: extract validation logic` |
| **perf** | Performance improvement | `perf: optimize database queries` |
| **test** | Adding/updating tests | `test: add unit tests for auth service` |
| **ci** | CI/CD changes | `ci: update GitHub Actions workflow` |
| **build** | Build system changes | `build: update webpack configuration` |
| **style** | Code style, formatting | `style: fix linting errors` |
| **revert** | Revert previous commit | `revert: revert "add feature X"` |

### Subject Line Rules

**DO:**
- ✅ Use lowercase
- ✅ Start with type: (e.g., `feat:`, `fix:`)
- ✅ Keep under 50 characters
- ✅ Use imperative mood ("add" not "added" or "adds")
- ✅ No period at the end

**DON'T:**
- ❌ Capitalize first letter after type:
- ❌ Use past tense
- ❌ Add period at end
- ❌ Be vague ("update stuff")

### Examples

**Good:**
```bash
feat: add dark mode toggle
fix: resolve API timeout issue
docs: update installation guide
chore: upgrade dependencies to latest versions
refactor: simplify authentication logic
perf: reduce bundle size by 15%
test: add integration tests for payment flow
```

**Bad:**
```bash
Update code                    # No type
Added new feature              # Past tense
fix: Fix the bug.              # Period at end, capitalized
feat: Updated the dashboard    # Past tense
Random changes                 # No type, vague
```

---

## 📝 Commit Message Body (Optional)

### When to Add Body

Add body for:
- Complex changes
- Breaking changes
- Changes needing explanation
- Multiple related changes

### Body Format

```
<type>: <subject>

- Detailed explanation of what changed
- Why the change was necessary
- Any side effects or considerations
- References to issues (Fixes #123)
```

### Example with Body

```bash
git commit -m "feat: add OAuth2 authentication

- Implemented OAuth2 flow with Google and GitHub providers
- Added JWT token generation and validation
- Updated user model to support external auth
- Configured secure session management

Fixes #234
Related to #145"
```

---

## 🚫 No Co-Authors (CRITICAL)

### Single Author Only

**All commits must have:**
- Author: Deepak Rao Gaikwad
- Email: gaikwad.dcg@gmail.com
- GPG Signature: Your GPG key

**NEVER include:**
- ❌ Co-authored-by:
- ❌ Co-committed-by:
- ❌ Pair-programmed-by:
- ❌ Any other attribution

### Verify Author

```bash
# Check commit author
git log --format="%an <%ae>" -1

# Should output:
# Deepak Rao Gaikwad <gaikwad.dcg@gmail.com>
```

### Verify GPG Signature

```bash
# Check if commit is signed
git log --show-signature -1

# Should show:
# gpg: Signature made ...
# gpg: Good signature from "Deepak Rao Gaikwad <gaikwad.dcg@gmail.com>"
```

---

## 🎯 PR Description Format (No Agent Attribution)

### What to INCLUDE

✅ **Technical details:**
- Summary of changes
- Implementation approach
- Testing performed
- Performance impact
- Security considerations

✅ **Professional tone:**
- First-person ("I implemented...")
- Technical accuracy
- Clear explanations

### What to EXCLUDE

❌ **Any mention of:**
- "Generated by Cursor"
- "Created by Claude"
- "AI agent"
- "Automated by"
- "Bot created"
- "Agent implemented"

### PR Template

```markdown
## Summary

[Clear, concise description of what changed]

## Motivation

[Why this change was needed]

## Implementation

[How it was implemented, technical details]

## Changes

- [Specific change 1]
- [Specific change 2]
- [Specific change 3]

## Testing

- Unit tests: [coverage %]
- Integration tests: [what was tested]
- Manual testing: [steps performed]
- Performance: [before/after metrics]

## Security

[Any security considerations]

## Breaking Changes

[None OR list with migration guide]

## Deployment

- [ ] Can deploy anytime
- [ ] Requires maintenance window
- [ ] Feature flag available

## Rollback

[Rollback procedure if needed]

## Checklist

- [ ] Tests pass
- [ ] Linting passes
- [ ] Documentation updated
- [ ] Reviewed locally
```

**Note:** Write in first-person, as if Deepak wrote it personally.

---

## ✍️ Writing Style for PRs

### First-Person Professional

**Good:**
```markdown
## Summary

I've implemented user authentication with JWT tokens. This provides
secure, stateless authentication for our API.

## Implementation

I chose bcrypt for password hashing (cost factor 10) and RS256
for JWT signing. The implementation follows OAuth2 best practices.

## Testing

I've added 24 unit tests covering all edge cases, with 87% coverage.
Manual testing included:
- Successful login flow
- Invalid credentials handling
- Token expiration
- Refresh token rotation
```

**Bad:**
```markdown
## Summary

The agent has implemented user authentication...
Claude generated JWT token handling...
This PR was created by Cursor Agent...
```

### Technical and Professional

**Use:**
- ✅ "I implemented..."
- ✅ "I've added..."
- ✅ "I chose... because..."
- ✅ "The approach..."
- ✅ "This change..."

**Avoid:**
- ❌ "Agent implemented..."
- ❌ "Cursor created..."
- ❌ "AI generated..."
- ❌ "Automated process..."

---

## 🔧 Git Hooks Setup

### Pre-Commit Hook

**`.git/hooks/pre-commit`:**

```bash
#!/bin/bash

# Check GPG signing is enabled
GPG_SIGN=$(git config --get commit.gpgsign)
if [ "$GPG_SIGN" != "true" ]; then
    echo "❌ Error: GPG signing not enabled"
    echo "Run: git config commit.gpgsign true"
    exit 1
fi

# Check commit author
AUTHOR_NAME=$(git config --get user.name)
AUTHOR_EMAIL=$(git config --get user.email)

if [ "$AUTHOR_NAME" != "Deepak Rao Gaikwad" ]; then
    echo "❌ Error: Incorrect author name: $AUTHOR_NAME"
    echo "Run: git config user.name \"Deepak Rao Gaikwad\""
    exit 1
fi

if [ "$AUTHOR_EMAIL" != "gaikwad.dcg@gmail.com" ]; then
    echo "❌ Error: Incorrect author email: $AUTHOR_EMAIL"
    echo "Run: git config user.email \"gaikwad.dcg@gmail.com\""
    exit 1
fi

echo "✅ GPG signing enabled"
echo "✅ Author: $AUTHOR_NAME <$AUTHOR_EMAIL>"
```

### Commit Message Hook

**`.git/hooks/commit-msg`:**

```bash
#!/bin/bash

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

# Check conventional commit format
PATTERN="^(feat|fix|docs|chore|refactor|perf|test|ci|build|style|revert): .+"

if ! echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
    echo "❌ Error: Commit message doesn't follow conventional format"
    echo ""
    echo "Format: <type>: <subject>"
    echo ""
    echo "Valid types: feat, fix, docs, chore, refactor, perf, test, ci, build, style, revert"
    echo ""
    echo "Examples:"
    echo "  feat: add user authentication"
    echo "  fix: resolve memory leak"
    echo "  docs: update API documentation"
    echo ""
    echo "Your commit message:"
    echo "$COMMIT_MSG"
    exit 1
fi

# Check subject line length (type + ": " + subject should be < 50 chars)
SUBJECT_LINE=$(echo "$COMMIT_MSG" | head -n 1)
SUBJECT_LENGTH=${#SUBJECT_LINE}

if [ $SUBJECT_LENGTH -gt 72 ]; then
    echo "⚠️  Warning: Subject line is $SUBJECT_LENGTH characters (recommended: < 72)"
fi

# Check for period at end of subject
if echo "$SUBJECT_LINE" | grep -q "\.$"; then
    echo "❌ Error: Subject line should not end with a period"
    exit 1
fi

# Check for capitalization after type:
TYPE_AND_COLON=$(echo "$SUBJECT_LINE" | grep -oE "^[a-z]+: ")
FIRST_CHAR_AFTER_COLON=$(echo "$SUBJECT_LINE" | sed 's/^[a-z]*: //' | head -c 1)

if echo "$FIRST_CHAR_AFTER_COLON" | grep -q "[A-Z]"; then
    echo "❌ Error: Subject should be lowercase after 'type: '"
    echo "Example: 'feat: add feature' not 'feat: Add feature'"
    exit 1
fi

echo "✅ Commit message follows conventional format"
```

### Make Hooks Executable

```bash
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/commit-msg
```

---

## 📋 Agent Commit Instructions

### When Agent Creates Commits

**1. Set Author (Always):**
```bash
git config user.name "Deepak Rao Gaikwad"
git config user.email "gaikwad.dcg@gmail.com"
git config commit.gpgsign true
```

**2. Use Conventional Format:**
```bash
# Good examples:
git commit -m "feat: add dark mode toggle"
git commit -m "fix: resolve API timeout in user endpoint"
git commit -m "docs: update installation instructions"
git commit -m "refactor: extract validation logic to separate module"
git commit -m "perf: optimize database queries with indexes"
```

**3. Verify Before Push:**
```bash
# Check last commit
git log -1 --format="%an <%ae>" --show-signature

# Should show:
# Deepak Rao Gaikwad <gaikwad.dcg@gmail.com>
# gpg: Good signature from "Deepak Rao Gaikwad..."
```

**4. Multiple Commits:**

For logical grouping:
```bash
git commit -m "feat: add user authentication endpoint"
git commit -m "test: add unit tests for auth service"
git commit -m "docs: update API documentation with auth examples"
```

---

## 🎯 PR Description Guidelines

### Human-Written Tone

**Write as Deepak would write:**

```markdown
## Summary

I've implemented the user authentication system using JWT tokens.
This provides a secure, stateless authentication mechanism for our API.

## Why This Change

Our application needs a robust authentication system. I chose JWT
because it's stateless, scales horizontally, and works well with
our microservices architecture.

## Implementation Details

**Technology choices:**
- bcrypt for password hashing (cost factor 10)
- RS256 for JWT signing (more secure than HS256)
- Redis for refresh token storage

**Key features:**
- User registration with email verification
- Login with email/password
- Access token (1 hour expiry)
- Refresh token (7 days expiry)
- Token rotation on refresh
- Rate limiting (10 attempts per 15 minutes)

## Security Considerations

I've implemented several security measures:
- Passwords hashed with bcrypt before storage
- JWT tokens signed with RS256
- Refresh tokens stored in Redis with expiration
- Rate limiting prevents brute force attacks
- Input validation with Zod schemas
- SQL injection prevention with parameterized queries

## Testing

I've added comprehensive tests:
- 24 unit tests (87% coverage)
- 12 integration tests (API endpoints)
- 5 E2E tests (complete auth flow)

Manual testing included:
- Successful registration and login
- Invalid credentials handling
- Token expiration and refresh
- Rate limiting verification

## Performance

Benchmarks show excellent performance:
- Login endpoint: 145ms average
- Token validation: 8ms average
- All within our <200ms target

## Breaking Changes

None. This is a new feature.

## Rollback

If issues occur:
```bash
git revert abc123
```

Database doesn't need rollback as it's additive only.

## Deployment

- [x] Can deploy anytime
- [ ] No maintenance window needed
- [x] All tests pass
- [x] Documentation updated

Let me know if you have any questions or need changes!
```

### What to Avoid

❌ **Never write:**
```markdown
"This PR was generated by Cursor Agent..."
"Claude implemented the following features..."
"AI agent created this change..."
"Automated implementation..."
"Bot-generated code..."
```

✅ **Always write:**
```markdown
"I've implemented..."
"I chose this approach because..."
"I've added tests for..."
"This change improves..."
```

---

## ✅ Verification Checklist

### Before Every Commit

- [ ] Git author: Deepak Rao Gaikwad
- [ ] Git email: gaikwad.dcg@gmail.com
- [ ] GPG signing enabled
- [ ] Commit message: conventional format
- [ ] Subject line: lowercase, <72 chars, no period
- [ ] No co-author attribution

### Before Every PR

- [ ] All commits GPG-signed
- [ ] All commits follow conventional format
- [ ] PR description: first-person, professional
- [ ] No mention of AI/agent/automation
- [ ] Reads as human-written by Deepak
- [ ] Technical details accurate
- [ ] Testing evidence included

### Verify Command

```bash
# Check last commit
git log -1 --pretty=fuller --show-signature

# Should show:
# Author: Deepak Rao Gaikwad <gaikwad.dcg@gmail.com>
# Commit: Deepak Rao Gaikwad <gaikwad.dcg@gmail.com>
# gpg: Good signature from "Deepak Rao Gaikwad..."
# 
# feat: add user authentication
```

---

## 🚨 Common Mistakes to Avoid

### ❌ Wrong

```bash
# No type prefix
git commit -m "add new feature"

# Capitalized after colon
git commit -m "feat: Add new feature"

# Past tense
git commit -m "feat: added new feature"

# Period at end
git commit -m "feat: add new feature."

# Co-author
git commit -m "feat: add feature

Co-authored-by: AI Agent <agent@example.com>"
```

### ✅ Correct

```bash
# Proper format
git commit -m "feat: add new feature"

# With body
git commit -m "feat: add OAuth2 authentication

- Implemented Google and GitHub OAuth2 providers
- Added JWT token generation
- Updated user model for external auth

Fixes #234"
```

---

## 📚 Resources

**Conventional Commits:**
- https://www.conventionalcommits.org/

**GPG Signing:**
- https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits

**Git Configuration:**
```bash
# View all config
git config --list

# View specific config
git config user.name
git config user.email
git config commit.gpgsign
```

---

**All commits must follow these guidelines. No exceptions.**

---

**Version:** 1.0.0  
**Last Updated:** July 21, 2026  
**Owner:** Deepak Rao Gaikwad (@deepakraog)
