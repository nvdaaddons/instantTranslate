# instantTranslate #

* 作者: Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino その他
  NVDA 貢献者
* ダウンロード [安定版][1]
* ダウンロード [開発版][2]

This add-on is used to translate selected and/or clipboard text from one
language to another.  This is done using the Google Translate service.

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

Anyway, this is a temporary configuration; if this option has no effect
(it's experimental), try to commute manually to a stable configuration,
using the gesture for swapping described below. It's experimental because in
some situations (with short texts, typically), Google does not recognize the
real source language correctly, and you have to swap languages manually via
script, so to force the source language to be the previous target language
(English in our example).

At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.

## 使用方法 ##
You can use this add-on in three ways:

1. Select some text using selection commands (shift with arrow keys, for
   example) and press associated key to translate. translation result will
   be read with synthesizer which you are using.
2. クリップボードからもテキストを翻訳出来ます。
3. Press the dedicated shortcut key to translate the last spoken text.

## ショートカットキー ##
以下のキーを、いずれも、修飾キーNVDA+Shift+tの後に押して下さい。

* T: 選択されたテキストを翻訳
* Shift+t: クリップボードからテキストを翻訳
* S: 翻訳元の言語と翻訳先の言語を入れ替え
* A: 現在の設定を通知
* C: 最後の結果をクリップボードにコピー
* I: 選択されたテキストの言語を識別
* L: translate the last spoken text,
* O: open translation settings dialog
* H: announces all available layered commands.

## Changes for 4.4.2 ##
* Restore language detection and auto-swapping (Thanks to Cyrille for fix)
* updated languages for translation (thanks to Cyrille)

## Changes for 4.4 ##
* Instant translate is now compatible with NVDA 2019.3 (Python 3 versions of
  NVDA)

## Changes for 4.3 ##
* nvda compatibility fix Now instant translate will be compatible with
  latest nvda builds.
* found a way to use google as a translation service again.

## Changes for 4.2 ##
* Restored working state with newer versions of nvda.
* Restored automatic language detection.

## Changes for 4.1 ##
* InstantTranslate is working again, now with Yandex translator service
  instead of Google.

## Changes for 4.0 ##
* Translation is automatically performed after swapping.
* Cache bug fixed.

## 3.0 での変更点 ##
* ショートカットの使用方法を変更しました。インスタント翻訳用の修飾キーNVDA+Shift+tを押して、一文字キーで動作を選んで実行出来ます
  (ショートカットキーの節の全コマンドをご覧下さい)
* 言語の入れ替えを実装しました。
* 設定画面のフォーマットを変更して、読み取り専用のペインにいる場合も設定を変更できるようになりました。ただし設定変更はNVDAを再起動するまで有効です。
* 翻訳可能な文字数の制限をなくしました。
* メニューの設定にショートカットを追加しました。
* 自動オプションを最初のコンボボックスに配置するようにしました。
* 「翻訳結果をコピーする」にチェックボックスを追加しました。
* 設定ファイルを設定フォルダーのルートディレクトリに保存するように変更しました
* 翻訳元の言語と翻訳先の言語を、Google Translateの現在の状態(2015年4月22日時点)に合わせました。


## 2.1 での変更点 ##
* NVDA+Shift+Yでクリップボードのテキストを翻訳できるようになりました。

## 2.0 での変更点 ##
* 翻訳言語を選ぶ設定に、GUIを追加しました。
* 「設定メニュー」にアドオンのメニューを追加しました。
* 設定情報を、独立した設定ファイルに書き込むようにしました。
* 翻訳結果を再利用できるようにするために、翻訳結果を自動でクリップボードにコピーするようになりました。

## 1.0 での変更点 ##
* 最初のバージョン


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=it

[2]: https://addons.nvda-project.org/files/get.php?file=it-dev
