---
name: writing-containerfiles
description: Writing optimized, secure, multi-stage Containerfiles (Containerfile/Podman) with language-specific patterns (Python, Node.js, Go, Rust), BuildKit features, distroless images, and explicit registry references. Use when containerizing applications, optimizing existing Containerfiles, or reducing image sizes.
---

# Writing Containerfiles

Create production-grade Containerfiles with multi-stage builds, security hardening, language-specific optimizations, and explicit registry references.

## When to Use This Skill

Invoke when:
- "Write a Containerfile for [Python/Node.js/Go/Rust] application"
- "Optimize this Containerfile to reduce image size"
- "Use multi-stage build for..."
- "Secure Containerfile with non-root user"
- "Use distroless base image"
- "Add BuildKit cache mounts"
- "Prevent secrets from leaking in Docker layers"

## Quick Decision Framework

Ask three questions to determine the approach:

**1. What language?**
- Python → See `references/python-dockerfiles.md`
- Node.js → See `references/nodejs-dockerfiles.md`
- Go → See `references/go-dockerfiles.md`
- Rust → See `references/rust-dockerfiles.md`
- Java → See `references/java-dockerfiles.md`

**2. Is security critical?**
- YES → Use distroless runtime images (see `references/security-hardening.md`)
- NO → Use slim/alpine base images

**3. Is image size critical?**
- YES (<50MB) → Multi-stage + distroless + static linking
- NO (<500MB) → Multi-stage + slim base images

## Core Concepts

### Multi-Stage Builds

Separate build environment from runtime environment to minimize final image size.

**Pattern:**
```dockerfile
# Stage 1: Build
FROM build-image AS builder
RUN compile application

# Stage 2: Runtime
FROM minimal-runtime-image
COPY --from=builder /app/binary /app/
CMD ["/app/binary"]
```

**Benefits:**
- 80-95% smaller images (excludes build tools)
- Improved security (no compilers in production)
- Faster deployments
- Better layer caching

### Registry Best Practices

**Always specify full registry path:**

```dockerfile
# ❌ Wrong
FROM redis:7-alpine
FROM python:3.12-slim

# ✅ Correct
FROM docker.io/library/redis:7-alpine
FROM docker.io/library/python:3.12-slim
```

**Common registries:**
- `docker.io` — Docker Hub
- `ghcr.io` — GitHub Container Registry
- `lscr.io` — LinuxServer.io
- `gcr.io` — Google (distroless)
- `quay.io` — Red Hat Quay
- `registry.access.redhat.com` — Red Hat UBI

### Base Image Selection

**Decision matrix:**

| Language | Build Stage | Runtime Stage | Final Size |
|----------|-------------|---------------|------------|
| Go (static) | `docker.io/library/golang:1.22-alpine` | `gcr.io/distroless/static-debian12` | 10-30MB |
| Rust (static) | `docker.io/library/rust:1.75-alpine` | `scratch` | 5-15MB |
| Python | `docker.io/library/python:3.12-slim` | `docker.io/library/python:3.12-slim` | 200-400MB |
| Node.js | `docker.io/library/node:20-alpine` | `docker.io/library/node:20-alpine` | 150-300MB |
| Java | `docker.io/library/maven:3.9-eclipse-temurin-21` | `docker.io/library/eclipse-temurin:21-jre-alpine` | 200-350MB |

**Distroless images** (Google-maintained):
- `gcr.io/distroless/static-debian12` → Static binaries (2MB)
- `gcr.io/distroless/base-debian12` → Dynamic binaries with libc (20MB)
- `gcr.io/distroless/python3-debian12` → Python runtime (60MB)
- `gcr.io/distroless/nodejs20-debian12` → Node.js runtime (150MB)

See `references/base-image-selection.md` for complete comparison.

### BuildKit Features

Enable BuildKit for advanced caching and security:

```bash
export DOCKER_BUILDKIT=1
docker build .
# OR
docker buildx build .
```

**Key features:**
- `--mount=type=cache` → Persistent package manager caches
- `--mount=type=secret` → Inject secrets without storing in layers
- `--mount=type=ssh` → SSH agent forwarding for private repos
- Parallel stage execution
- Improved layer caching

See `references/buildkit-features.md` for detailed patterns.

### Layer Optimization

Order Containerfile instructions from least to most frequently changing:

```dockerfile
# 1. Base image (rarely changes)
FROM python:3.12-slim

# 2. System packages (rarely changes)
RUN apt-get update && apt-get install -y build-essential

# 3. Dependencies manifest (changes occasionally)
COPY requirements.txt .
RUN pip install -r requirements.txt

# 4. Application code (changes frequently)
COPY . .

# 5. Runtime configuration (rarely changes)
CMD ["python", "app.py"]
```

**BuildKit cache mounts:**
```dockerfile
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt
```

Cache persists across builds, eliminating redundant downloads.

### Security Hardening

**Essential security practices:**

**1. Non-root users**
```dockerfile
# Debian/Ubuntu
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Alpine
RUN adduser -D -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Distroless (built-in)
USER nonroot:nonroot
```

**2. Secret management**
```dockerfile
# ❌ NEVER: Secret in layer history
RUN git clone https://${GITHUB_TOKEN}@github.com/private/repo.git

# ✅ ALWAYS: BuildKit secret mount
RUN --mount=type=secret,id=github_token \
    TOKEN=$(cat /run/secrets/github_token) && \
    git clone https://${TOKEN}@github.com/private/repo.git
```

Build with:
```bash
docker buildx build --secret id=github_token,src=./token.txt .
```

**3. Vulnerability scanning**
```bash
# Trivy (recommended)
trivy image myimage:latest

# Docker Scout
docker scout cves myimage:latest
```

**4. Health checks**
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/health || exit 1
```

See `references/security-hardening.md` for comprehensive hardening patterns.

### .containerignore Configuration

Create `.containerignore` to exclude unnecessary files:

```
# Version control
.git
.gitignore

# CI/CD
.github
.gitlab-ci.yml

# IDE
.vscode
.idea

# Testing
tests/
coverage/
**/*_test.go
**/*.test.js

# Build artifacts
node_modules/
dist/
build/
target/
__pycache__/

# Environment
.env
.env.local
*.log
```

Reduces build context size and prevents leaking secrets.

## Language-Specific Patterns

### Python Quick Reference

**Three approaches:**

1. **pip (simple)** → Single-stage, requirements.txt
2. **poetry (production)** → Multi-stage, virtual environment
3. **uv (fastest)** → 10-100x faster than pip

**Example: Poetry multi-stage**
```dockerfile
FROM docker.io/library/python:3.12-slim AS builder
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install poetry==1.7.1

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt --output requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    python -m venv /opt/venv && \
    /opt/venv/bin/pip install -r requirements.txt

FROM docker.io/library/python:3.12-slim
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
USER 1000:1000
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
```

See `references/python-dockerfiles.md` for complete patterns and `examples/python-fastapi.Containerfile`.

### Node.js Quick Reference

**Key patterns:**

- Use `npm ci` (not `npm install`) for reproducible builds
- Multi-stage: Build stage → Production dependencies only
- Built-in `node` user (UID 1000)
- Alpine variant smallest (~180MB vs 1GB)

**Example: Express multi-stage**
```dockerfile
FROM docker.io/library/node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN --mount=type=cache,target=/root/.npm \
    npm ci
COPY . .
RUN npm run build
RUN npm prune --omit=dev

FROM docker.io/library/node:20-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
USER node
CMD ["node", "dist/index.js"]
```

See `references/nodejs-dockerfiles.md` for npm/pnpm/yarn patterns and `examples/nodejs-express.Containerfile`.

### Go Quick Reference

**Smallest possible images:**

- Static binary (CGO_ENABLED=0) + distroless = 10-30MB
- Strip symbols with `-ldflags="-s -w"`
- Cache both `/go/pkg/mod` and build cache

**Example: Distroless static**
```dockerfile
FROM docker.io/library/golang:1.22-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download

COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o main .

FROM gcr.io/distroless/static-debian12
COPY --from=builder /app/main /app/main
USER nonroot:nonroot
ENTRYPOINT ["/app/main"]
```

See `references/go-dockerfiles.md` and `examples/go-microservice.Containerfile`.

### Rust Quick Reference

**Ultra-small static binaries:**

- musl static linking → No libc dependencies
- scratch base image (0 bytes overhead)
- Final image: 5-15MB

**Example: Scratch base**
```dockerfile
FROM docker.io/library/rust:1.75-alpine AS builder
RUN apk add --no-cache musl-dev
WORKDIR /app

# Cache dependencies
COPY Cargo.toml Cargo.lock ./
RUN --mount=type=cache,target=/usr/local/cargo/registry \
    mkdir src && echo "fn main() {}" > src/main.rs && \
    cargo build --release --target x86_64-unknown-linux-musl && \
    rm -rf src

# Build application
COPY src ./src
RUN --mount=type=cache,target=/usr/local/cargo/registry \
    cargo build --release --target x86_64-unknown-linux-musl

FROM scratch
COPY --from=builder /app/target/x86_64-unknown-linux-musl/release/app /app
USER 1000:1000
ENTRYPOINT ["/app"]
```

See `references/rust-dockerfiles.md` and `examples/rust-actix.Containerfile`.

## Package Manager Cache Mounts

**BuildKit cache mount locations:**

| Language | Package Manager | Cache Mount Target |
|----------|----------------|-------------------|
| Python | pip | `--mount=type=cache,target=/root/.cache/pip` |
| Python | poetry | `--mount=type=cache,target=/root/.cache/pypoetry` |
| Python | uv | `--mount=type=cache,target=/root/.cache/uv` |
| Node.js | npm | `--mount=type=cache,target=/root/.npm` |
| Node.js | pnpm | `--mount=type=cache,target=/root/.local/share/pnpm/store` |
| Go | go mod | `--mount=type=cache,target=/go/pkg/mod` |
| Rust | cargo | `--mount=type=cache,target=/usr/local/cargo/registry` |

Persistent caches eliminate redundant package downloads across builds.

## Validation and Testing

**Validate Containerfile quality:**
```bash
# Lint Containerfile
python <skill-dir>/scripts/validate_dockerfile.py Containerfile

# Scan for vulnerabilities
trivy image myimage:latest

# Analyze image size
docker images myimage:latest
docker history myimage:latest
```

**Compare optimization results:**
```bash
# Before optimization
docker build -t myapp:before .

# After optimization
docker build -t myapp:after .

# Compare
bash <skill-dir>/scripts/analyze_image_size.sh myapp:before myapp:after
```

See `<skill-dir>/scripts/validate_dockerfile.py` for automated Containerfile linting.

## Integration with Related Skills

**Upstream (provide input):**
- `testing-strategies` → Test application before containerizing
- `security-hardening` → Application-level security before Docker layer

**Downstream (consume Containerfiles):**
- `building-ci-pipelines` → Build and push Docker images in CI
- `kubernetes-operations` → Deploy containers to K8s clusters
- `infrastructure-as-code` → Deploy containers with Terraform/Pulumi

**Parallel (related context):**
- `secret-management` → Inject runtime secrets (K8s secrets, vaults)
- `observability` → Container logging and metrics collection

## Common Patterns Quick Reference

**1. Static binary (Go/Rust) → Smallest image**
- Build: Language-specific builder image
- Runtime: `gcr.io/distroless/static-debian12` or `scratch`
- Size: 5-30MB

**2. Interpreted language (Python/Node.js) → Production-optimized**
- Build: Install dependencies, build artifacts
- Runtime: Same base, production dependencies only
- Size: 150-400MB

**3. JVM (Java) → Optimized runtime**
- Build: Maven/Gradle with full JDK
- Runtime: JRE-only image (alpine variant)
- Size: 200-350MB

**4. Security-critical → Maximum hardening**
- Base: Distroless images
- User: Non-root (nonroot:nonroot)
- Secrets: BuildKit secret mounts
- Scan: Trivy/Docker Scout in CI

**5. Development → Fast iteration**
- Base: Full language image (not slim)
- Volumes: Mount source code
- Hot reload: Language-specific tools
- Not covered in this skill (see Docker Compose docs)

## Anti-Patterns to Avoid

**❌ Never:**
- Use `latest` tags (unpredictable builds)
- Run as root in production
- Store secrets in ENV vars or layers
- Install unnecessary packages
- Combine unrelated RUN commands (breaks caching)
- Skip .containerignore (bloated build context)

**✅ Always:**
- Pin exact image versions with registry (`docker.io/library/python:3.12.1-slim`, not `python:3`)
- Create and use non-root user
- Use BuildKit secret mounts for credentials
- Minimize layers and image size
- Order commands from least to most frequently changing
- Create .containerignore file

## Additional Resources

**Base image registries:**
- Docker Hub: `docker.io/library/*`
- Google Distroless: `gcr.io/distroless/*`
- Red Hat UBI: `registry.access.redhat.com/ubi9/*`
- LinuxServer.io: `lscr.io/linuxserver/*`

**Vulnerability scanners:**
- Trivy (recommended): `trivy image myimage:latest`
- Docker Scout: `docker scout cves myimage:latest`
- Grype: `grype myimage:latest`

**Reference documentation:**
- `references/base-image-selection.md` → Complete base image comparison
- `references/buildkit-features.md` → Advanced BuildKit patterns
- `references/security-hardening.md` → Comprehensive security guide
- Language-specific references in `references/` directory
- Working examples in `examples/` directory
