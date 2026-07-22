# ⚡ JARVIS Token Optimization Guidelines

**Principle:** Deliver maximum value with minimum resource consumption

**Owner:** Deepak Rao Gaikwad (@deepakraog)  
**Version:** 1.0.0  
**Goal:** Optimize results with less input, less token usage, less cost

---

## 🎯 Core Philosophy

**"Less is More"**

- ✅ **Efficient** - Use minimal tokens for maximum impact
- ✅ **Precise** - Get exactly what's needed, nothing more
- ✅ **Strategic** - Plan before executing
- ✅ **Batched** - Do multiple things in one operation
- ✅ **Cached** - Reuse information, don't re-fetch

**Target:** 50-70% reduction in token usage while maintaining quality

---

## 📊 Token Usage Priorities

### 1. Read Operations (Highest Cost)

**❌ Wasteful:**
- Read entire 10,000 line file to find one function

**✅ Optimized:**
- Grep for function name first
- Read only the specific lines found

**Savings:** ~95% fewer tokens

### 2. Search Operations

**❌ Wasteful:**
- Read all files matching pattern
- Search through each one

**✅ Optimized:**
- Use Grep with specific pattern
- Get direct matches only

**Savings:** ~90% fewer tokens

### 3. File Navigation

**❌ Wasteful:**
- Read README → Find directory → Read directory files → Find target

**✅ Optimized:**
- Glob for specific file pattern directly

**Savings:** ~80% fewer tokens

---

## 🛠️ Efficient Tool Usage

### Reading Files

**Rule:** Never read entire files unless absolutely necessary

**❌ Bad Example:**
```
Task: Find UserProfile component
Action: Read /src/components/App.tsx (3000 lines)
Result: Found on line 2450
```

**✅ Good Example:**
```
Task: Find UserProfile component
Action 1: Grep "UserProfile" in src/components/
Action 2: Read only lines 2445-2480 from App.tsx
Result: Found efficiently
```

**Commands:**
```bash
# Step 1: Find location
Grep pattern="class UserProfile|function UserProfile" 
     path="src/components/"

# Step 2: Read specific lines only
Read path="src/components/App.tsx" 
     offset=2445 
     limit=35
```

**Token Savings:** 2965 lines = ~15,000 tokens saved

### Searching Code

**Rule:** Use most specific search pattern possible

**❌ Bad Example:**
```bash
Grep pattern="user"
# Returns 500+ matches across all files
```

**✅ Good Example:**
```bash
Grep pattern="class UserAuthService" 
     type="ts"
# Returns 1 exact match
```

**Better Patterns:**
```bash
# Use anchors
Grep pattern="^export class UserAuthService"

# Combine with path
Grep pattern="UserAuthService" 
     path="src/services/"

# Use file type
Grep pattern="UserAuthService" 
     type="ts"
```

**Token Savings:** 499 unnecessary matches = ~2,500 tokens saved

### Glob Patterns

**Rule:** Use precise patterns to minimize results

**❌ Bad Example:**
```bash
Glob "*.ts"
# Returns 500 TypeScript files
```

**✅ Good Example:**
```bash
Glob "src/services/*Auth*.ts"
# Returns 3 relevant files
```

**Precision Examples:**
```bash
# Specific path + pattern
Glob "**/services/*Auth*.service.ts"

# Multiple specific patterns
Glob "**/components/User*.tsx"
Glob "**/hooks/use*.ts"
```

**Token Savings:** 497 unnecessary files = ~5,000 tokens saved

---

## 💡 Strategic Planning

### Before ANY Operation

**Ask These Questions:**
1. What's the MINIMUM information needed?
2. Can I get it with search instead of reading?
3. Can I batch multiple operations?
4. Do I already have this information?
5. Can I infer from context instead of fetching?

### Example Workflow Comparison

**Task:** Add authentication to API

**❌ Wasteful Approach (50,000 tokens):**
1. Read entire API codebase (20 files, 10,000 lines) - 30,000 tokens
2. Search web for auth examples - 5,000 tokens
3. Read all examples in full - 10,000 tokens
4. Design complete system - 3,000 tokens
5. Re-read files to verify - 2,000 tokens

**✅ Optimized Approach (8,000 tokens):**
1. Grep existing auth patterns → find 2 examples - 200 tokens
2. Read ONLY those 2 files (200 lines total) - 1,500 tokens
3. Design based on existing patterns - 2,000 tokens
4. Implement (read files only when editing) - 3,500 tokens
5. Verify with targeted Grep searches - 800 tokens

**Savings:** 42,000 tokens = **84% reduction**

---

## 🔄 Batch Operations

### Rule: Combine related operations in parallel

**❌ Wasteful - Sequential:**
```
1. Read file1.ts → Analyze
2. Read file2.ts → Analyze
3. Read file3.ts → Analyze

Total: 3 round trips, slower, more context
```

**✅ Optimized - Parallel:**
```
1. Read file1.ts + file2.ts + file3.ts simultaneously
2. Analyze all together with shared context

Total: 1 round trip, faster, efficient
```

**When to Batch:**
- Reading multiple related files
- Multiple Grep searches
- Multiple Glob patterns
- File edits in same logical change

**Token Savings:** Eliminates redundant context = ~30% fewer tokens

---

## 📝 Response Optimization

### Rule: Be concise but complete

**❌ Wasteful Response:**
```
I understand you want to add authentication. Let me explain 
what I'm going to do. First, I'll read the current API 
structure. Then I'll analyze the security requirements. 
After that, I'll design the authentication system. Following 
that, I'll implement the changes. Finally, I'll test 
everything to make sure it works properly.

Now, let me start by reading the API files...
[continues for 500 more words]
```

**✅ Optimized Response:**
```
Adding authentication to API.

Steps:
1. Grep existing auth patterns
2. Read relevant files only
3. Implement based on existing patterns
4. Test

Starting...
[proceeds directly to action]
```

**Token Savings:** ~80% fewer response tokens

### Communication Guidelines

**Do:**
- ✅ State what you're doing (1 line)
- ✅ Execute immediately
- ✅ Report results concisely
- ✅ Ask clarifying questions (if needed)

**Don't:**
- ❌ Explain every detail before acting
- ❌ Repeat information already known
- ❌ Provide unnecessary background
- ❌ Give multiple alternatives unless asked

---

## 🎯 Specific Optimization Techniques

### 1. Progressive Reading

**Technique:** Read in stages, from general to specific

```bash
# Stage 1: Get overview (cheap)
Glob "src/**/*.ts" | head -20

# Stage 2: Find specific area (medium)
Grep pattern="AuthService" path="src/"

# Stage 3: Read exact location (targeted)
Read path="src/services/auth.ts" offset=50 limit=100
```

**Savings:** ~70% fewer tokens than reading everything upfront

### 2. Contextual Inference

**Technique:** Deduce from existing information

**Example:**
```
Given: Project uses TypeScript, React, Express
Task: Add new endpoint

Inference: 
- Routes likely in src/routes/
- Controllers in src/controllers/
- Use existing patterns

Action: Grep for similar endpoints instead of reading docs
```

**Savings:** ~60% fewer tokens from avoiding redundant research

### 3. Lazy Loading

**Technique:** Load information only when needed

**❌ Eager Loading:**
```
1. Read entire test suite
2. Read all dependencies
3. Read documentation
4. Start implementing
```

**✅ Lazy Loading:**
```
1. Start implementing
2. Read specific test when writing test
3. Read specific dependency when using it
4. Read specific doc section when needed
```

**Savings:** ~50% fewer tokens by avoiding unnecessary reads

### 4. Smart Caching

**Technique:** Remember information from earlier in conversation

**Example:**
```
Turn 1: User says "Project is React + TypeScript"
Turn 5: Don't ask "What framework?" - already know
Turn 10: Don't read package.json - already have context
```

**Savings:** ~40% fewer tokens by avoiding re-fetching known info

### 5. Targeted Updates

**Technique:** Edit only what needs changing

**❌ Wasteful:**
```
Read entire 500-line file
Change 3 lines
Write entire file back
```

**✅ Optimized:**
```
Read only the function being changed (20 lines)
Use StrReplace with minimal context
Done
```

**Savings:** ~95% fewer tokens

---

## 📈 Token Budget Guidelines

### Per-Task Budgets

| Task Type | Token Budget | Strategy |
|-----------|--------------|----------|
| **Bug Fix** | 5,000-10,000 | Grep error → Read specific file → Fix |
| **New Feature** | 10,000-20,000 | Grep patterns → Read examples → Implement |
| **Refactor** | 15,000-30,000 | Analyze structure → Plan → Execute in chunks |
| **Documentation** | 5,000-10,000 | Read code sections → Generate docs |
| **Code Review** | 8,000-15,000 | Read diffs only → Provide feedback |

### Emergency Budget Cuts

**If approaching token limits:**

1. **Stop reading entire files** - Switch to grep + targeted reads
2. **Batch all remaining operations** - No more sequential calls
3. **Minimize responses** - State actions, skip explanations
4. **Use inference** - Deduce from context instead of fetching
5. **Prioritize** - Complete critical tasks first

---

## 🔍 Search Strategy Hierarchy

**Use this order (cheapest to most expensive):**

1. **Glob** (cheapest) - Find files by pattern
   ```bash
   Glob "**/auth*.service.ts"
   ```

2. **Grep** (cheap) - Search file contents
   ```bash
   Grep pattern="class AuthService" path="src/"
   ```

3. **Read with offset/limit** (medium) - Read specific lines
   ```bash
   Read path="file.ts" offset=100 limit=50
   ```

4. **Read full file** (expensive) - Only when necessary
   ```bash
   Read path="file.ts"  # Use sparingly!
   ```

**Cost Comparison:**
- Glob: ~100 tokens
- Grep: ~300 tokens
- Read (partial): ~1,000 tokens
- Read (full): ~5,000+ tokens

**Always start cheap, go expensive only if needed.**

---

## 🎓 Real-World Examples

### Example 1: Add Dark Mode

**❌ Wasteful (30,000 tokens):**
```
1. Read entire React codebase
2. Research dark mode implementations
3. Read CSS files
4. Read theme files
5. Plan implementation
6. Implement
```

**✅ Optimized (6,000 tokens):**
```
1. Grep "theme" in src/ → Find theme.ts
2. Read theme.ts only (100 lines)
3. Grep "useTheme|ThemeProvider"
4. Implement based on existing pattern
```

**Result:** Same quality, **80% fewer tokens**

### Example 2: Fix Production Bug

**❌ Wasteful (25,000 tokens):**
```
1. Read entire application
2. Review all error handling
3. Check all API calls
4. Test everything
```

**✅ Optimized (4,000 tokens):**
```
1. Grep error message in logs
2. Read exact file + function (50 lines)
3. Identify issue
4. Fix + verify
```

**Result:** Faster fix, **84% fewer tokens**

### Example 3: Add New API Endpoint

**❌ Wasteful (35,000 tokens):**
```
1. Read all existing endpoints
2. Read routing documentation
3. Read middleware files
4. Design new endpoint
5. Implement
```

**✅ Optimized (8,000 tokens):**
```
1. Grep one similar endpoint
2. Read that endpoint only (80 lines)
3. Copy pattern, adapt for new endpoint
4. Done
```

**Result:** Same quality, **77% fewer tokens**

---

## 📋 Token Optimization Checklist

**Before Every Operation:**

- [ ] Can I use Grep instead of Read?
- [ ] Can I use Glob instead of listing?
- [ ] Can I read partial instead of full file?
- [ ] Can I batch this with other operations?
- [ ] Do I already have this information?
- [ ] Is this the minimum I need?

**During Implementation:**

- [ ] Reading only necessary files?
- [ ] Using specific search patterns?
- [ ] Batching parallel operations?
- [ ] Keeping responses concise?
- [ ] Avoiding redundant explanations?

**Response Writing:**

- [ ] Stating action clearly (1 line)?
- [ ] Proceeding directly to work?
- [ ] Reporting concisely?
- [ ] Omitting unnecessary details?

---

## 🎯 Success Metrics

**Track these to measure optimization:**

1. **Tokens per task** - Target: 50-70% reduction
2. **Search-to-read ratio** - Target: 3:1 or higher
3. **Partial vs full reads** - Target: 80% partial
4. **Batch operation rate** - Target: 70%+ batched
5. **Response conciseness** - Target: <200 words unless detailed explanation needed

**Monthly Review:**
- Compare token usage vs previous month
- Identify optimization opportunities
- Update guidelines based on learnings

---

## 🚀 Quick Reference Card

**Think:**
- Minimum information needed?
- Search before read?
- Batch operations?
- Already have info?

**Search:**
- Glob → Grep → Read (cheap to expensive)
- Be specific (patterns, paths, types)
- Read partial when possible

**Respond:**
- State action (1 line)
- Execute immediately
- Report concisely
- Skip unnecessary details

**Batch:**
- Multiple reads together
- Multiple searches together
- Related edits together

**Target:**
- 50-70% token reduction
- Same or better quality
- Faster execution

---

**Remember: Every token saved is money saved and faster responses delivered.**

**Token optimization is not about doing less - it's about being smarter.** ⚡

---

**Version:** 1.0.0  
**Last Updated:** July 22, 2026  
**Applies to:** All AI platforms using JARVIS  
**Owner:** Deepak Rao Gaikwad
