import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.user import Base,User


def web_scraping():
    '''
    簡単なWebスクレイピング
        requests と BeautifulSoup を使って、あるWebページのタイトルを取得するスクリプトを作る。
    '''
    #パナソニック株式会社
    url = 'https://panasonic.jp/'
    # ウェブページのHTMLを取得
    response = requests.get(url, timeout=10)
    if response.status_code != 200:
        print(f"エラー：ステータスコード{response.status_code}")
        return

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, "html.parser")

    # タイトルを取得
    title = getattr(soup.title,"text","NoTitle")
    print(title)

def database_control():
    '''
    簡単なDB操作
        users テーブル（id, name, age）を作成し、適当なデータを挿入後、全件取得するスクリプトを書く。
    '''
    # 環境変数からユーザー名とパスワードを取得
    user_name = os.getenv('POSTGRES_USERNAME')
    password = os.getenv('POSTGRES_PASSWORD')
    engine = create_engine(f"postgresql+psycopg2://{user_name}:{password}@localhost/test_database")
    session_local = sessionmaker(bind=engine)

    #テーブルの作成
    Base.metadata.create_all(bind=engine)
    with session_local() as session:
        #レコードを追加
        new_record = User(id=1,name="test",age=20)
        session.add(new_record)
        #追加されたレコードを取得
        record = session.query(User).all()
        for x in record:
            print(f"id:{x.id} name:{x.name} age:{x.age}")
    #ロールバックされたことを確認
    with session_local() as session:
        record = session.query(User).all()
        print(record)



web_scraping()
database_control()