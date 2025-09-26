# Markdown to PDF Converter

A simple and powerful tool to convert Markdown files into high-quality PDF documents, with excellent support for LaTeX math formulas, tables, and code blocks.

## Features

- Converts Markdown to PDF.
- Renders LaTeX math using KaTeX.
- Supports GitHub Flavored Markdown (tables, strikethrough).
- Customizable via CSS.

## Installation

1. Clone this repository.
2. Install dependencies using `uv`:
    ```bash
    uv pip install -e .
    ```
3. Install Playwright browser dependencies:
    ```bash
    uv run playwright install chromium
    ```

## Usage

Use the `md2pdf` command provided by the tool:

```bash
uv run md2pdf <input.md> <output.pdf>
```

**Example:**
```bash
uv run md2pdf test.md output.pdf
```