import pandas as pd
import pathlib
import os

def read_csv_pd():
    '''
    要件
    1.pandas を使用してCSVファイルを読み込む。
    2.age の平均値を求める
    3.score が 85 以上の人をフィルタリングして新しいCSVファイルに保存する
    4.score の平均値を求める
    5.結果を output.csv に保存する
    '''
    #pathの設定
    csv_path = os.path.join(pathlib.Path(__file__).parent,"plactice1.csv")
    output_path = os.path.join(pathlib.Path(__file__).parent,"output.csv")
    #csvファイルを読み込む
    df_csv = pd.read_csv(csv_path)
    # ageの平均値
    age_average = df_csv["age"].mean()
    # scoreの平均値
    score_average = df_csv["score"].mean()
    # 85点以上の人を抽出
    df_high_core = df_csv.loc[df_csv["score"] >= 85]
    #出力用データフレームを作成
    df_high_core["age_average"] = age_average
    df_high_core["score_average"] = score_average
    #csvファイルに出力
    df_high_core.to_csv(output_path,index=False)


if __name__ == "__main__":
    read_csv_pd()
