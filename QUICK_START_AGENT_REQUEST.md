# ⚡ Quick Start: Agent Request Template

**Use this condensed template for fast agent requests. For detailed guidance, see [CURSOR_AGENT_WORKFLOW.md](./CURSOR_AGENT_WORKFLOW.md)**

---

## 🎯 REQUEST: [Title]

### Repositories
- Primary: https://github.com/[org]/[repo]
- Additional: [list if multi-repo]

### Task Type
- [ ] New Feature  
- [ ] Bug Fix  
- [ ] Refactor  
- [ ] Performance  
- [ ] Testing  
- [ ] Other: ___

### Requirements

**What to build:**
[Brief description]

**Acceptance criteria:**
1. [ ] Criterion 1
2. [ ] Criterion 2
3. [ ] Criterion 3

**Technical details:**
- Files to modify: 
- API endpoints: 
- Dependencies: 
- Environment vars needed:

### Testing
```bash
# Commands to run tests
npm test
```

**Expected results:**
- [ ] All tests pass
- [ ] Coverage >80%
- [ ] Build succeeds
- [ ] Linting passes

### PR Requirements
- Branch: `cursor/[type]/[description]-[id]`
- Base branch: `main`
- Labels: [bug, feature, etc.]
- Reviewers: [@deepakraog]

---

## 🤖 Agent Instructions

When you receive this request:

1. ✅ **Create TODO list** for task breakdown
2. 🔍 **Explore codebase** using sub-agents if needed
3. 💻 **Implement changes** with tests
4. 🧪 **Run full test suite** and verify
5. ✅ **Check prerequisites**: lint, build, type-check
6. 📤 **Create PR** as draft with comprehensive description
7. 📊 **Provide summary** of changes and testing

**Launch sub-agents for:**
- Complex codebases (explore agent)
- Comprehensive testing (test-runner)
- Multi-approach solutions (best-of-n-runner)

---

## 💡 Example: Quick Bug Fix

```markdown
## 🎯 REQUEST: Fix Login Button Not Working

**Repository:** https://github.com/myorg/app
**Task Type:** Bug Fix

**Requirements:**
Login button on `/login` page doesn't submit form. Console shows "handleSubmit is not defined".

**Acceptance Criteria:**
1. [ ] Login button submits form
2. [ ] User redirected to dashboard on success
3. [ ] Error message shown on failure

**Technical Details:**
- File: `src/pages/Login.tsx`
- Issue: Missing handleSubmit function
- Fix: Add form submission handler

**Testing:**
```bash
npm test -- Login.test.tsx
npm run test:e2e -- login.spec.ts
```

**PR Requirements:**
- Branch: `cursor/fix/login-button-submit-a1b2`
- Label: `bug`, `urgent`
```

---

## 📚 Full Documentation

- **Detailed Workflow:** [CURSOR_AGENT_WORKFLOW.md](./CURSOR_AGENT_WORKFLOW.md)
- **Automation Templates:** [.cursor/AUTOMATION_CONFIG_TEMPLATE.md](./.cursor/AUTOMATION_CONFIG_TEMPLATE.md)
- **Cursor Docs:** [cursor.com/docs/cloud-agent](https://cursor.com/docs/cloud-agent)

---

**Version:** 1.0.0 | **Owner:** Deepak Rao Gaikwad (@deepakraog)
