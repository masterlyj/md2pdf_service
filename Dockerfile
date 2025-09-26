# 使用官方 Playwright 镜像
FROM mcr.microsoft.com/playwright/python:v1.55.0-jammy

# 安装 uv
RUN pip install --no-cache-dir uv

WORKDIR /app

# 复制项目元数据
COPY pyproject.toml uv.lock ./

# 使用 uv 安装项目及其依赖
RUN uv pip install --system --no-cache-dir .


# 复制源代码
COPY md_to_pdf.py server.py ./

# 暴露端口
EXPOSE 8020

# 启动 FastAPI 服务
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8020"]