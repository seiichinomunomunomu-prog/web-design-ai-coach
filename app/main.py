import os
from pathlib import Path

import markdown
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# main.pyが置かれているappフォルダ
BASE_DIR = Path(__file__).resolve().parent

# appフォルダ内の.envを明示的に読み込む
# override=Trueで、古いWindows環境変数があっても.envの値を優先する
load_dotenv(
    dotenv_path=BASE_DIR / ".env",
    override=True
)

# Dify APIキーを取得
DIFY_API_KEY = os.getenv("DIFY_API_KEY")

if not DIFY_API_KEY:
    raise RuntimeError(
        "DIFY_API_KEYが読み込めません。"
        "appフォルダ内の.envを確認してください。"
    )


app = FastAPI()

# staticフォルダを公開
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# templatesフォルダを指定
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/review")
def review(
    request: Request,
    html_code: str = Form(...),
    css_code: str = Form(...),
    js_code: str = Form(""),
    question: str = Form(...)
):
    url = "https://api.dify.ai/v1/chat-messages"

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": f"""
以下のHTML、CSS、質問を確認し、
Webデザイン初心者にも分かりやすく改善点を説明してください。

HTML
{html_code}

CSS
{css_code}

JavaScript
{js_code}

質問
{question}
""",
        "response_mode": "blocking",
        "user": "web-design-ai-coach"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=60
        )

        # 通信トラブルの調査時だけ、先頭の「#」を外す
        print("DIFY STATUS:", response.status_code)
        print("DIFY RESPONSE:", response.text)

        result = response.json()

        if response.status_code != 200:
            return {
                "answer": (
                    "Dify APIエラーが発生しました。"
                    f"ステータスコード: {response.status_code}"
                )
            }

        answer_markdown = result.get(
            "answer",
            "回答を取得できませんでした。"
        )

        answer_html = markdown.markdown(
            answer_markdown,
            extensions=["fenced_code", "tables"]
        )

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "answer_html": answer_html,
                "html_code": html_code,
                "css_code": css_code,
                "js_code": js_code,
                "question": question
            }
        )
    
    except requests.exceptions.Timeout:
        return {
            "answer": (
                "Difyからの応答がタイムアウトしました。"
                "しばらくしてから再度お試しください。"
            )
        }

    except requests.exceptions.RequestException as error:
        print("Dify API通信エラー:", error)

        return {
            "answer": "Difyとの通信中にエラーが発生しました。"
        }

    except ValueError as error:
        print("JSON解析エラー:", error)

        return {
            "answer": "Difyからの回答を正しく読み取れませんでした。"
        }