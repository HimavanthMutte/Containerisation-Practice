FROM node:24.18-alpine3.24

WORKDIR /app

COPY package* .

RUN npm install

COPY . . 

EXPOSE 3000

CMD ["node","index.js"]