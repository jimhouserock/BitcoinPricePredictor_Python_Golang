# Production-Ready Bitcoin Price Predictor
# Multi-stage build for security and minimal image size

FROM golang:1.21-alpine AS builder

# Install git and ca-certificates for go modules and HTTPS
RUN apk add --no-cache git ca-certificates

WORKDIR /app

# Copy go mod files and initialize
COPY go-service/go.mod ./
RUN go mod init btc-api || true

# Copy Go source code
COPY go-service/main.go .
COPY go-service/static ./static

# Download dependencies and build with security flags
RUN go get github.com/gin-gonic/gin@v1.9.1
RUN go get github.com/gin-contrib/cors@v1.4.0
RUN go get github.com/gorilla/websocket@v1.5.0
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o main .

# Final lightweight runtime stage
FROM alpine:latest

# Install ca-certificates for HTTPS requests and curl for health checks
RUN apk --no-cache add ca-certificates curl

# Create non-root user for security
RUN addgroup -g 1001 -S appgroup && \
    adduser -S appuser -u 1001 -G appgroup

WORKDIR /app

# Copy binary and static files from builder
COPY --from=builder /app/main .
COPY --from=builder /app/static ./static

# Change ownership to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user for security
USER appuser

# Expose port 3000
EXPOSE 3000

# Health check for container orchestration
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

# Run the application
CMD ["./main"]
