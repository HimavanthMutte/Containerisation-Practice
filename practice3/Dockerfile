# STAGE1: Building
FROM node:24.18-alpine3.24 AS builder

WORKDIR /app

COPY package* .

RUN npm install

COPY . . 

RUN npm run build

# STAGE2: Running

FROM nginx:alpine-slim

COPY --from=builder app/dist /usr/share/nginx/html

EXPOSE 80 

CMD ["nginx", "-g", "daemon off;"]