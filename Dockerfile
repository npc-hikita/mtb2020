###########################
# 本番環境用Dockerコンテナ #
###########################

# ベースとなるコンテナイメージを指定（今回はPython 3.9）
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

WORKDIR /mtb
COPY . .

# フロントエンドのセットアップ
WORKDIR /mtb/frontend
RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install lts/* 2>&1"
RUN yarn install
RUN yarn build
RUN mv build/* ../backend/static/

# バックエンドのセットアップ
WORKDIR /mtb/backend
RUN pip3 install --user -r requirements.txt

# コンテナ起動時に実行するコマンドを指定
CMD [ "python", "main.py" ]