FROM node:9.0.0
MAINTAINER gaozhe.net

#ENV NODE_ENV=production
#ENV HOST 0.0.0.0

RUN mkdir -p /app
COPY . /app
WORKDIR /app

EXPOSE 3000

RUN npm config set registry https://registry.npm.taobao.org

RUN npm install

#RUN npm install pm2 --save-dev

RUN npm install sass-loader
RUN npm install node-sass

#RUN npm install sass-loader node-sass webpack --save-dev
#RUN npm install style-loader css-loader --save-dev

#RUN npm run dev
RUN nuxt build && npm start
#CMD ["npm", "pm2"]
