# Climate 測試

> **Climate 無法相容於 Windows 平台，如需在該平台上運行，務必請使用 Docker，或轉為使用 GNU/Linux 系統（推薦 Debian >= 10）來運行**

Climate 採用 PyTest 及 GitHub Action，分別進行單元測試及自動化整合。

## 自動化整合

該部分負責了「單元測試」及「鏡像建構」。

關於自動化整合流水線，請參見：

<https://github.com/poyang31/hw_2021_12/actions>

## PyTest 單元測試

PyTest 單元測試使用說明，需詳見：

<https://docs.pytest.org>

## PyTest 全部測試

利用 PyTest 進行全部測試，請安裝所有需求套件，並在程式工作根目錄下，請輸入：

```shell
pytest
```
