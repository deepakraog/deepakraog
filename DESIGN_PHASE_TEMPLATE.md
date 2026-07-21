# 🏗️ Design Phase Template for Cursor Cloud Agents

**Purpose:** Comprehensive design documentation before implementation  
**Owner:** Deepak Rao Gaikwad (@deepakraog)  
**Version:** 1.0.0

---

## 📋 Overview

This template ensures thorough design and architectural planning before any code changes. Agents should complete this phase for all non-trivial changes (new features, refactoring, infrastructure changes).

---

## 1️⃣ HIGH-LEVEL DESIGN (HLD)

### 1.1 Problem Statement

**What problem are we solving?**
[Clear description of the business/technical problem]

**Why is this important?**
[Business value, user impact, technical debt, performance issues]

**Current State:**
- What exists today
- Pain points and limitations
- Metrics (if applicable): response time, error rate, user complaints

**Desired State:**
- What we want to achieve
- Success metrics
- Timeline constraints (if any)

---

### 1.2 Proposed Solution Overview

**High-Level Approach:**
[Brief description of the solution strategy]

**Key Components:**
1. Component A - [Purpose]
2. Component B - [Purpose]
3. Component C - [Purpose]

**System Context Diagram:**
```mermaid
graph TB
    User[User/Client] --> API[API Gateway]
    API --> Service1[Service 1]
    API --> Service2[Service 2]
    Service1 --> DB[(Database)]
    Service2 --> Cache[(Cache)]
```

**Data Flow:**
```mermaid
sequenceDiagram
    participant Client
    participant API
    participant Service
    participant Database
    
    Client->>API: Request
    API->>Service: Process
    Service->>Database: Query
    Database-->>Service: Data
    Service-->>API: Response
    API-->>Client: Result
```

---

### 1.3 Architecture Decisions

**Architectural Style:**
- [ ] Monolithic
- [ ] Microservices
- [ ] Serverless
- [ ] Event-Driven
- [ ] Layered
- [ ] Hexagonal/Clean Architecture
- [ ] Other: __________

**Key Decisions:**

| Decision | Options Considered | Chosen Option | Rationale |
|----------|-------------------|---------------|-----------|
| Database | PostgreSQL, MongoDB, DynamoDB | PostgreSQL | ACID compliance required for transactions |
| API Style | REST, GraphQL, gRPC | REST | Simple CRUD operations, wide client support |
| Caching | Redis, Memcached, In-memory | Redis | Pub/sub needed for real-time updates |
| Authentication | JWT, OAuth2, Sessions | JWT | Stateless, works well with microservices |

---

### 1.4 Technology Stack

**New Project:**
```yaml
Backend:
  Language: TypeScript (Node.js 20+)
  Framework: Express / Fastify / NestJS
  ORM: Prisma / TypeORM
  Validation: Zod / Joi
  
Frontend:
  Language: TypeScript
  Framework: React 18+ / Next.js 14+
  State: Zustand / Redux Toolkit
  Styling: Tailwind CSS
  
Database:
  Primary: PostgreSQL 16+
  Cache: Redis 7+
  
Infrastructure:
  Cloud: AWS / GCP
  Containers: Docker
  Orchestration: Kubernetes / ECS
  IaC: Terraform
  
Observability:
  Logging: Winston / Pino
  Monitoring: Datadog / Prometheus
  Tracing: OpenTelemetry
  
CI/CD:
  Pipeline: GitHub Actions
  Testing: Jest, Playwright
  Quality: SonarQube
```

**Existing Project:**
```yaml
Current Stack:
  Backend: Node.js 18, Express
  Frontend: React 17
  Database: PostgreSQL 14
  
Additions/Changes:
  - Upgrade Node.js 18 → 20 (LTS)
  - Add Redis for caching
  - Introduce TypeScript (gradual migration)
  - Add OpenTelemetry for tracing
  
Migration Strategy:
  Phase 1: Add new components in TypeScript
  Phase 2: Migrate critical paths
  Phase 3: Full migration
```

---

### 1.5 Infrastructure Architecture

**Deployment Architecture:**
```mermaid
graph TB
    subgraph "Production Environment"
        LB[Load Balancer]
        subgraph "Application Tier"
            App1[App Instance 1]
            App2[App Instance 2]
            App3[App Instance 3]
        end
        subgraph "Data Tier"
            Primary[(Primary DB)]
            Replica[(Read Replica)]
            Cache[Redis Cluster]
        end
        LB --> App1
        LB --> App2
        LB --> App3
        App1 --> Primary
        App2 --> Primary
        App3 --> Primary
        App1 --> Replica
        App2 --> Replica
        App3 --> Replica
        App1 --> Cache
        App2 --> Cache
        App3 --> Cache
    end
```

**Infrastructure Changes:**

| Component | Current | Proposed | Reason |
|-----------|---------|----------|--------|
| Compute | EC2 t3.medium | ECS Fargate | Better scaling, lower management |
| Database | Single RDS instance | Multi-AZ with replica | High availability |
| Cache | None | ElastiCache Redis | Reduce DB load |
| CDN | None | CloudFront | Static asset delivery |

**Scaling Strategy:**
- Horizontal scaling for application tier (target: 70% CPU)
- Vertical scaling for database (monitor IOPS)
- Auto-scaling rules: min 2, max 10 instances
- Database connection pooling (max 100 connections per instance)

---

### 1.6 Performance Considerations

**Target Metrics:**

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| API Response Time (p95) | 800ms | 200ms | 75% reduction |
| Database Query Time (p95) | 500ms | 50ms | 90% reduction |
| Page Load Time (FCP) | 3.2s | 1.5s | 53% reduction |
| Throughput | 100 req/s | 1000 req/s | 10x increase |
| Error Rate | 2.5% | <0.1% | 96% reduction |

**Optimization Strategies:**
1. **Caching:** Redis for frequently accessed data (TTL: 5 minutes)
2. **Database:** Indexes on `user_id`, `created_at`, composite indexes
3. **API:** Implement pagination (max 100 items per page)
4. **Frontend:** Code splitting, lazy loading, image optimization
5. **Network:** Enable gzip compression, HTTP/2

---

### 1.7 Capacity Planning

**Expected Load:**
- Current Users: 10,000 MAU
- Expected Growth: 50% YoY
- Peak Traffic: 3x average (during business hours)

**Resource Requirements:**

```yaml
Application Tier:
  Normal: 3 instances (2 vCPU, 4GB RAM each)
  Peak: 10 instances
  
Database:
  Instance: db.r6g.xlarge (4 vCPU, 32GB RAM)
  Storage: 500GB SSD (IOPS: 3000)
  Connections: 300 max
  
Cache:
  Instance: cache.r6g.large (2 vCPU, 13GB RAM)
  Memory: 10GB data + 3GB overhead
```

**Cost Estimate:**
- Compute: $500/month (normal), $1,200/month (peak)
- Database: $600/month
- Cache: $150/month
- Storage: $50/month
- **Total:** ~$1,300/month normal, ~$2,000/month peak

---

## 2️⃣ LOW-LEVEL DESIGN (LLD)

### 2.1 Component Design

**Component: User Authentication Service**

**Responsibilities:**
- User registration and login
- JWT token generation and validation
- Password hashing and verification
- Session management

**Interface:**
```typescript
interface AuthService {
  // User registration
  register(email: string, password: string, profile: UserProfile): Promise<User>;
  
  // User login
  login(email: string, password: string): Promise<AuthToken>;
  
  // Token validation
  validateToken(token: string): Promise<TokenPayload>;
  
  // Token refresh
  refreshToken(refreshToken: string): Promise<AuthToken>;
  
  // Password reset
  requestPasswordReset(email: string): Promise<void>;
  resetPassword(token: string, newPassword: string): Promise<void>;
}

interface User {
  id: string;
  email: string;
  profile: UserProfile;
  createdAt: Date;
  updatedAt: Date;
}

interface AuthToken {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
}

interface TokenPayload {
  userId: string;
  email: string;
  roles: string[];
  iat: number;
  exp: number;
}
```

**Implementation Details:**
```typescript
// SOLID Principles Applied:
// - Single Responsibility: Each class has one reason to change
// - Open/Closed: Extensible through interfaces
// - Liskov Substitution: Implementations can be swapped
// - Interface Segregation: Small, focused interfaces
// - Dependency Inversion: Depends on abstractions

class AuthServiceImpl implements AuthService {
  constructor(
    private readonly userRepository: UserRepository,
    private readonly tokenService: TokenService,
    private readonly passwordHasher: PasswordHasher,
    private readonly emailService: EmailService
  ) {}

  async register(
    email: string,
    password: string,
    profile: UserProfile
  ): Promise<User> {
    // Validate input
    this.validateEmail(email);
    this.validatePassword(password);
    
    // Check if user exists
    const existingUser = await this.userRepository.findByEmail(email);
    if (existingUser) {
      throw new ConflictError('User already exists');
    }
    
    // Hash password
    const hashedPassword = await this.passwordHasher.hash(password);
    
    // Create user (atomically)
    const user = await this.userRepository.create({
      email,
      passwordHash: hashedPassword,
      profile,
    });
    
    // Send welcome email (async, non-blocking)
    this.emailService.sendWelcomeEmail(user).catch(err => {
      logger.error('Failed to send welcome email', { userId: user.id, error: err });
    });
    
    return user;
  }

  async login(email: string, password: string): Promise<AuthToken> {
    // Retrieve user
    const user = await this.userRepository.findByEmail(email);
    if (!user) {
      // Use constant-time comparison to prevent timing attacks
      await this.passwordHasher.hash(password); // Dummy operation
      throw new UnauthorizedError('Invalid credentials');
    }
    
    // Verify password
    const isValid = await this.passwordHasher.verify(password, user.passwordHash);
    if (!isValid) {
      throw new UnauthorizedError('Invalid credentials');
    }
    
    // Generate tokens
    const accessToken = this.tokenService.generateAccessToken({
      userId: user.id,
      email: user.email,
      roles: user.roles,
    });
    
    const refreshToken = this.tokenService.generateRefreshToken({
      userId: user.id,
    });
    
    // Store refresh token (for revocation)
    await this.userRepository.storeRefreshToken(user.id, refreshToken);
    
    return {
      accessToken,
      refreshToken,
      expiresIn: 3600, // 1 hour
    };
  }

  // DRY Principle: Reusable validation methods
  private validateEmail(email: string): void {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      throw new ValidationError('Invalid email format');
    }
  }

  private validatePassword(password: string): void {
    if (password.length < 8) {
      throw new ValidationError('Password must be at least 8 characters');
    }
    if (!/[A-Z]/.test(password)) {
      throw new ValidationError('Password must contain uppercase letter');
    }
    if (!/[0-9]/.test(password)) {
      throw new ValidationError('Password must contain number');
    }
    if (!/[!@#$%^&*]/.test(password)) {
      throw new ValidationError('Password must contain special character');
    }
  }
}
```

---

### 2.2 Database Schema Design

**Entity-Relationship Diagram:**
```mermaid
erDiagram
    USERS ||--o{ POSTS : creates
    USERS ||--o{ COMMENTS : writes
    POSTS ||--o{ COMMENTS : has
    USERS ||--o{ SESSIONS : has
    
    USERS {
        uuid id PK
        string email UK
        string password_hash
        jsonb profile
        timestamp created_at
        timestamp updated_at
    }
    
    POSTS {
        uuid id PK
        uuid user_id FK
        string title
        text content
        string status
        timestamp published_at
        timestamp created_at
        timestamp updated_at
    }
    
    COMMENTS {
        uuid id PK
        uuid post_id FK
        uuid user_id FK
        text content
        timestamp created_at
    }
    
    SESSIONS {
        uuid id PK
        uuid user_id FK
        string refresh_token
        timestamp expires_at
        timestamp created_at
    }
```

**Schema Definition:**
```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at DESC);

-- Posts table
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(500) NOT NULL,
    content TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
    published_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_status_published ON posts(status, published_at DESC) WHERE status = 'published';
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);

-- Comments table
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_comments_post_id ON comments(post_id, created_at DESC);
CREATE INDEX idx_comments_user_id ON comments(user_id);

-- Sessions table
CREATE TABLE sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    refresh_token VARCHAR(500) UNIQUE NOT NULL,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_sessions_refresh_token ON sessions(refresh_token);
CREATE INDEX idx_sessions_expires_at ON sessions(expires_at);

-- Trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER posts_updated_at BEFORE UPDATE ON posts
    FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

**Migration Strategy:**
```sql
-- Migration: Add indexes for performance
-- Version: 2024_07_21_001_add_performance_indexes

BEGIN;

-- Add composite index for common query pattern
CREATE INDEX CONCURRENTLY idx_posts_user_status_published 
    ON posts(user_id, status, published_at DESC)
    WHERE status = 'published';

-- Add partial index for active sessions
CREATE INDEX CONCURRENTLY idx_sessions_active
    ON sessions(user_id, expires_at)
    WHERE expires_at > NOW();

COMMIT;
```

---

### 2.3 API Design

**RESTful API Endpoints:**

```yaml
Authentication:
  POST /api/v1/auth/register:
    description: Register new user
    request:
      body:
        email: string (required)
        password: string (required)
        profile: object (optional)
    response:
      201: User created
      400: Validation error
      409: User already exists
    
  POST /api/v1/auth/login:
    description: Login user
    request:
      body:
        email: string (required)
        password: string (required)
    response:
      200: { accessToken, refreshToken, expiresIn }
      401: Invalid credentials
      
  POST /api/v1/auth/refresh:
    description: Refresh access token
    request:
      body:
        refreshToken: string (required)
    response:
      200: { accessToken, refreshToken, expiresIn }
      401: Invalid token

Posts:
  GET /api/v1/posts:
    description: List posts
    query:
      page: number (default: 1)
      limit: number (default: 20, max: 100)
      status: string (optional)
      userId: uuid (optional)
    response:
      200: { data: Post[], pagination: { total, page, limit } }
      
  GET /api/v1/posts/:id:
    description: Get post by ID
    response:
      200: Post
      404: Post not found
      
  POST /api/v1/posts:
    description: Create post
    auth: required
    request:
      body:
        title: string (required)
        content: string (required)
        status: string (optional)
    response:
      201: Post created
      400: Validation error
      401: Unauthorized
      
  PATCH /api/v1/posts/:id:
    description: Update post
    auth: required
    request:
      body:
        title: string (optional)
        content: string (optional)
        status: string (optional)
    response:
      200: Post updated
      403: Forbidden (not owner)
      404: Post not found
      
  DELETE /api/v1/posts/:id:
    description: Delete post
    auth: required
    response:
      204: Post deleted
      403: Forbidden (not owner)
      404: Post not found
```

**API Implementation (Express + TypeScript):**

```typescript
// SOLID: Single Responsibility - Each controller handles one resource
class PostController {
  constructor(private readonly postService: PostService) {}

  // GET /api/v1/posts
  listPosts = async (req: Request, res: Response): Promise<void> => {
    const { page = 1, limit = 20, status, userId } = req.query;
    
    // Validate and sanitize input
    const validatedParams = ListPostsSchema.parse({
      page: Number(page),
      limit: Math.min(Number(limit), 100), // Max 100 items
      status,
      userId,
    });
    
    const result = await this.postService.list(validatedParams);
    
    res.json({
      data: result.posts,
      pagination: {
        total: result.total,
        page: validatedParams.page,
        limit: validatedParams.limit,
        pages: Math.ceil(result.total / validatedParams.limit),
      },
    });
  };

  // POST /api/v1/posts
  createPost = async (req: AuthRequest, res: Response): Promise<void> => {
    // Validate input
    const validatedData = CreatePostSchema.parse(req.body);
    
    // Create post
    const post = await this.postService.create({
      ...validatedData,
      userId: req.user.id, // From auth middleware
    });
    
    res.status(201).json(post);
  };

  // Error handling with proper HTTP codes
  handleError = (error: Error, res: Response): void => {
    if (error instanceof ValidationError) {
      res.status(400).json({ error: error.message });
    } else if (error instanceof UnauthorizedError) {
      res.status(401).json({ error: error.message });
    } else if (error instanceof ForbiddenError) {
      res.status(403).json({ error: error.message });
    } else if (error instanceof NotFoundError) {
      res.status(404).json({ error: error.message });
    } else {
      logger.error('Unhandled error', { error });
      res.status(500).json({ error: 'Internal server error' });
    }
  };
}

// Router configuration
const router = express.Router();

router.get('/posts', asyncHandler(postController.listPosts));
router.get('/posts/:id', asyncHandler(postController.getPost));
router.post('/posts', authenticateJWT, asyncHandler(postController.createPost));
router.patch('/posts/:id', authenticateJWT, asyncHandler(postController.updatePost));
router.delete('/posts/:id', authenticateJWT, asyncHandler(postController.deletePost));
```

---

### 2.4 State Management (Frontend)

**For React Applications:**

```typescript
// Using Zustand with TypeScript
// SOLID: Interface Segregation - Small, focused stores

interface User {
  id: string;
  email: string;
  profile: UserProfile;
}

interface AuthState {
  user: User | null;
  accessToken: string | null;
  isAuthenticated: boolean;
  
  // Actions
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  refreshToken: () => Promise<void>;
  setUser: (user: User) => void;
}

// DRY: Reusable auth store
const useAuthStore = create<AuthState>((set, get) => ({
  user: null,
  accessToken: null,
  isAuthenticated: false,
  
  login: async (email, password) => {
    const response = await authApi.login(email, password);
    set({
      user: response.user,
      accessToken: response.accessToken,
      isAuthenticated: true,
    });
    localStorage.setItem('refreshToken', response.refreshToken);
  },
  
  logout: () => {
    set({ user: null, accessToken: null, isAuthenticated: false });
    localStorage.removeItem('refreshToken');
  },
  
  refreshToken: async () => {
    const refreshToken = localStorage.getItem('refreshToken');
    if (!refreshToken) throw new Error('No refresh token');
    
    const response = await authApi.refresh(refreshToken);
    set({
      accessToken: response.accessToken,
    });
  },
  
  setUser: (user) => set({ user }),
}));

// Usage in component
function Profile() {
  const { user, logout } = useAuthStore();
  
  return (
    <div>
      <h1>{user?.profile.name}</h1>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

---

### 2.5 Class Diagrams

**OOP Design:**

```mermaid
classDiagram
    class AuthService {
        <<interface>>
        +register(email, password, profile) User
        +login(email, password) AuthToken
        +validateToken(token) TokenPayload
        +refreshToken(refreshToken) AuthToken
    }
    
    class AuthServiceImpl {
        -userRepository: UserRepository
        -tokenService: TokenService
        -passwordHasher: PasswordHasher
        +register(email, password, profile) User
        +login(email, password) AuthToken
        +validateToken(token) TokenPayload
        +refreshToken(refreshToken) AuthToken
        -validateEmail(email) void
        -validatePassword(password) void
    }
    
    class UserRepository {
        <<interface>>
        +create(data) User
        +findByEmail(email) User
        +findById(id) User
        +update(id, data) User
        +delete(id) void
    }
    
    class TokenService {
        <<interface>>
        +generateAccessToken(payload) string
        +generateRefreshToken(payload) string
        +verifyToken(token) TokenPayload
    }
    
    class PasswordHasher {
        <<interface>>
        +hash(password) string
        +verify(password, hash) boolean
    }
    
    AuthService <|.. AuthServiceImpl : implements
    AuthServiceImpl --> UserRepository : uses
    AuthServiceImpl --> TokenService : uses
    AuthServiceImpl --> PasswordHasher : uses
```

---

## 3️⃣ THREAT MODEL & SECURITY

### 3.1 Threat Modeling (STRIDE)

| Threat | Description | Mitigation |
|--------|-------------|------------|
| **Spoofing** | Attacker impersonates user | - Strong authentication (JWT)<br>- Password complexity requirements<br>- Rate limiting on login |
| **Tampering** | Attacker modifies data | - Input validation<br>- Parameterized queries<br>- HTTPS only |
| **Repudiation** | User denies action | - Audit logs<br>- Signed JWT tokens<br>- Database triggers for changes |
| **Information Disclosure** | Sensitive data leaked | - Encryption at rest (AES-256)<br>- Encryption in transit (TLS 1.3)<br>- No sensitive data in logs |
| **Denial of Service** | Service unavailable | - Rate limiting (100 req/min per IP)<br>- DDoS protection (CloudFlare)<br>- Auto-scaling |
| **Elevation of Privilege** | Attacker gains admin access | - RBAC (Role-Based Access Control)<br>- Principle of least privilege<br>- Regular security audits |

---

### 3.2 Security Controls

**Authentication & Authorization:**
```typescript
// SOLID: Dependency Inversion - Depend on abstractions
interface AuthorizationService {
  canAccess(user: User, resource: Resource, action: Action): boolean;
}

// RBAC Implementation
class RBACService implements AuthorizationService {
  canAccess(user: User, resource: Resource, action: Action): boolean {
    // Check if user has required role
    const requiredRole = this.getRequiredRole(resource, action);
    return user.roles.some(role => this.hasPermission(role, requiredRole));
  }
  
  private hasPermission(userRole: string, requiredRole: string): boolean {
    // Role hierarchy: admin > moderator > user
    const hierarchy = ['user', 'moderator', 'admin'];
    const userLevel = hierarchy.indexOf(userRole);
    const requiredLevel = hierarchy.indexOf(requiredRole);
    return userLevel >= requiredLevel;
  }
}

// Middleware for authorization
function authorize(action: Action) {
  return async (req: AuthRequest, res: Response, next: NextFunction) => {
    const resource = await getResource(req.params.id);
    
    if (!authService.canAccess(req.user, resource, action)) {
      throw new ForbiddenError('Insufficient permissions');
    }
    
    next();
  };
}

// Usage
router.delete('/posts/:id', 
  authenticateJWT, 
  authorize('delete'), 
  postController.deletePost
);
```

**Input Validation:**
```typescript
// Using Zod for runtime validation
import { z } from 'zod';

const CreatePostSchema = z.object({
  title: z.string()
    .min(1, 'Title required')
    .max(500, 'Title too long')
    .trim(),
  content: z.string()
    .min(10, 'Content too short')
    .max(50000, 'Content too long')
    .trim(),
  status: z.enum(['draft', 'published', 'archived'])
    .optional()
    .default('draft'),
});

// SQL Injection Prevention (Parameterized Queries)
async function findPostById(id: string): Promise<Post> {
  // NEVER do this: `SELECT * FROM posts WHERE id = '${id}'`
  // ALWAYS use parameterized queries:
  const result = await db.query(
    'SELECT * FROM posts WHERE id = $1',
    [id] // Parameters are properly escaped
  );
  return result.rows[0];
}

// XSS Prevention
function sanitizeHtml(html: string): string {
  // Use DOMPurify or similar library
  return DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p', 'br'],
    ALLOWED_ATTR: [],
  });
}
```

**Rate Limiting:**
```typescript
import rateLimit from 'express-rate-limit';

// Global rate limit
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 1000, // 1000 requests per window
  message: 'Too many requests, please try again later',
});

// Auth endpoint rate limit (stricter)
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 10, // 10 login attempts per 15 minutes
  skipSuccessfulRequests: true,
});

app.use('/api', globalLimiter);
app.use('/api/auth/login', authLimiter);
```

---

### 3.3 Data Protection

**Encryption:**
```typescript
// Encryption at rest (for sensitive fields)
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto';

class EncryptionService {
  private readonly algorithm = 'aes-256-gcm';
  private readonly key: Buffer;

  constructor(key: string) {
    this.key = Buffer.from(key, 'hex'); // 32 bytes for AES-256
  }

  encrypt(plaintext: string): string {
    const iv = randomBytes(16);
    const cipher = createCipheriv(this.algorithm, this.key, iv);
    
    let encrypted = cipher.update(plaintext, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    
    const authTag = cipher.getAuthTag();
    
    // Return: iv + authTag + encrypted
    return iv.toString('hex') + authTag.toString('hex') + encrypted;
  }

  decrypt(ciphertext: string): string {
    const iv = Buffer.from(ciphertext.slice(0, 32), 'hex');
    const authTag = Buffer.from(ciphertext.slice(32, 64), 'hex');
    const encrypted = ciphertext.slice(64);
    
    const decipher = createDecipheriv(this.algorithm, this.key, iv);
    decipher.setAuthTag(authTag);
    
    let decrypted = decipher.update(encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');
    
    return decrypted;
  }
}

// Usage for PII
const ssn = encryptionService.encrypt(user.ssn);
await db.query('UPDATE users SET ssn_encrypted = $1 WHERE id = $2', [ssn, user.id]);
```

---

## 4️⃣ CODE QUALITY STANDARDS

### 4.1 SOLID Principles Checklist

**Single Responsibility Principle (SRP):**
- [ ] Each class has ONE reason to change
- [ ] Each function does ONE thing
- [ ] No "God classes" with multiple responsibilities

Example:
```typescript
// ❌ BAD: Multiple responsibilities
class UserManager {
  createUser() { /* ... */ }
  sendEmail() { /* ... */ }
  logActivity() { /* ... */ }
  validateInput() { /* ... */ }
}

// ✅ GOOD: Single responsibility per class
class UserService {
  createUser() { /* ... */ }
}

class EmailService {
  sendEmail() { /* ... */ }
}

class Logger {
  logActivity() { /* ... */ }
}

class Validator {
  validateInput() { /* ... */ }
}
```

**Open/Closed Principle (OCP):**
- [ ] Open for extension, closed for modification
- [ ] Use interfaces and abstract classes
- [ ] Plugin architecture where applicable

Example:
```typescript
// ✅ GOOD: Extensible through interface
interface PaymentProcessor {
  process(amount: number): Promise<void>;
}

class StripeProcessor implements PaymentProcessor {
  async process(amount: number): Promise<void> {
    // Stripe-specific implementation
  }
}

class PayPalProcessor implements PaymentProcessor {
  async process(amount: number): Promise<void> {
    // PayPal-specific implementation
  }
}

// Can add new processors without modifying existing code
class CryptoProcessor implements PaymentProcessor {
  async process(amount: number): Promise<void> {
    // Crypto-specific implementation
  }
}
```

**Liskov Substitution Principle (LSP):**
- [ ] Subtypes must be substitutable for base types
- [ ] No surprising behavior changes
- [ ] Contracts must be honored

Example:
```typescript
// ✅ GOOD: Subtypes can replace base type
abstract class Shape {
  abstract area(): number;
}

class Rectangle extends Shape {
  constructor(private width: number, private height: number) {
    super();
  }
  
  area(): number {
    return this.width * this.height;
  }
}

class Circle extends Shape {
  constructor(private radius: number) {
    super();
  }
  
  area(): number {
    return Math.PI * this.radius ** 2;
  }
}

// Works with any Shape
function printArea(shape: Shape) {
  console.log(shape.area());
}
```

**Interface Segregation Principle (ISP):**
- [ ] Small, focused interfaces
- [ ] Clients shouldn't depend on unused methods
- [ ] Prefer composition over fat interfaces

Example:
```typescript
// ❌ BAD: Fat interface
interface Animal {
  walk(): void;
  fly(): void;
  swim(): void;
}

// ✅ GOOD: Segregated interfaces
interface Walkable {
  walk(): void;
}

interface Flyable {
  fly(): void;
}

interface Swimmable {
  swim(): void;
}

class Dog implements Walkable, Swimmable {
  walk() { /* ... */ }
  swim() { /* ... */ }
}

class Bird implements Walkable, Flyable {
  walk() { /* ... */ }
  fly() { /* ... */ }
}
```

**Dependency Inversion Principle (DIP):**
- [ ] Depend on abstractions, not concretions
- [ ] High-level modules don't depend on low-level modules
- [ ] Use dependency injection

Example:
```typescript
// ✅ GOOD: Depend on abstraction
interface Database {
  query(sql: string, params: any[]): Promise<any>;
}

class UserService {
  constructor(private readonly db: Database) {}
  
  async findUser(id: string): Promise<User> {
    return this.db.query('SELECT * FROM users WHERE id = $1', [id]);
  }
}

// Can inject different implementations
const postgresDB = new PostgresDatabase();
const mongoDBDB = new MongoDatabase();

const userService = new UserService(postgresDB);
```

---

### 4.2 DRY Principle (Don't Repeat Yourself)

**Checklist:**
- [ ] No duplicate code
- [ ] Extract common logic into functions/classes
- [ ] Use utility functions and helpers
- [ ] Configuration externalized

Example:
```typescript
// ❌ BAD: Repeated code
function createUser(data) {
  if (!data.email || !data.email.includes('@')) {
    throw new Error('Invalid email');
  }
  if (!data.password || data.password.length < 8) {
    throw new Error('Invalid password');
  }
  // ...
}

function updateUser(data) {
  if (!data.email || !data.email.includes('@')) {
    throw new Error('Invalid email');
  }
  if (!data.password || data.password.length < 8) {
    throw new Error('Invalid password');
  }
  // ...
}

// ✅ GOOD: DRY
class UserValidator {
  static validateEmail(email: string): void {
    if (!email || !email.includes('@')) {
      throw new ValidationError('Invalid email');
    }
  }
  
  static validatePassword(password: string): void {
    if (!password || password.length < 8) {
      throw new ValidationError('Password must be at least 8 characters');
    }
  }
}

function createUser(data) {
  UserValidator.validateEmail(data.email);
  UserValidator.validatePassword(data.password);
  // ...
}

function updateUser(data) {
  UserValidator.validateEmail(data.email);
  UserValidator.validatePassword(data.password);
  // ...
}
```

---

### 4.3 Performance Optimization

**Checklist:**
- [ ] Use appropriate data structures (O(1) lookup where needed)
- [ ] Implement caching for expensive operations
- [ ] Lazy loading for large datasets
- [ ] Database query optimization (indexes, joins)
- [ ] Async/await for I/O operations
- [ ] Connection pooling
- [ ] Compression for large responses

Example:
```typescript
// ✅ Performance optimized code

// 1. Caching
class PostService {
  private cache = new Map<string, Post>();
  
  async getPost(id: string): Promise<Post> {
    // Check cache first (O(1))
    if (this.cache.has(id)) {
      return this.cache.get(id)!;
    }
    
    // Fetch from DB
    const post = await this.postRepository.findById(id);
    
    // Store in cache
    this.cache.set(id, post);
    
    return post;
  }
}

// 2. Database query optimization
async function getPostsWithAuthors(): Promise<Post[]> {
  // ❌ BAD: N+1 query problem
  const posts = await db.query('SELECT * FROM posts');
  for (const post of posts) {
    post.author = await db.query('SELECT * FROM users WHERE id = $1', [post.user_id]);
  }
  
  // ✅ GOOD: Single query with JOIN
  return db.query(`
    SELECT 
      p.*,
      u.email as author_email,
      u.profile as author_profile
    FROM posts p
    INNER JOIN users u ON p.user_id = u.id
    WHERE p.status = 'published'
    ORDER BY p.published_at DESC
    LIMIT 20
  `);
}

// 3. Pagination for large datasets
async function listPosts(page: number, limit: number): Promise<Post[]> {
  const offset = (page - 1) * limit;
  return db.query(
    'SELECT * FROM posts ORDER BY created_at DESC LIMIT $1 OFFSET $2',
    [limit, offset]
  );
}

// 4. Async operations in parallel
async function getUserWithPostsAndComments(userId: string) {
  // ❌ BAD: Sequential (slow)
  const user = await userRepository.findById(userId);
  const posts = await postRepository.findByUserId(userId);
  const comments = await commentRepository.findByUserId(userId);
  
  // ✅ GOOD: Parallel (fast)
  const [user, posts, comments] = await Promise.all([
    userRepository.findById(userId),
    postRepository.findByUserId(userId),
    commentRepository.findByUserId(userId),
  ]);
  
  return { user, posts, comments };
}
```

---

### 4.4 Code Formatting & Linting

**Required Tools:**
- ESLint / Pylint / Clippy (language-specific)
- Prettier / Black / rustfmt (code formatting)
- TypeScript strict mode
- EditorConfig for consistency

**Configuration:**
```json
// .eslintrc.json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "prettier"
  ],
  "rules": {
    "no-console": "error",
    "no-debugger": "error",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "error",
    "max-lines": ["error", 300],
    "max-lines-per-function": ["error", 50],
    "complexity": ["error", 10]
  }
}
```

```json
// tsconfig.json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true
  }
}
```

---

## 5️⃣ TESTING STRATEGY

### 5.1 Test Coverage Requirements

**Targets:**
- Unit Tests: 80%+ coverage
- Integration Tests: Critical paths covered
- E2E Tests: User journeys covered
- Performance Tests: Load and stress testing

### 5.2 Test Pyramid

```
        /\
       /  \      E2E Tests (10%)
      /    \     - User flows
     /------\    - Browser tests
    /        \   
   /          \  Integration Tests (30%)
  /            \ - API tests
 /--------------\- Database tests
/                \
------------------
   Unit Tests (60%)
   - Pure functions
   - Business logic
```

### 5.3 Example Tests

```typescript
// Unit Test
describe('UserService', () => {
  let userService: UserService;
  let mockUserRepository: jest.Mocked<UserRepository>;
  
  beforeEach(() => {
    mockUserRepository = {
      create: jest.fn(),
      findByEmail: jest.fn(),
    } as any;
    
    userService = new UserService(mockUserRepository);
  });
  
  describe('register', () => {
    it('should create user with valid data', async () => {
      const userData = {
        email: 'test@example.com',
        password: 'SecurePass123!',
        profile: { name: 'Test User' },
      };
      
      mockUserRepository.findByEmail.mockResolvedValue(null);
      mockUserRepository.create.mockResolvedValue({ id: '123', ...userData });
      
      const result = await userService.register(
        userData.email,
        userData.password,
        userData.profile
      );
      
      expect(result.id).toBe('123');
      expect(result.email).toBe(userData.email);
      expect(mockUserRepository.create).toHaveBeenCalledTimes(1);
    });
    
    it('should throw error for duplicate email', async () => {
      mockUserRepository.findByEmail.mockResolvedValue({ id: '123' } as any);
      
      await expect(
        userService.register('existing@example.com', 'pass', {})
      ).rejects.toThrow(ConflictError);
    });
  });
});

// Integration Test
describe('POST /api/v1/auth/register', () => {
  it('should register user and return 201', async () => {
    const response = await request(app)
      .post('/api/v1/auth/register')
      .send({
        email: 'new@example.com',
        password: 'SecurePass123!',
        profile: { name: 'New User' },
      });
    
    expect(response.status).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe('new@example.com');
  });
});

// E2E Test (Playwright)
test('user can register and login', async ({ page }) => {
  await page.goto('http://localhost:3000/register');
  
  await page.fill('input[name="email"]', 'e2e@example.com');
  await page.fill('input[name="password"]', 'SecurePass123!');
  await page.click('button[type="submit"]');
  
  await expect(page).toHaveURL('http://localhost:3000/dashboard');
  await expect(page.locator('h1')).toContainText('Welcome');
});
```

---

## 6️⃣ FLOW DIAGRAMS

### 6.1 User Registration Flow

```mermaid
flowchart TD
    Start([User Visits Registration Page]) --> Input[User Enters Email & Password]
    Input --> Validate{Validation}
    Validate -->|Invalid| ShowError[Show Error Message]
    ShowError --> Input
    Validate -->|Valid| CheckExisting{User Exists?}
    CheckExisting -->|Yes| ShowConflict[Show 'Email Already Registered']
    ShowConflict --> Input
    CheckExisting -->|No| HashPassword[Hash Password]
    HashPassword --> CreateUser[Create User in DB]
    CreateUser --> GenerateToken[Generate JWT Tokens]
    GenerateToken --> SendEmail[Send Welcome Email]
    SendEmail --> Success[Return User + Tokens]
    Success --> End([Redirect to Dashboard])
```

### 6.2 Authentication Flow

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant AuthService
    participant Database
    participant TokenService
    
    Client->>API: POST /auth/login
    API->>AuthService: login(email, password)
    AuthService->>Database: findUserByEmail(email)
    Database-->>AuthService: User data
    AuthService->>AuthService: verifyPassword(password, hash)
    alt Password Valid
        AuthService->>TokenService: generateAccessToken(userId)
        TokenService-->>AuthService: accessToken
        AuthService->>TokenService: generateRefreshToken(userId)
        TokenService-->>AuthService: refreshToken
        AuthService->>Database: storeRefreshToken(userId, token)
        AuthService-->>API: { accessToken, refreshToken }
        API-->>Client: 200 OK + Tokens
    else Password Invalid
        AuthService-->>API: UnauthorizedError
        API-->>Client: 401 Unauthorized
    end
```

### 6.3 Request Lifecycle

```mermaid
flowchart LR
    Request[HTTP Request] --> RateLimiter{Rate Limit OK?}
    RateLimiter -->|No| Block[429 Too Many Requests]
    RateLimiter -->|Yes| Auth{Authenticated?}
    Auth -->|No| Unauthorized[401 Unauthorized]
    Auth -->|Yes| Validate{Valid Input?}
    Validate -->|No| BadRequest[400 Bad Request]
    Validate -->|Yes| Authorize{Authorized?}
    Authorize -->|No| Forbidden[403 Forbidden]
    Authorize -->|Yes| Business[Business Logic]
    Business --> Cache{In Cache?}
    Cache -->|Yes| Return[Return Cached Data]
    Cache -->|No| Database[Query Database]
    Database --> StoreCache[Store in Cache]
    StoreCache --> Return
    Return --> Response[200 OK Response]
```

---

**Continue to Part 2: Pre-commit Hooks, CI/CD Integration, and Agent Workflow Updates...**

---

**Version:** 1.0.0  
**Last Updated:** July 21, 2026  
**Owner:** Deepak Rao Gaikwad (@deepakraog)
