// server.js
const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// 提供靜態檔案的中介軟體
app.use(express.static(path.join(__dirname)));

// 定義根路由
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html')); // 假設你的 HTML 檔案名為 index.html
});

// 啟動伺服器
app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});