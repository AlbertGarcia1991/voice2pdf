FROM node:20-slim

WORKDIR /app

# Add npm configuration for better reliability
RUN npm config set fetch-retry-mintimeout 20000 \
    && npm config set fetch-retry-maxtimeout 120000

# Copy package files
COPY package*.json ./

# Install dependencies with specific flags
RUN npm install --legacy-peer-deps --no-audit --no-fund

# Copy the rest of the application
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"] 