# elan-parser
ELANファイルの解析を行う

**pympi_elan_parser.py**  
Pympi(https://github.com/dopefishh/pympi  )を使用して解析を行う。通常これを使用する。  
Pympiは`pip install pympi-ling`で導入可能。  
corpus_root以下のELANファイルを読み込み、発話開始時間・発話終了時間・発話内容を取得する。  
output_rootに取得した内容をcsv形式で書き込みを行う。  

**pympi_elan_unit_parser.py**  
pympi_elan_parser.pyの単独ファイル用。

**elan_parser.py**  
標準ライブラリのElementTreeを使用して解析を行う。  
現状ディレクトリ以下すべてのファイルの発話内容の標準出力のみ可能。  

**sort.py**  
pympi_elan_parser.pyで解析するとELAN形式通り話者ごとに出力されるため、  
時系列順に変換したい場合に使用する。  
