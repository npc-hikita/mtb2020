# ベースとなるコンテナイメージを指定（今回はPython 3.9）
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.9

# 以下、ベースイメージに対して行う追加の作業を記述

# Node.jsをインストール
su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install lts/* 2>&1"
