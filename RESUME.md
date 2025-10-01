## Deepak Gaikwad

Principal Engineer • Bengaluru, IN 560069  
Email: gaikwad.dcg@gmail.com • Phone: +91 96635 00154  
LinkedIn: https://www.linkedin.com/in/deepakraog • GitHub: https://github.com/deepakraog

### Professional Summary
Results-driven Principal Engineer with a focus on scalable backend architectures, serverless microservices, performance optimization, and cost efficiency. Extensive experience designing APIs, building NodeJS/TypeScript services, refining CI/CD with GitHub Actions, and partnering with frontend teams (React/Angular) to deliver fast, reliable user experiences.

### Selected Impact (2024–2025)
- **Backend caching with end‑to‑end observability**: Introduced layered caching (Redis/ElastiCache + HTTP cache headers) and request coalescing to prevent cache stampedes. Achieved ~85–92% cache hit rate, reduced p95 latency by 40–55%, cut database reads by ~60%, and lowered compute cost by ~25%. Instrumented with CloudWatch metrics, structured logs, and dashboards for hit/miss, TTL, and latency.
- **Image delivery via S3 + CDN with browser caching**: Moved media assets to Amazon S3 behind CloudFront, standardized object metadata (`Cache-Control`, `ETag`, `Last-Modified`, `immutable`) and enabled responsive formats (WebP/AVIF). Realized ~95–99% CDN hit ratio, p95 image TTFB down 35–50%, and origin egress reduced ~40–55%.
- **Idempotent billing APIs**: Implemented idempotency keys with durable request ledger and TTL to ensure once-and-only-once charging across retries and concurrent requests. Eliminated duplicate charges (0 incidents post‑launch) and reduced billing-related support tickets by ~70%.
- **React UX and static preloading**: Shipped route-based code splitting, `preload/prefetch` of critical routes, `preconnect/dns-prefetch`, and service worker warmup of static content. Improved Core Web Vitals (LCP ↓ 25–35%, TTI ↓ 20–30%) and raised Lighthouse performance to 90–95+ across key flows.

### Experience

#### Principal Engineer — STEDI, Bengaluru, IN (2024‑02 → 2025‑05)
- Crafted cost‑effective microservices/serverless architectures on AWS using CDK.
- Designed APIs with Smithy; added SNIP/JSONata validations and contract testing.
- Integrated Claude 3.7 and ChatGPT for feature triage and bug resolution workflows.
- Established CI/CD with GitHub Actions (multi‑stage deploy, canaries, automated rollbacks).
- Engineered the initiatives in "Selected Impact" (caching, CDN/image headers, idempotent billing, React preloading) delivering measurable latency and cost improvements.
- Optimized data stores (PostgreSQL, DynamoDB), schema design, and query performance.

#### Senior Software Engineer II — CLEO, Bengaluru, IN (2017‑09 → 2024‑02)
- Spearheaded design and implementation of cloud‑native microservices at scale.
- Built and optimized RESTful APIs, improved observability and reliability SLOs.
- Mentored engineers through design reviews, code reviews, and sprint ceremonies.

### Skills
- **Languages**: TypeScript, JavaScript, Rust (utilities)
- **Backend**: NodeJS, Fastify/Express, REST, Smithy, API Gateway, Lambda
- **Frontend**: React, Angular, CSS; performance profiling and Core Web Vitals
- **Cloud & Data**: AWS (S3, CloudFront, Lambda, API Gateway, DynamoDB, RDS, CloudWatch, IAM)
- **DevOps**: GitHub Actions, CDK, Docker, IaC, canary deployments, feature flags
- **Observability**: CloudWatch, X‑Ray, Grafana/Prometheus, structured logging, tracing

### Links
- LinkedIn: https://www.linkedin.com/in/deepakraog
- GitHub: https://github.com/deepakraog
- Email: gaikwad.dcg@gmail.com

> Metrics reflect aggregated CloudWatch/CloudFront dashboards and vary by region/route; ranges are provided for clarity. Replace with your exact figures if needed.

