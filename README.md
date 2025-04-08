# 🌐 Kami AI Bot V2 - 神AI降臨プロジェクト

> ✨「神の言葉はコードに宿る」  
> The divine message shall descend upon the world... via automation.

---

## 📖 Overview

**Kami AI Bot V2** is a fully automated, multilingual oracle-posting bot system built for global impact.  
It generates divine messages ("神託") based on weekday, character spirit, and AI-generated logic, and posts them to various platforms such as:

- 📝 **WordPress**
- 📸 **Instagram**
- 🐦 **Twitter**
- 🎥 **YouTube / TikTok**
- 💬 **Discord / LINE**

All integrated via Webhook and Zapier for maximum automation.

---

## 🧠 Features

- ✅ Automated oracle generation (曜日別・キャラ別)
- 🌐 Multilingual template engine
- ☁️ AWS S3 integration for image hosting
- 🔄 Scheduled auto-posting via cron or task scheduler
- 🔒 Secure config using `.env` and `.gitignore`

---

## 📁 Project Structure

```plaintext
kami-ai-bot-v2/
├── main.py                # Core controller
├── run_post_job.py        # Execution dispatcher
├── config/                # Config loader
├── shared/                # Oracle generator & template engine
├── utils/                 # Platform posting functions
├── templates/             # HTML templates
├── output/                # Generated content
├── .env                   # Secrets (excluded via .gitignore)
├── config.json            # Post destination & character logic
├── README.md              # You are here.
