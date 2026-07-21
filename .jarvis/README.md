# 🤖 JARVIS Universal Protocol

**Platform-Agnostic AI Development Assistant**  
**Version:** 1.0.0  
**Owner:** Deepak Rao Gaikwad (@deepakraog)

---

## 🌐 Universal System

JARVIS is **platform-agnostic** - it works with ANY AI system:

- ✅ **Claude** (Anthropic)
- ✅ **Cursor Cloud Agents**
- ✅ **ChatGPT** (OpenAI)
- ✅ **Gemini** (Google)
- ✅ **GitHub Copilot**
- ✅ **Any LLM with file access**

**One system. Maintained in one place. Works everywhere.**

---

## 📍 Centralized Configuration

All JARVIS configuration lives in **this repository** at:
```
https://github.com/deepakraog/deepakraog
```

**Any AI agent** can access these instructions by:
1. Reading this repository
2. Following the documented protocols
3. Maintaining your standards automatically

**You never have to repeat yourself across platforms.**

---

## 🎯 How It Works

### Step 1: Point Any AI to This Repo

**With Claude:**
```
Claude, I have a development assistant system called JARVIS.
Please read these instructions:
https://github.com/deepakraog/deepakraog

Then follow the JARVIS protocol for all development work.
```

**With Cursor:**
```
Cursor, use my JARVIS system from:
https://github.com/deepakraog/deepakraog

Follow all protocols documented there.
```

**With ChatGPT:**
```
ChatGPT, I use JARVIS as my development assistant.
Instructions are at:
https://github.com/deepakraog/deepakraog

Please follow the JARVIS_QUICKSTART.md guide.
```

### Step 2: Give Commands

**All platforms understand:**
```
JARVIS, add dark mode to the dashboard
```

```
JARVIS, fix the API timeout issue
```

```
JARVIS, optimize database queries
```

### Step 3: AI Follows Protocol

**Every AI reads:**
1. `UNIVERSAL_AGENT_INSTRUCTIONS.md` - Core protocols
2. `COMMIT_GUIDELINES.md` - Git standards
3. `JARVIS_QUICKSTART.md` - Command patterns
4. Repository-specific `.cursor/config.json`

**Result:** Consistent behavior across all platforms.

---

## 🔧 Platform-Specific Setup

### For Claude (Anthropic)

**Option 1: Claude Desktop (with MCP)**
```bash
# Add to Claude Desktop config
{
  "mcpServers": {
    "jarvis": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token",
        "REPOSITORY": "deepakraog/deepakraog"
      }
    }
  }
}
```

**Option 2: Claude Web (Projects)**
```
1. Create Project: "JARVIS Development"
2. Add Knowledge:
   - Upload JARVIS_QUICKSTART.md
   - Upload UNIVERSAL_AGENT_INSTRUCTIONS.md
   - Upload COMMIT_GUIDELINES.md
3. Set Custom Instructions:
   "I am JARVIS, Deepak's AI development assistant.
    Follow protocols in uploaded documents."
```

**Option 3: Claude API**
```python
import anthropic

# Load JARVIS instructions
with open('UNIVERSAL_AGENT_INSTRUCTIONS.md', 'r') as f:
    jarvis_protocol = f.read()

client = anthropic.Anthropic(api_key="your_key")

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=8096,
    system=f"""You are JARVIS, an AI development assistant.

{jarvis_protocol}

Follow all protocols exactly.""",
    messages=[
        {"role": "user", "content": "JARVIS, add dark mode to dashboard"}
    ]
)
```

### For Cursor

**Already integrated!** Cursor Cloud Agents automatically read this repo.

```
1. Open Cursor
2. Start Cloud Agent
3. Agent reads JARVIS protocols from this repo
4. Say: "JARVIS, [your task]"
```

### For ChatGPT

**Option 1: GPTs (Custom GPT)**
```
1. Create GPT: "JARVIS Development Assistant"
2. Instructions:
   "You are JARVIS. Read protocols from:
    github.com/deepakraog/deepakraog
    Follow JARVIS_QUICKSTART.md for commands."
3. Capabilities:
   - Code Interpreter: ON
   - Web Browsing: ON
   - DALL-E: OFF
4. Upload key documents as Knowledge
```

**Option 2: ChatGPT Plus (Projects)**
```
1. Create Project: "JARVIS"
2. Upload documents:
   - JARVIS_QUICKSTART.md
   - UNIVERSAL_AGENT_INSTRUCTIONS.md
   - COMMIT_GUIDELINES.md
3. Custom Instructions in Project
```

### For GitHub Copilot

**Copilot Workspace:**
```
1. Create .github/copilot-instructions.md:

# JARVIS Protocol for Copilot

Follow instructions from:
https://github.com/deepakraog/deepakraog

Key protocols:
- GPG-signed commits
- Conventional format
- SOLID principles
- 80%+ test coverage
```

### For Any LLM (Universal)

**If the AI can read files:**
```
You are JARVIS, Deepak's AI development assistant.

Read and follow these protocols:
1. [repo]/UNIVERSAL_AGENT_INSTRUCTIONS.md
2. [repo]/COMMIT_GUIDELINES.md
3. [repo]/JARVIS_QUICKSTART.md

All development work must follow these standards.
```

---

## 📂 Repository Structure

```
deepakraog/deepakraog/
│
├── .jarvis/                          # JARVIS configuration
│   ├── README.md                     # This file
│   └── PLATFORM_SETUP.md            # Platform-specific guides
│
├── JARVIS_QUICKSTART.md             # Daily usage guide
├── UNIVERSAL_AGENT_INSTRUCTIONS.md  # Core protocols
├── COMMIT_GUIDELINES.md             # Git standards
├── AUTONOMOUS_WORKFLOW.md           # 24/7 workflow
├── DESIGN_PHASE_TEMPLATE.md         # Design protocols
├── STAKEHOLDER_PRESENTATION_TEMPLATE.md
├── PRE_COMMIT_HOOKS_SETUP.md
├── CURSOR_AGENT_WORKFLOW.md
├── QUICK_START_AGENT_REQUEST.md
├── AUTOMATION_CONFIG_TEMPLATE.md
├── AGENT_SETUP_SUMMARY.md
└── .cursor/
    ├── config.json                  # Repository config
    ├── COMMIT_GUIDELINES.md
    ├── AUTOMATION_CONFIG_TEMPLATE.md
    └── README.md
```

**All AIs read from the same source. One truth, many interfaces.**

---

## 🔄 Updating JARVIS

### Add New Feature

**Update once, applies everywhere:**

```bash
# In this repository
git clone https://github.com/deepakraog/deepakraog
cd deepakraog

# Update protocol
vim UNIVERSAL_AGENT_INSTRUCTIONS.md

# Commit
git commit -m "feat: add new JARVIS capability"
git push

# Now ALL platforms see the update:
# - Claude reads updated file
# - Cursor sees new protocol
# - ChatGPT uses updated instructions
# - Any AI gets latest version
```

### Version Control

```bash
# Tag versions
git tag -a v1.1.0 -m "JARVIS v1.1.0 - Added XYZ"
git push --tags

# Specific platform can pin to version
"Use JARVIS v1.1.0 protocols"
```

---

## 🎯 Universal Command Format

**All platforms understand:**

```
JARVIS, [action] [target] [details]

Examples:
JARVIS, add dark mode to dashboard
JARVIS, fix bug in payment flow
JARVIS, refactor auth service
JARVIS, update documentation
```

**With details:**
```
JARVIS, please [action]:

REPO: [github url]
TARGET: [what to change]
REQUIREMENTS:
- [requirement 1]
- [requirement 2]

[Additional context]
```

**Natural language:**
```
JARVIS, I need help with [problem].
Can you [solution]?
```

---

## 🔒 Security & Credentials

### Centralized Secrets

**Never in code. Store in:**

1. **GitHub Secrets** (for GitHub Actions)
2. **Cursor Secrets** (for Cursor agents)
3. **Environment Variables** (for local development)
4. **1Password/Vault** (for team sharing)

**In .jarvis/config.json:**
```json
{
  "secrets": {
    "required": ["GITHUB_TOKEN", "OPENAI_API_KEY"],
    "storage": "github-secrets",
    "reference": "cursor.com/cloud-agents/secrets"
  }
}
```

### Git Configuration

**Set once per platform:**

```bash
# Claude, Cursor, ChatGPT all use:
git config user.name "Deepak Rao Gaikwad"
git config user.email "gaikwad.dcg@gmail.com"
git config commit.gpgsign true
git config user.signingkey YOUR_GPG_KEY
```

---

## 📊 Platform Comparison

| Feature | Claude | Cursor | ChatGPT | Copilot |
|---------|--------|--------|---------|---------|
| **Read GitHub** | ✅ MCP | ✅ Native | ✅ Browse | ✅ Native |
| **File Access** | ✅ Yes | ✅ Yes | ✅ Upload | ✅ Yes |
| **Git Integration** | ⚠️ Manual | ✅ Auto | ⚠️ Manual | ✅ Auto |
| **24/7 Operation** | ⚠️ API only | ✅ Cloud Agents | ⚠️ API only | ❌ No |
| **Code Execution** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| **Custom Instructions** | ✅ Projects | ✅ .cursor/ | ✅ GPTs | ✅ .github/ |
| **JARVIS Compatible** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

**All platforms can follow JARVIS protocols!**

---

## 🚀 Best Practices

### 1. Keep Instructions Updated

```bash
# Update JARVIS protocols regularly
cd deepakraog/deepakraog
git pull origin main

# All platforms automatically see updates
```

### 2. Use Repository-Specific Config

**In each project repository:**
```
your-project/
├── .jarvis/
│   └── config.json       # Project-specific settings
└── .cursor/
    └── config.json       # Cursor-specific (if needed)
```

**Example `.jarvis/config.json`:**
```json
{
  "jarvis": {
    "protocolVersion": "1.0.0",
    "protocolSource": "github.com/deepakraog/deepakraog",
    "repository": {
      "type": "frontend",
      "language": "typescript",
      "framework": "nextjs"
    },
    "quality": {
      "testCoverage": 80,
      "lintingRequired": true
    },
    "deployment": {
      "productionBranch": "main",
      "requiresApproval": true
    }
  }
}
```

### 3. Document Platform-Specific Quirks

**In `.jarvis/PLATFORM_NOTES.md`:**
```markdown
## Claude
- Use Projects for context persistence
- MCP for GitHub integration
- Manual git operations

## Cursor
- Native git integration
- Cloud Agents for 24/7
- .cursor/config.json for settings

## ChatGPT
- Use GPTs for consistency
- Upload documents to Knowledge
- Manual git operations
```

---

## 🔧 Troubleshooting

### Issue: AI Not Following Protocol

**Solution:**
```
[AI Platform], please re-read JARVIS protocols:
https://github.com/deepakraog/deepakraog

Specifically:
- UNIVERSAL_AGENT_INSTRUCTIONS.md
- COMMIT_GUIDELINES.md

Then continue with: [your task]
```

### Issue: Inconsistent Behavior Across Platforms

**Solution:**
```bash
# Check protocol version in each platform
# Ensure all platforms reference same commit/tag

# Pin to specific version:
"Use JARVIS protocols from:
github.com/deepakraog/deepakraog @ v1.0.0"
```

### Issue: Platform Can't Access GitHub

**Solution:**
```
Option 1: Upload key documents directly
- JARVIS_QUICKSTART.md
- UNIVERSAL_AGENT_INSTRUCTIONS.md
- COMMIT_GUIDELINES.md

Option 2: Use API/MCP for access
- Claude: MCP server
- Cursor: Native access
- ChatGPT: Web browsing
```

---

## 📈 Analytics & Monitoring

### Track JARVIS Usage

**In `.jarvis/analytics.json`:**
```json
{
  "usage": {
    "claude": {
      "totalCommands": 150,
      "lastUsed": "2026-07-21T23:00:00Z"
    },
    "cursor": {
      "totalCommands": 320,
      "lastUsed": "2026-07-21T22:30:00Z"
    },
    "chatgpt": {
      "totalCommands": 45,
      "lastUsed": "2026-07-20T15:00:00Z"
    }
  }
}
```

### Monitor Quality

```bash
# Check if protocols are being followed
git log --grep="^(feat|fix|docs):" --oneline

# Verify GPG signatures
git log --show-signature -10

# Check test coverage trend
# (tracked in CI/CD)
```

---

## 🎓 Quick Start for New Platform

**Adding JARVIS to ANY AI platform:**

1. **Point to protocols:**
   ```
   [AI], use JARVIS from github.com/deepakraog/deepakraog
   ```

2. **Set identity:**
   ```
   You are JARVIS, Deepak's AI development assistant.
   ```

3. **Load key documents:**
   - JARVIS_QUICKSTART.md
   - UNIVERSAL_AGENT_INSTRUCTIONS.md
   - COMMIT_GUIDELINES.md

4. **Test:**
   ```
   JARVIS, introduce yourself and confirm protocol version
   ```

5. **Use:**
   ```
   JARVIS, [your first task]
   ```

**That's it! JARVIS is now available on that platform.**

---

## 🌟 Benefits of Universal JARVIS

✅ **Write Once, Use Everywhere**
- Update protocols in one place
- All platforms see changes instantly
- No duplication of documentation

✅ **Consistent Behavior**
- Same standards across all AIs
- GPG signing works everywhere
- Code quality maintained universally

✅ **Platform Freedom**
- Use Claude for complex reasoning
- Use Cursor for 24/7 automation
- Use ChatGPT for quick tasks
- Switch platforms anytime

✅ **Easy Maintenance**
- Single source of truth
- Version controlled
- Git history of all changes

✅ **Extensible**
- Add new platforms easily
- Enhance protocols once
- Benefits all platforms

---

**JARVIS is now universal. One system, infinite possibilities.** 🌐

---

**Protocol Version:** 1.0.0  
**Last Updated:** July 21, 2026  
**Maintained by:** Deepak Rao Gaikwad  
**Repository:** github.com/deepakraog/deepakraog  
**Compatible with:** All AI platforms with file/repo access
