###########################
# 本番環境用Dockerコンテナ #
###########################

# ベースとなるコンテナイメージを指定（今回はPython 3.9）
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

# 以下、ベースイメージに対して行う追加の作業を記述

# コンテナ内の作業ディレクトリを指定
WORKDIR /mtb2020

# ソースをコンテナにコピー
COPY . .

# ★フロントエンドのセットアップ
WORKDIR /mtb2020/frontend
# Node.jsをインストール
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh && sudo bash nodesource_setup.sh && sudo apt install nodejs
# Node.jsの依存ライブラリをインストール
RUN yarn install
# 本番環境用のReactアプリを生成（ビルド）
RUN yarn build
# バックエンド側にフロントエンドのアプリをコピー
RUN mv build/* ../backend/static/

# ★バックエンドのセットアップ
WORKDIR /mtb2020/backend
# Pythonの依存ライブラリをインストール
RUN pip3 install -r requirements.txt

# コンテナ起動時に実行するコマンドを指定
CMD [ "python", "main.py" ]