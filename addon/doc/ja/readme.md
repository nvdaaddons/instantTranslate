# instantTranslate #

* 作者: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino その他
  NVDA 貢献者。
* ダウンロード [安定版][1]
* ダウンロード [開発版][2]

このアドオンは選択されたおよび/またはクリップボードのテキストを、一つの言語から他の言語に翻訳するのに使用されます。これは、Google
Translateサービスを使用して行われます。

## 言語設定 ##
翻訳元の言語および翻訳先の言語、あるいは入れ替え言語を設定するには、NVDAメニュー、設定、インスタント翻訳の設定に進んで下さい。

「翻訳元の言語」、「翻訳先の言語」とラベルされた、二つのコンボボックスと、翻訳をクリップボードにコピーするかどうかを決めるための一つのチェックボックスがあります。

さらに、「翻訳元の言語」のコンボボックスの言語の自動検出
(一つ目の選択肢)を選択すると、さらに「入れ替え言語」とラベルされたコンボボックスと、自動入れ替えについてのチェックボックスがあります。

最初の二つのコンボボックスとコピーのためのチェックボックスの意味は明快ですが、他についてはもう少し説明が必要です。以下の説明は翻訳元の言語が言語の自動検出に設定されているのを想定しています。

「入れ替え言語」は、翻訳元の言語と翻訳先の言語を、スクリプトを通じて交換する際に有用です(以下を参照して下さい)。実際、翻訳先の言語を言語の自動検出に設定しても意味がありません。よって、このアドオンでは、これを上記のコンボボックスの値に設定します。

そこで、次の場合を想像して下さい。あなたは普段は英語に(あなたの主要言語は英語とします)翻訳しますが、時には(例えば、文章を書いている時に)イタリア語に翻訳する必要があるとします(あなたの二番目の言語と考えて下さい)。あなたは、「入れ替え言語」コンボボックスを、イタリア語に設定出来ます。よって、あなたは英語からイタリア語に、アドオンの設定を直接触ることなく、翻訳することが出来ます。

ここで、自動入れ替えチェックボックス、
これは、「翻訳元の言語」のコンボボックスを言語の自動検出に設定している時のみ現れ、「入れ替え言語」コンボボックスに直接自動的に接続されます。もしこれを有効にすると、アドオンは翻訳元の言語と翻訳先の言語の設定から、翻訳先の言語が翻訳元の言語になる設定に、そして、「入れ替え言語」コンボボックスで選択された言語が新しい翻訳先の言語になるように、自動的に入れ替えようとします。これは、翻訳したいテキストの翻訳元の言語が、翻訳先の言語である場合に非常に便利です。

簡単な例:
また、前に想像した場面を思い出して下さい。もし英語ではない言語のテキストを翻訳するなら、特に問題はなく、正しい英語への翻訳文を得ることが出来ます。しかし、もし、英語からテキストを翻訳したい場合、通常は、原文と同一の英語への翻訳が得られます。これはあまり意味がありません。しかしながら、テキストをイタリア語でどう読むのか知りたいとしたら、この自動入れ替え機能により、自動的に翻訳先の言語をイタリア語にして、有用な翻訳を得ることが出来ます。

しかしながら、これは一時的な設定です; このオプションに効果が見られない場合
(実験的です)、以下に示す入れ替えのためのジェスチャーを使って、手動で安定的な設定に入れ替えてみて下さい。これは実験的で、状況によっては
(典型的には短いテキストでは)、Googleが実際の翻訳元の言語を正しく認識しないためで、その場合は、翻訳元の言語を、前の翻訳先の言語(この例では英語)にするために、スクリプトを通じて言語を手動で入れ替えなければなりません。

少なくとも、読み上げ設定パラメータダイアログ(NVDAメニュー>>設定(P)>>読み上げ), "自動言語切り替え(サポートされている場合)"オプションをチェックしたくなると思います。この方法で、複数言語の合成音声を使用している場合、翻訳が対象言語の合成音声を使用して通知されるようになります。

## 使用方法 ##
三つの方法でこのアドオンを使用出来ます:

1. 選択コマンドでテキストを選択し(例えばshiftキーと矢印キー)、翻訳用のキーを押します。翻訳結果が使用されている合成音声によって読み上げられます。
2. クリップボードからもテキストを翻訳出来ます。
3. 最後に読み上げられたテキストを翻訳するには専用のショートカットキーを押します。

## ショートカットキー ##
以下のキーを、いずれも、修飾キーNVDA+Shift+tの後に押して下さい:

* T: 選択されたテキストを翻訳,
* Shift+t: クリップボードからテキストを翻訳,
* S: 翻訳元の言語と翻訳先の言語を入れ替え,
* A: 現在の設定を通知,
* C: 最後の結果をクリップボードにコピー,
* I: 選択されたテキストの言語を識別,
* L: 最後に読み上げられたテキストを翻訳,
* O: 翻訳設定ダイアログを開く
* H: 全ての使用可能なコマンドをユーザーに通知。

## 4.4.3の変更点 ##
* アンダースコアをスペースに置き換える機能を追加し、内容によってより良い翻訳結果となるようにしました(Beka Gozalishviliのおかげです)
* NVDA 2022.1への互換性を追加

## 4.4.2の変更点 ##
* 言語検出と自動入れ替えを戻しました(Cyrilleの修正のおかげです)
* 翻訳の言語を更新しました(Cyrilleのおかげです)

## 4.4の変更点 ##
* Instant TranslateはNVDA 2019.3(NVDAのPython 3バージョン)に互換しました

## 4.3の変更点 ##
* Instant Translateが、最新のNVDAのビルドに互換となるように、NVDAへの互換性を修正しました。
* 翻訳サービスとしてGoogleを再び使用する方法を見つけました。

## 4.2の変更点 ##
* より新しいNVDAでの動作状態を戻しました。
* 自動言語検出を戻しました。

## 4.1の変更点 ##
* Instant Translateが、Googleの代わりに、Yandex翻訳サービスで、動作するようになりました。

## 4.0の変更点 ##
* 入れ替え後、翻訳が自動的に行われます。
* キャッシュバグを修正しました。

## 3.0の変更点 ##
* ショートカットの使用方法を変更しました。インスタント翻訳用の修飾キーNVDA+Shift+tを押して、一文字キーで動作を選んで実行出来ます
  (ショートカットキーの節の全コマンドをご覧下さい)
* 言語の入れ替えを実装しました。
* 設定画面のフォーマットを変更して、読み取り専用のペインにいる場合も設定を変更できるようになりました。ただし設定変更はNVDAを再起動するまで有効です。
* 翻訳可能な文字数の制限をなくしました。
* Instant Translate設定メニューの項目にショートカットtを追加しました
* 自動オプションを最初のコンボボックスに配置するようにしました。
* 「翻訳結果をコピーする」にチェックボックスを追加しました。
* 設定ファイルを設定フォルダーのルートに保存します。
* 翻訳元の言語と翻訳先の言語を、Google Translateの現在の状態(2015年4月22日時点)に合わせました。


## 2.1の変更点 ##
* NVDA+Shift+Yでクリップボードのテキストを翻訳できるようになりました。

## 2.0 の変更点 ##
* 翻訳言語を選ぶ設定に、GUIを追加しました。
* 「設定メニュー」にアドオンのメニューを追加しました。
* 設定情報を、独立した設定ファイルに書き込むようにしました。
* 翻訳結果を再利用できるようにするために、翻訳結果を自動でクリップボードにコピーするようになりました。

## 1.0 での変更点 ##
* 最初のバージョン。


[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=instantTranslate

[2]: https://www.nvaccess.org/addonStore/legacy?file=it-dev
