# elan-parser
ELANファイルの解析を行う

**pympi_elan_parser.py**  
Pympi(https://github.com/dopefishh/pympi  )を使用して解析を行う。  
`pip install pympi-ling`で導入可能。  
corpus_root以下のELANファイルを読み込み、発話開始時間・発話終了時間・発話内容を取得する。  
output_rootに取得した内容をcsv形式で書き込みを行う。  

**elan_parser.py**  
標準ライブラリのElementTreeを使用して解析を行う。  
現状ディレクトリ以下すべてのファイルの発話内容の標準出力のみ可能。  