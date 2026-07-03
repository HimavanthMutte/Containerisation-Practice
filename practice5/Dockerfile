FROM node:24.18-alpine3.24

WORKDIR /app

COPY package* .

RUN npm install 

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["node","./dist/index.js"]