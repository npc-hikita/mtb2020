#!bin/bash

# バックエンド（Python）の依存ライブラリをインストール
cd ./backend
pip3 install --user -r requirements.txt

# フロントエンド（React）の依存ライブラリをインストール
cd ../frontend
yarn install
