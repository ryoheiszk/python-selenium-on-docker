# Python-Selenium on Docker

## 使用方法

`build.sh`を実行すれば必要なDockerコマンドが実行される。

VSCodeユーザーなら、`.devcontainer/devcontainer.json`の通り`ms-vscode-remote.remote-containers`用の設定ができているため利用されたし。

`vnc://localhost:5900`にてブラウザの表示を見ながらデバッグが可能。

WindowsユーザならRealVNCで動作確認済み。


---

## my memo

- vnc クライアントは realVNC を使用
    - hostは localhost:5900 で
    - 初期passwordは "secret"


- [SeleniumIDE for firefox](https://addons.mozilla.org/ja/firefox/addon/selenium-ide/)を使用する

  - テスト作成後以下の処理を実行する

  1. Export

  2. Python pytes を選択

  3. Export for use on Selenium Grid を選択
     1. Remote URL を "http://selenium:4444/wd/hub" に変更

  4. Export

  5. 対象サーバーとして、localhost:8080 等を指定している場合は、"localhost" を "host.docker.internal" へ変更


テストの実行は、``` ./build.sh ``` 後に ```pytest tests```
