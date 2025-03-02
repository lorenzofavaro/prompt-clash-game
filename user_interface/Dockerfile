# Build stage
FROM node:22.13.1-slim AS builder

# Install pnpm
RUN npm install -g pnpm@latest

# Set working directory
WORKDIR /app

# Copy the entire project
COPY . .

# Install dependencies
RUN pnpm install

# Build the application
RUN pnpm buildUi

# Production stage
FROM nginx:alpine

# Copy the built files from builder stage to nginx
COPY --from=builder /app/app/dist /usr/share/nginx/html

# Copy custom nginx configuration if needed
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 3000

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
