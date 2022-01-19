# Climate 中文啟動指南

> **Climate 無法相容於 Windows 平台，如需在該平台上運行，務必請使用 Docker，或轉為使用 GNU/Linux 系統（推薦 Debian >= 10）來運行**

本文件將教學，如何利用 Docker Compose 啟動 Climate 系統。

## 系統

推薦 GNU/Linux 作業系統作為主體系統環境，以 Debian 發行版最為推薦。

執行平台需搭載 Docker 18.09 以上，具備 Docker-Compose 以進行部署。

## 設定

**注意：以下檔案需儲存在同一個目錄下**

請將以下文字存為 `config.yaml`

```yaml
database:
    dsn: mongodb://root:default@mongo:27017/
    name: climate
```

請將以下文字存為 `docker-compose.yml`

```yaml
version: "2.2"

services:
  climate:
    image: poyang31/climate
    restart: always
    ports:
      - 127.0.0.1:7351:7351
    volumes:
      - ./config.yaml:/app/config.yaml
    depends_on:
      - mongo
    networks:
      - climate

  mongo:
    image: mongo
    restart: always
    volumes:
      - database:/data
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: default
    networks:
      - climate

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 127.0.0.1:8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: default
      ME_CONFIG_MONGODB_URL: mongodb://root:default@mongo:27017/
    networks:
      - climate

volumes:
  database:
    driver: local

networks:
  climate:
    driver: bridge
```

## 啟動

請在該目錄下，直接輸入指令

```shell
docker-compose up
```

Climate 系統即可啟動

## 介面

Climate 互動介面：
<http://127.0.0.1:7351>

MongoDB 管理介面：
<http://127.0.0.1:8081>
