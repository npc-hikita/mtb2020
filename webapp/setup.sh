#!bin/bash

cd ./webapp

# Pythonの依存ライブラリをインストール
pip3 install --user -r requirements.txt

# フロントエンドの依存ライブラリをインストール
cd frontend
yarn install
