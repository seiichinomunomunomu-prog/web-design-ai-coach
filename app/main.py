import os
from pathlib import Path
import json
import markdown
import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

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
DIFY_CREATE_API_KEY = os.getenv("DIFY_CREATE_API_KEY")

APP_PASSWORD = os.getenv("APP_PASSWORD")
SESSION_SECRET = os.getenv("SESSION_SECRET")


if not DIFY_API_KEY:
    raise RuntimeError(
        "DIFY_API_KEYが読み込めません。"
        "appフォルダ内の.envを確認してください。"
    )
if not DIFY_CREATE_API_KEY:
    raise RuntimeError(
        "DIFY_CREATE_API_KEYが読み込めません。"
        "appフォルダ内の.envを確認してください。"
    )
if not APP_PASSWORD:
    raise RuntimeError(
        "APP_PASSWORDが読み込めません。"
        "appフォルダ内の.envを確認してください。"
    )

if not SESSION_SECRET:
    raise RuntimeError(
        "SESSION_SECRETが読み込めません。"
        "appフォルダ内の.envを確認してください。"
    )

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key=SESSION_SECRET
)

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

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": None
        }
    )


@app.post("/login")
def login(
    request: Request,
    password: str = Form(...)
):
    if password == APP_PASSWORD:
        request.session["authenticated"] = True

        return RedirectResponse(
            url="/",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": "パスワードが違います。"
        }
    )

@app.get("/logout")
def logout(request: Request):
    request.session.clear()

    return RedirectResponse(
        url="/login",
        status_code=303
    )

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    if not request.session.get("authenticated"):
        return RedirectResponse(
            url="/login",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
@app.get("/create", response_class=HTMLResponse)
def create_page(request: Request):

    if not request.session.get("authenticated"):
        return RedirectResponse(
            url="/login",
            status_code=303
        )

    return templates.TemplateResponse(
        request=request,
        name="create.html"
    )    
@app.post("/create")
def create_webpage(
    request: Request,
    request_text: str = Form(...)
):

    if not request.session.get("authenticated"):
        return RedirectResponse(
            url="/login",
            status_code=303
        )

    url = "https://api.dify.ai/v1/chat-messages"

    headers = {
        "Authorization": f"Bearer {DIFY_CREATE_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": request_text,
        "response_mode": "blocking",
        "user": "web-design-ai-coach-create"
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=120
        )

        print("CREATE DIFY STATUS:", response.status_code)
        
        response.raise_for_status()
        result = response.json()

        answer_text = result["answer"]
        create_result = json.loads(answer_text)

        generated_html = create_result["html"]
        generated_css = create_result["css"]
        generated_javascript = create_result["javascript"]
        generated_explanation = create_result["explanation"]

        html_lower = generated_html.lower()

        style_block = f"""
        <style>
        {generated_css}
        </style>
        """

        script_block = ""

        if generated_javascript:
            script_block = f"""
        <script>
        {generated_javascript}
        </script>
        """

        if "<html" in html_lower and "</html>" in html_lower:

            preview_html = generated_html

            # Previewでは外部CSSファイルを読み込まない
            preview_html = preview_html.replace(
                '<link rel="stylesheet" href="style.css">',
                ''
            )

            # Previewでは外部JavaScriptファイルを読み込まない
            preview_html = preview_html.replace(
                '<script src="style.js"></script>',
                ''
            )

            # CSSをPreviewへ埋め込む
            if "</head>" in preview_html.lower():
                head_end_index = preview_html.lower().rfind("</head>")

                preview_html = (
                    preview_html[:head_end_index]
                    + style_block
                    + preview_html[head_end_index:]
                )

            else:
                preview_html = style_block + preview_html

            # JavaScriptをPreviewへ埋め込む
            if generated_javascript:
                if "</body>" in preview_html.lower():
                    body_end_index = preview_html.lower().rfind("</body>")

                    preview_html = (
                        preview_html[:body_end_index]
                        + script_block
                        + preview_html[body_end_index:]
                    )

                else:
                    preview_html += script_block

        else:

            preview_html = f"""
        <!DOCTYPE html>
        <html lang="ja">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {style_block}
        </head>

        <body>
            {generated_html}
            {script_block}
        </body>
        </html>
        """        

        print("CREATE HTML取得:", bool(generated_html))
        print("CREATE CSS取得:", bool(generated_css))
        print("CREATE JAVASCRIPT取得:", bool(generated_javascript))
        print("CREATE EXPLANATION取得:", bool(generated_explanation))
        print("CREATE PREVIEW HTML取得:", bool(preview_html))
        
        return templates.TemplateResponse(
            request=request,
            name="create.html",
            context={
                "request_text": request_text,
                "generated_html": generated_html,
                "generated_css": generated_css,
                "generated_javascript": generated_javascript,
                "generated_explanation": generated_explanation,
                "preview_html": preview_html
            }
        )

    except requests.exceptions.Timeout:
        print("CREATE DIFY TIMEOUT")

        return templates.TemplateResponse(
            request=request,
            name="create.html",
            context={
                "request_text": request_text,
                "error_message": "AIの生成に時間がかかりすぎました。しばらくしてからもう一度お試しください。"
            }
        )

    except requests.exceptions.RequestException as error:
        print("CREATE DIFY通信エラー:", error)

        return templates.TemplateResponse(
            request=request,
            name="create.html",
            context={
                "request_text": request_text,
                "error_message": "AIとの通信に失敗しました。しばらくしてからもう一度お試しください。"
            }
        )
    except ValueError as error:
        print("CREATE JSON解析エラー:", error)

        return templates.TemplateResponse(
            request=request,
            name="create.html",
            context={
                "request_text": request_text,
                "error_message": "AIの回答形式を正しく読み取れませんでした。もう一度お試しください。"
            }
        )
    
    except KeyError as error:
        print("CREATE 必須項目エラー:", error)

        return templates.TemplateResponse(
            request=request,
            name="create.html",
            context={
                "request_text": request_text,
                "error_message": "AIの回答に必要な情報が不足していました。もう一度お試しください。"
            }
        )

@app.post("/review")
def review(
    request: Request,
    html_code: str = Form(""),
    css_code: str = Form(""),
    js_code: str = Form(""),
    question: str = Form(...)
):

    if not request.session.get("authenticated"):
        return RedirectResponse(
            url="/login",
            status_code=303
        )

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