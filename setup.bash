#!/bin/bash

# 仮想環境作成
python3 -m venv venv

# 仮想環境起動
. ./venv/bin/activate

# 仮想環境にライブラリをインストール
pip install -r requirements.txt

# マイグレーション
python3 ./manage.py migrate

# サンプルデータのロード
python3 manage.py loaddata sample_data.json

# サーバー起動
python3 manage.py runserver
