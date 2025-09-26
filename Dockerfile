# 使用更小的基础镜像
FROM mcr.microsoft.com/playwright/python:v1.48.0-jammy

WORKDIR /app
COPY md_to_pdf.py .
COPY requirements.txt .

# 只安装必要依赖
RUN pip install --no-cache-dir -r requirements.txt

# 删除不用的浏览器（Firefox/WebKit）
RUN rm -rf /ms-playwright/firefox-* /ms-playwright/webkit-*

ENTRYPOINT ["python", "md_to_pdf.py"]