FROM gradle:jdk17-alpine

WORKDIR /app

COPY . .

RUN gradle build

RUN cp build/libs/*[^plain].jar app.jar

CMD ["java","-jar","app.jar"]