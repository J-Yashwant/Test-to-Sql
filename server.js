const express = require("express");
const connectDB = require("./config/db");

require("dotenv").config();
connectDB();

const app = express();
app.use(express.json());

app.get("/", (req, res) => res.send("MCP Server Running"));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));