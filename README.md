# aidevteam-playground

AI Development Team の実証用の、公開の小さなリポジトリ。
AI が Issue から計画・実装・テストを行うときの対象として使う。

## 中身

- `calculator.py`: 小さな計算の関数（外部の依存なし）
- `tests/`: pytest のテスト

## テストの動かし方

```bash
python -m pytest
```

Python 3.12 以上と pytest だけを使う。

## 注意

このリポジトリは公開で、中身（Issue を含む）は外部の AI に送られることがある。
秘密情報（トークン・パスワード・鍵・AWS のアカウント ID など）・個人情報・ほかのリポジトリの情報を置かない・書かない。
