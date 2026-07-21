# 🤖 Cursor Cloud Agent Development Workflow

**Owner:** Deepak Rao Gaikwad (@deepakraog)  
**Last Updated:** July 21, 2026  
**Purpose:** Standardized template for submitting development requests to Cursor Cloud Agents

---

## 📋 Overview

This document provides a structured approach for working with Cursor Cloud Agents to implement features, fix bugs, and manage the complete software development lifecycle across multiple projects.

### What Cloud Agents Can Do

✅ **Full-Stack Development:** Frontend, backend, mobile, databases  
✅ **AI Integration:** LLM APIs, agent systems, MCP tooling  
✅ **Testing:** Unit tests, integration tests, E2E tests  
✅ **Multi-Repository Work:** Work across multiple connected repos  
✅ **PR Management:** Create, update, and manage pull requests  
✅ **Sub-Agent Orchestration:** Launch specialized agents for complex tasks  
✅ **Prerequisites Verification:** Linting, testing, build checks before PR creation  

---

## 🚀 Automation Options Available

### 1. **Cursor Automations** (Recommended)

Cursor Automations trigger Cloud Agents automatically based on events. You can set these up at [cursor.com](https://cursor.com).

#### Available Triggers:

| Trigger Type | When It Fires | Use Cases |
|---|---|---|
| **Scheduled (Cron)** | On a recurring schedule | Regular maintenance, dependency updates, reports |
| **PR Opened** | When a non-draft PR is created | Code review, testing, analysis |
| **PR Pushed** | New commits pushed to existing PR | Re-run tests, update documentation |
| **PR Commented** | Someone comments on a PR | Respond to review feedback |
| **Push to Branch** | Commits pushed to specific branch | Deploy to staging, run checks |
| **GitHub CI Completed** | CI check finishes | Follow-up actions after tests |
| **Webhook** | HTTP POST to private endpoint | Custom integrations, external triggers |
| **Slack Message** | Message in connected channel | Team requests, incident response |
| **Linear Issue Created** | New issue in Linear | Auto-assign, create implementation branch |
| **Linear Status Changed** | Issue status changes | Sync with GitHub, notify team |

#### Setup Steps:

1. Go to [cursor.com/automations](https://cursor.com/automations)
2. Click "New Automation"
3. Choose trigger(s) from the list above
4. Write agent instructions (use template below)
5. Select repositories
6. Enable optional tools (Slack, MCP, etc.)
7. Save and activate

#### Webhook Triggers:

For custom integrations, webhook triggers provide a private HTTP endpoint:

```bash
# Example: Trigger agent via webhook
curl -X POST https://cursor.com/webhooks/your-automation-id \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Fix the bug in user authentication",
    "priority": "high"
  }'
```

**Note:** You must save the automation first to generate the webhook URL and API key.

### 2. **Manual Cloud Agent Launch** (Current Method)

Start a Cloud Agent manually from:
- Cursor Desktop IDE
- Cursor Mobile App
- [cursor.com](https://cursor.com)

Use the requirement template below to provide comprehensive context.

### 3. **GitHub Actions Integration**

You can integrate Cloud Agents into GitHub Actions workflows:

```yaml
name: Cursor Agent on PR
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  cursor-agent:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Cursor Agent
        run: |
          curl -X POST ${{ secrets.CURSOR_WEBHOOK_URL }} \
            -H "Authorization: Bearer ${{ secrets.CURSOR_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "prompt": "Review PR #${{ github.event.pull_request.number }} and suggest improvements",
              "ref": "${{ github.ref }}"
            }'
```

---

## 📝 Requirement Submission Template

Copy and fill this template when requesting feature development or bug fixes:

```markdown
## 🎯 REQUEST: [Brief Title]

### 1. PROJECT INFORMATION

**Primary Repository:**
- URL: https://github.com/[org]/[repo]
- Branch: [main/develop/feature-branch]
- Technology Stack: [Node.js, React, Python, etc.]

**Additional Repositories (if multi-repo):**
- Repo 2: https://github.com/[org]/[repo2] (Purpose: [backend/frontend/shared])
- Repo 3: https://github.com/[org]/[repo3] (Purpose: [microservice/library])

**Project Type:**
- [ ] Web Application (Frontend)
- [ ] Web Application (Backend/API)
- [ ] Mobile Application (iOS/Android/React Native/Flutter)
- [ ] CLI Tool
- [ ] Library/Package
- [ ] Microservice
- [ ] AI Agent/Integration
- [ ] Other: __________

---

### 2. TASK TYPE

- [ ] **New Feature Development**
- [ ] **Bug Fix**
- [ ] **Refactoring**
- [ ] **Performance Optimization**
- [ ] **Security Enhancement**
- [ ] **Documentation**
- [ ] **Testing** (Unit/Integration/E2E)
- [ ] **Infrastructure/DevOps**
- [ ] **AI Integration**
- [ ] **Database Migration**
- [ ] **Other:** __________

---

### 3. DETAILED REQUIREMENTS

#### Background/Context:
[Explain the business context, user story, or problem statement]

Example:
- Users are currently unable to reset their passwords
- We need a new dashboard for analytics
- The payment API is timing out under load

#### Acceptance Criteria:
[List specific, testable outcomes]

1. [ ] Criterion 1
2. [ ] Criterion 2
3. [ ] Criterion 3

Example:
1. [ ] User can click "Forgot Password" and receive email within 1 minute
2. [ ] Password reset link expires after 24 hours
3. [ ] New password must meet complexity requirements (8+ chars, 1 number, 1 special char)
4. [ ] Unit tests cover all edge cases
5. [ ] Integration tests pass with 100% success rate

#### Technical Specifications:
[Provide technical details, architecture decisions, or constraints]

- API Endpoints: `POST /api/auth/reset-password`
- Database Schema: Add `password_reset_token` and `token_expiry` columns to `users` table
- Third-party Services: Use SendGrid for email delivery
- Authentication: JWT-based with refresh tokens
- Rate Limiting: Max 3 reset attempts per hour per email

#### Dependencies:
[List any prerequisites or related work]

- Depends on #123 (user authentication refactor)
- Requires AWS SES credentials (stored in Secrets)
- Needs Redis for token storage

---

### 4. ENVIRONMENT & CONFIGURATION

**Environment Variables Required:**
```bash
DATABASE_URL=postgres://...
REDIS_URL=redis://...
SENDGRID_API_KEY=[Stored in Cursor Secrets]
JWT_SECRET=[Stored in Cursor Secrets]
```

**Secrets Management:**
- Add secrets at: [cursor.com/cloud-agents/secrets](https://cursor.com/cloud-agents/secrets)
- Scope: User/Team/Repo-specific

**Package Manager:**
- [ ] npm
- [ ] yarn
- [ ] pnpm
- [ ] pip
- [ ] cargo
- [ ] go modules
- [ ] Other: __________

**Required Tools/CLIs:**
```bash
# Example
node >= 18.x
docker >= 24.x
aws-cli
terraform
```

---

### 5. TESTING REQUIREMENTS

**Test Coverage Expected:**
- [ ] Unit Tests (Target: 80%+ coverage)
- [ ] Integration Tests
- [ ] E2E Tests
- [ ] Performance Tests
- [ ] Security Tests (OWASP Top 10)
- [ ] Load Tests

**Test Frameworks:**
- [ ] Jest
- [ ] Vitest
- [ ] Pytest
- [ ] Go Test
- [ ] Cypress
- [ ] Playwright
- [ ] Other: __________

**Testing Instructions:**
```bash
# Commands to run tests
npm test
npm run test:integration
npm run test:e2e
```

**Expected Test Results:**
- All existing tests must pass
- New tests added for new functionality
- No regression in code coverage
- Performance benchmarks met (e.g., API response < 200ms)

---

### 6. DEPLOYMENT & CI/CD

**Pre-Deployment Checks:**
- [ ] Linting passes (`npm run lint`)
- [ ] Type checking passes (`npm run type-check`)
- [ ] Build succeeds (`npm run build`)
- [ ] Tests pass (`npm test`)
- [ ] Security scan passes (Snyk/Dependabot)
- [ ] Bundle size within limits
- [ ] No console.log or debugger statements

**Deployment Target:**
- [ ] Staging Environment
- [ ] Production Environment
- [ ] Preview/Feature Environment
- [ ] Not applicable (library/package)

**CI/CD Integration:**
- GitHub Actions workflows: `.github/workflows/ci.yml`
- Required status checks before PR merge
- Automated deployment on merge to `main`

---

### 7. PULL REQUEST INSTRUCTIONS

**Branch Naming Convention:**
```
cursor/[feature|fix|refactor|docs]/[brief-description]-[random-id]

Examples:
- cursor/feature/password-reset-flow-a1b2
- cursor/fix/payment-timeout-issue-c3d4
- cursor/refactor/auth-module-cleanup-e5f6
```

**Commit Message Format:**
```
[type]: Brief description (50 chars max)

Longer description if needed (72 chars per line)

- Bullet points for changes
- Reference issues: Fixes #123, Closes #456

[Breaking changes if any]
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`, `style`, `ci`

**PR Template:**
- Use template at: `.github/PULL_REQUEST_TEMPLATE.md` (if exists)
- Include: Summary, Testing steps, Screenshots (UI changes), Breaking changes

**PR Requirements:**
- [ ] Create as draft initially
- [ ] Mark ready for review only after all tests pass
- [ ] Link related issues
- [ ] Add appropriate labels (bug, enhancement, breaking-change)
- [ ] Request reviewers: [@deepakraog, @team-member]

**Auto-Merge:**
- [ ] Enable auto-merge after approvals
- [ ] Do NOT enable auto-merge (manual review required)

---

### 8. DOCUMENTATION REQUIREMENTS

**Documentation to Update:**
- [ ] README.md
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Architecture diagrams
- [ ] Inline code comments (for complex logic only)
- [ ] CHANGELOG.md
- [ ] Migration guides (breaking changes)

**Documentation Style:**
- Clear, concise language
- Code examples for new APIs
- Before/after examples for breaking changes
- Diagrams for architecture changes (Mermaid preferred)

---

### 9. AGENT WORKFLOW INSTRUCTIONS

**For the Cursor Cloud Agent:**

When you receive this request, follow this workflow:

1. **🔍 Discovery Phase:**
   - Read all provided repositories
   - Understand current architecture
   - Identify affected modules
   - Check for existing tests and patterns

2. **📋 Planning Phase:**
   - Create TODO list with specific, actionable tasks
   - Break down complex tasks into sub-tasks
   - Identify potential risks or blockers
   - Estimate complexity (simple/moderate/complex)

3. **💻 Implementation Phase:**
   - Create feature branch following naming convention
   - Implement changes incrementally
   - Write tests alongside code (TDD preferred)
   - Follow existing code style and patterns
   - Add necessary documentation
   - Commit frequently with clear messages

4. **🧪 Testing Phase:**
   - Run all existing tests
   - Add new tests for new functionality
   - Perform integration testing
   - Test edge cases and error scenarios
   - Verify no regressions
   - Run linters and type checkers

5. **✅ Pre-PR Phase:**
   - Run full test suite
   - Verify all prerequisites pass
   - Build project successfully
   - Review own changes for quality
   - Update documentation
   - Clean up temporary/debug code

6. **📤 PR Creation Phase:**
   - Push changes to feature branch
   - Create PR with comprehensive description
   - Link related issues
   - Add appropriate labels
   - Include testing steps
   - Add screenshots/videos (UI changes)
   - Set as draft initially

7. **🔄 Review & Iteration Phase:**
   - Monitor CI/CD pipelines
   - Fix any failing checks
   - Update PR based on test results
   - Mark ready for review when all checks pass
   - Respond to review comments (if automation configured)

8. **📊 Summary Phase:**
   - Provide summary of changes made
   - List all tests added/modified
   - Note any deviations from requirements
   - Highlight areas needing human review
   - Document any blockers encountered

**Sub-Agent Usage:**

Launch specialized sub-agents when:
- **Explore Agent:** Understanding large codebases, finding related code
- **Test Runner Agent:** Running comprehensive test suites
- **General Purpose Agent:** Complex refactoring, multi-file changes
- **Best-of-N Runner:** Trying multiple implementation approaches in parallel

---

### 10. SKILLS & CAPABILITIES TO LEVERAGE

The agent has access to these specialized skills (automatically applied when relevant):

**GSAP Animation Skills:**
- `gsap-core`: Basic animations, tweens, easing
- `gsap-react`: React-specific animation patterns
- `gsap-frameworks`: Vue, Svelte animations
- `gsap-scrolltrigger`: Scroll-based animations
- `gsap-timeline`: Animation sequencing
- `gsap-plugins`: Advanced GSAP features
- `gsap-performance`: Animation optimization

**General Capabilities:**
- Full-stack development (Node.js, TypeScript, Rust, Go, Python, Java)
- Frontend frameworks (React, Angular, Vue, Svelte)
- Mobile development (React Native, Flutter)
- Cloud infrastructure (AWS, GCP, Docker, Kubernetes)
- Database design (PostgreSQL, MongoDB, DynamoDB, Redis)
- AI/ML integration (OpenAI, Claude, LangChain, MCP)
- Testing frameworks (Jest, Vitest, Pytest, Cypress, Playwright)
- CI/CD pipelines (GitHub Actions, Jenkins)

---

### 11. EXAMPLES

#### Example 1: Simple Bug Fix

```markdown
## 🎯 REQUEST: Fix Password Reset Email Not Sending

**Primary Repository:** https://github.com/myorg/auth-service
**Branch:** main
**Technology Stack:** Node.js, Express, TypeScript, PostgreSQL

**Task Type:** Bug Fix

**Requirements:**
Password reset emails are not being sent when users click "Forgot Password".
Investigation shows the SendGrid API call is failing with 401 Unauthorized.

**Acceptance Criteria:**
1. [ ] Password reset emails successfully sent
2. [ ] Error handling for email failures
3. [ ] Tests verify email sending logic
4. [ ] User sees appropriate error message if email fails

**Technical Details:**
- Issue: SendGrid API key rotation broke the integration
- Solution: Update API key from Cursor Secrets
- File: `src/services/email.service.ts`

**Testing:**
```bash
npm test -- email.service.test.ts
```

**PR Requirements:**
- Branch: `cursor/fix/sendgrid-api-key-c7d8`
- Draft PR initially
- Add label: `bug`, `urgent`
```

#### Example 2: New Feature

```markdown
## 🎯 REQUEST: Add Real-Time Dashboard with WebSocket Support

**Primary Repository:** https://github.com/myorg/dashboard-app
**Branch:** develop
**Technology Stack:** React, TypeScript, Socket.io, Node.js

**Task Type:** New Feature Development

**Requirements:**
Build a real-time analytics dashboard that updates live without page refresh.

**Acceptance Criteria:**
1. [ ] WebSocket connection established on dashboard load
2. [ ] Live data updates every 5 seconds
3. [ ] Graceful reconnection on connection loss
4. [ ] Performance: handles 1000+ updates/min
5. [ ] Unit tests: 80%+ coverage
6. [ ] E2E tests: user can see live updates

**Technical Specifications:**
- Frontend: React + Socket.io-client
- Backend: Socket.io server in Express
- Data: Fetch from `/api/analytics/stream`
- Charts: Use Recharts library
- Authentication: JWT tokens for WebSocket auth

**Dependencies:**
- Install: `socket.io`, `socket.io-client`, `recharts`
- Requires Redis for pub/sub (already configured)

**Testing Requirements:**
- Unit tests: Jest
- E2E tests: Playwright
- Load tests: Socket.io-client benchmark (1000 concurrent connections)

**PR Requirements:**
- Branch: `cursor/feature/realtime-dashboard-e9f0`
- Include demo video/GIF
- Documentation: Add WebSocket API docs to README
```

---

## 🔐 Security & Secrets Management

### Adding Secrets

1. Go to [cursor.com/cloud-agents/secrets](https://cursor.com/cloud-agents/secrets)
2. Add secrets with appropriate scope:
   - **User:** Only you can use
   - **Team:** All team members can use
   - **Repo:** Scoped to specific repository

### Common Secrets Needed

```bash
# Database
DATABASE_URL
DB_PASSWORD

# APIs
OPENAI_API_KEY
ANTHROPIC_API_KEY
SENDGRID_API_KEY
STRIPE_SECRET_KEY

# Cloud
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
GCP_SERVICE_ACCOUNT_KEY

# Authentication
JWT_SECRET
SESSION_SECRET
OAUTH_CLIENT_ID
OAUTH_CLIENT_SECRET
```

### Best Practices

- Never commit secrets to repositories
- Rotate secrets regularly
- Use different secrets for dev/staging/prod
- Grant minimum required permissions
- Audit secret usage periodically

---

## 📚 Resources

### Cursor Documentation
- [Cloud Agents](https://cursor.com/docs/cloud-agent)
- [Automations](https://cursor.com/docs/cloud-agent/automations)
- [Webhooks API](https://cursor.com/docs/cloud-agent/api/webhooks)
- [Secrets Management](https://cursor.com/docs/cloud-agent/secrets)

### Agent Dashboard
- **This Run:** https://cursor.com/agents/bc-019f86ea-87ef-75a3-ad06-d8fdb136304b
- **All Agents:** [cursor.com/cloud-agents](https://cursor.com/cloud-agents)
- **Automations:** [cursor.com/automations](https://cursor.com/automations)

### Support
- Email: deepaksraog@gmail.com
- LinkedIn: [linkedin.com/in/deepakraog](https://linkedin.com/in/deepakraog)

---

## 🎯 Quick Start Checklist

Before submitting a request to a Cloud Agent:

- [ ] Filled out requirement template completely
- [ ] Provided repository URLs and access
- [ ] Added necessary secrets to Cursor dashboard
- [ ] Specified technology stack and dependencies
- [ ] Defined clear acceptance criteria
- [ ] Listed testing requirements
- [ ] Specified PR requirements and branch naming
- [ ] Reviewed existing codebase structure
- [ ] Identified related issues/PRs

---

## 📊 Agent Performance Tracking

Track agent effectiveness over time:

| Metric | Target | How to Measure |
|---|---|---|
| PR Success Rate | >90% | PRs merged without major revisions |
| Test Coverage | >80% | Code coverage reports |
| Time to PR | <2 hours | Time from request to PR creation |
| Build Success | 100% | CI/CD pipeline pass rate |
| Bug Introduction | <5% | Bugs found post-merge |
| Code Review Cycles | <2 | Rounds of review before approval |

Review agent performance monthly to optimize prompts and workflows.

---

## 🚀 Advanced Usage

### Multi-Repository Coordination

When working across multiple repositories:

```markdown
**Repositories:**
1. Frontend: https://github.com/myorg/frontend
   - Changes: Update API client with new endpoints
   
2. Backend: https://github.com/myorg/backend
   - Changes: Add new REST endpoints
   
3. Shared: https://github.com/myorg/shared-types
   - Changes: Update TypeScript interfaces

**Coordination:**
- Update shared-types first (version 1.2.0)
- Backend depends on shared-types@1.2.0
- Frontend depends on shared-types@1.2.0
- Create PRs in order: shared → backend → frontend
```

### Complex Workflows

For complex features spanning multiple PRs:

```markdown
**Epic:** User Profile Redesign

**Phase 1:** Database Schema Changes
- Repository: backend
- Branch: cursor/feature/user-profile-schema-a1b2

**Phase 2:** API Endpoints
- Repository: backend
- Branch: cursor/feature/user-profile-api-c3d4
- Depends on: Phase 1 merged

**Phase 3:** Frontend UI
- Repository: frontend
- Branch: cursor/feature/user-profile-ui-e5f6
- Depends on: Phase 2 merged

**Submit phases separately, wait for Phase N to merge before starting Phase N+1**
```

---

## 📞 Feedback & Improvements

This workflow is a living document. Provide feedback on:

- Template clarity and completeness
- Agent performance and accuracy
- Missing sections or information
- Automation suggestions

**Last Review:** July 21, 2026  
**Next Review:** August 21, 2026  
**Version:** 1.0.0

---

**Happy Building! 🚀**
