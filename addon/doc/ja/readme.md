# instantTranslate #

* 作者: Alexy Sadovoy, ruslan, Beqa Gozalishvili and other nvda contributors.
* download [version 2.2beta2][1]

このアドオンは選択されたテキストやクリップボードのテキストをある言語から別の言語に翻訳します。これはGoogle翻訳のサービスを使って実現しています。

## 言語の設定 ##

翻訳元と翻訳先の言語を設定するには、NVDAメニュー「設定」「インスタント翻訳の設定」を実行してください。
翻訳元と翻訳先のふたつのコンボボックスがあります。言語を選択してOKボタンでエンターキーを押してください。

## このアドオンの使い方 ##

このアドオンには2種類の使い方があります:

1. テキストを選択（Shiftと矢印キーを使うなど）してください。
   Shift+NVDA+Tを押すと選択されたテキストが翻訳されます。
   翻訳結果は、その言語を音声合成がサポートしているなら、音声で読み上げられます。
2. クリップボードにテキストをコピーします。
   Shift+NVDA+Yを押すと、クリップボードのテキストが翻訳先の言語に翻訳されます。

## 2.2 での変更点 ##
* 文字数の上限を1500文字にしました。
* メニューの設定にショートカットを追加
* 設定「翻訳結果のコピー」にチェックボックスを追加
* 設定ファイルを設定フォルダーのルートディレクトリに保存するように変更しました
* 新しい言語:
  アラゴン語、アラビア語、ブラジルポルトガル語、クロアチア語、オランダ語、フィンランド語、フランス語、ガリシア語、ドイツ語、ハンガリー語、イタリア語、日本語、韓国語、ネパール語、ポーランド語、スロバキア語、スロベニア語、スペイン語、タミル語、トルコ語。

## 2.1 での変更点 ##
* NVDA+Shift+Yでクリップボードのテキストを翻訳できるようになりました。

## 2.0 での変更点 ##
* Added gui configurator where you can choose source and target languages.
* Added addon menu item found under preferences menu.
* Settings now is written in separate config file.
* Translation results now automatically copies into the clipboard for future
  manipulations.

## 1.0 での変更点 ##
* Initial version.

[[!tag dev]]

[1]: http://addons.nvda-project.org/files/get.php?file=it
