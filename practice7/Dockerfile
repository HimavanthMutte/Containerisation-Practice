FROM node:24.18-alpine3.24 AS builder

WORKDIR /app

COPY package* .

RUN npm ci 

COPY . .

RUN npm run build 

FROM nginx:alpine-slim

COPY --from=builder /app/dist /usr/share/nginx/html

CMD ["nginx","-g","daemon off;"]