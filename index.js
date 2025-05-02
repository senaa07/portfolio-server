const express = require("express");
const { Resend } = require("resend");
const cors = require("cors");
const axios = require("axios").default;
require("dotenv").config();
const app = express();
app.use(cors());
app.use(express.json());
const PORT = process.env.PORT || 8080;
/*
app.get("/", async (req, res) => {
    const { data, error } = await resend.emails.send({
        from: "Sena <senaabhisheksvs@gmail.com>",
        to: ["delivered@resend.dev"],
        subject: "Thanks world",
        html: "<strong>it works!</strong>",
    });

    if (error) {
        return res.status(400).json({ error });
    }

    res.status(200).json({ data });
});
*/
app.post("/api/form", async (req, res) => {
    try {
        const { recaptchaValue } = req.body;
        axios({
            url: `https://www.google.com/recaptcha/api/siteverify?secret=${process.env.RECAPTCHA_SECRET_KEY}&response=${recaptchaValue}`,
            method: "POST",
        })
            .then(async ({ data }) => {
                if (data.success) {
                    console.log("success");

                    res.status(200).json({ data });
                }
            })
            .catch((error) => {
                console.log("Invalid recaptcha");
                res.status(400).json({ error: "invalid recaptcha" });
            });
    } catch (error) {
        res.status(400).json({ error: "Error invalid" });
    }
});
app.listen(3000, () => {
    console.log(`Server running on port ${PORT}`);
});
