# セキュリティチェックシート

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yuzoiwasaki/security-checksheet/pulls)

オープンソースのセキュリティチェックシートです。誰でも自由に使ってください。PRも歓迎です。みんなでより良いセキュリティチェックシートを作っていきましょう！

自社におけるセキュリティ観点でのチェックにも使えるかもしれません。

## 背景
Web上にちょうど良いセキュリティチェックシートがなかったので、作ったものを公開してオープンソースとしてブラッシュアップしていければと考えました。

私の属性的に、現在のチェックシートにはセキュリティ以外の観点も入っていると思います。

## 方針
網羅的なものを作るというより、一般的なWeb企業を対象に最低限聞けると良さそうな項目をまとめています。ある程度の手軽さは維持したいです。

## CSVファイルの更新

```bash
python3 scripts/convert_to_csv.py
```