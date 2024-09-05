# カレンダーイベント抽出ツール

このプロジェクトは、OpenAIのGPTモデルを使用して、自然言語テキストからカレンダーイベント情報を抽出し、Pydanticを使用して構造化された形式に解析します。

## プロジェクト概要

カレンダーイベント抽出ツールは、OpenAIのGPTモデルの能力を活用して、自然言語の説明から自動的にイベントの詳細を抽出するPythonベースのツールです。非構造化テキストを解析し、イベント名、日付、参加者を含むイベントに関する構造化データを返すように設計されています。

## 特徴

- 自然言語テキストからイベント情報を抽出
- 正確な情報抽出のためにOpenAIのGPT-3.5-turboモデルを使用
- 抽出された情報を構造化されたPydanticモデルに解析
- APIレスポンスとデータ解析の潜在的なエラーを処理

## 前提条件

- Python 3.7以上
- OpenAI APIキー

## インストール

1. リポジトリをクローンします：
   ```
   git clone https://github.com/yourusername/calendar-event-extractor.git
   cd calendar-event-extractor
   ```

2. 仮想環境を作成し、アクティベートします：
   ```
   python -m venv venv
   source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
   ```

3. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

4. プロジェクトのルートディレクトリに`.env`ファイルを作成し、OpenAI APIキーを追加します：
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 使用方法

1. 仮想環境がアクティブになっていることを確認します。

2. メインスクリプトを実行します：
   ```
   python src/main.py
   ```

3. スクリプトはデフォルトの入力テキスト「Alice and Bob are going to a science fair on Friday.」を処理します。異なるイベントの説明から情報を抽出するには、`src/main.py`ファイル内のこのテキストを変更できます。

## サンプル出力

```
Extracted event: name='Science Fair' date='Friday' participants=['Alice', 'Bob']
```

## カスタマイズ

`src/main.py`の`input_text`変数を変更することで、異なるイベントの説明から情報を抽出できます。例：

```python
input_text = "John and Sarah are attending a concert on Saturday night at 8 PM."
```

## エラー処理

このスクリプトには、JSON解析とデータ検証の基本的なエラー処理が含まれています。エラーが発生した場合、コンソールに出力されます。

## 貢献

カレンダーイベント抽出ツールの改善への貢献を歓迎します。プルリクエストを自由に提出してください。

## ライセンス

このプロジェクトはオープンソースであり、[MITライセンス](LICENSE)の下で利用可能です。

## 免責事項

このツールはOpenAIのGPTモデルを使用しており、OpenAIの使用事例ポリシーと価格設定の対象となります。このツールを使用する際は、OpenAIの利用規約を遵守してください。
