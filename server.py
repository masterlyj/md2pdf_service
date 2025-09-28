import sys
import asyncio
# # --- 修复 Windows 下 asyncio 事件循环 ---
# # 在 Windows 上，默认的 ProactorEventLoop 不支持 subprocess，Playwright 依赖于 subprocess，因此需要切换为 SelectorEventLoopPolicy。
# if sys.platform == "win32":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import Response
import uvicorn
from md_to_pdf import MarkdownToPDFConverter

app = FastAPI(
    title="Markdown to PDF Converter API",
    description="An API to convert Markdown text to a PDF file.",
    version="1.0.0",
)

# 初始化转换器实例
converter = MarkdownToPDFConverter()

@app.post(
    "/convert",
    summary="Convert Markdown to PDF",
    response_description="A PDF file.",
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Successful conversion.",
        },
        500: {"description": "Internal server error during conversion."},
    },
)
async def convert_markdown_to_pdf(
    md_text: str = Body(..., media_type="text/markdown", description="Markdown text to convert.")
):
    """
    接收请求体中的 Markdown 文本，返回 PDF 文件。
    """
    try:
        pdf_bytes = await converter.convert_text(md_text)
        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=output.pdf"},
        )
    except Exception as e:
        # 生产环境建议使用更完善的日志
        print(f"Error during PDF conversion: {e}")
        raise HTTPException(status_code=500, detail="Failed to convert Markdown to PDF.")

if __name__ == "__main__":
    # 使用 uvicorn 启动服务
    # 生产环境建议使用 gunicorn + uvicorn workers
    uvicorn.run(app, host="0.0.0.0", port=8020)