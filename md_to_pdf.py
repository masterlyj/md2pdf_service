# md_to_pdf.py
import os
import re
import asyncio
from markdown_it import MarkdownIt
from playwright.async_api import async_playwright

class MarkdownToPDFConverter:
    """将 Markdown 文件（支持公式、表格、代码块）转化为PDF的工具类"""
    def __init__(self, custom_css: str = ""):
        self.custom_css = custom_css
        # 初始化 Markdown 解析器（支持表格、删除线等）
        self.md = MarkdownIt("commonmark", {"breaks": True, "html": True})
        self.md.enable(["table", "strikethrough"])
    
    def _preprocess_math(self, md_text: str) -> str:
        """预处理多行块级公式，压缩为单行"""
        def replace_block(match):
            content = match.group(1).strip()
            content = re.sub(r'\s+', ' ', content)
            return f"$$ {content} $$"
        return re.sub(r'\$\$\s*([\s\S]*?)\s*\$\$', replace_block, md_text, flags=re.MULTILINE)

    def _md_to_html(self, md_text: str) -> str:
        md_text = self._preprocess_math(md_text)
        return self.md.render(md_text)
    
    async def _html_to_pdf_bytes(self, html_content: str) -> bytes:
        """异步将 HTML 渲染为 PDF，并返回 bytes"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            
            full_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
                <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
                <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
                        onload="renderMathInElement(document.body, {{
                            delimiters: [
                                {{left: '$$', right: '$$', display: true}},
                                {{left: '$', right: '$', display: false}}
                            ]
                        }});"></script>
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
                        line-height: 1.6;
                        padding: 2rem;
                        max-width: 900px;
                        margin: auto;
                    }}
                    table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
                    th, td {{ border: 1px solid #ccc; padding: 0.6em 1em; }}
                    th {{ background-color: #f3f4f6; }}
                    pre {{ background: #f6f8fa; padding: 1em; border-radius: 6px; }}
                    blockquote {{ border-left: 4px solid #ddd; padding-left: 1em; color: #666; }}
                    {self.custom_css}
                </style>
            </head>
            <body>
                {html_content}
            </body>
            </html>
            """
            
            await page.set_content(full_html)
            await page.wait_for_load_state("networkidle")
            
            pdf_bytes = await page.pdf(
                format="A4",
                print_background=True,
                margin={"top": "1cm", "bottom": "1cm", "left": "1cm", "right": "1cm"}
            )
            await browser.close()
            return pdf_bytes

    async def convert_text(self, md_text: str) -> bytes:
        """将 Markdown 文本转换为 PDF 字节流"""
        html = self._md_to_html(md_text)
        pdf_bytes = await self._html_to_pdf_bytes(html)
        return pdf_bytes

    def convert_file(self, input_path: str, output_path: str):
        """主转换接口，用于命令行"""
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"输入文件不存在: {input_path}")
            
        with open(input_path, "r", encoding="utf-8") as f:
            md_text = f.read()
            
        pdf_bytes = asyncio.run(self.convert_text(md_text))

        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

def main():
    import sys
    if len(sys.argv) != 3:
        print("用法: python md_to_pdf.py <输入.md> <输出.pdf>")
        sys.exit(1)
        
    converter = MarkdownToPDFConverter()
    converter.convert_file(sys.argv[1], sys.argv[2])
    print(f"✅ 转换成功: {os.path.abspath(sys.argv[2])}")

if __name__ == "__main__":
    main()