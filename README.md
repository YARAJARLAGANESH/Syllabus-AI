# Syllabus-AI
Syllabus AI is a multi-agent system that converts raw curriculum PDFs/text into structured, chapter-wise syllabi. It uses Planner, Worker, and Evaluator agents to generate summaries, objectives, subtopics, MCQs, and resources, with session memory, context engineering, observability, and modular LLM support.

Syllabus AI is a multi-agent system designed to automatically convert unstructured college curriculum text/PDF content into clean, structured, chapter-wise syllabus outputs.
The project includes a Planner–Worker–Evaluator architecture, session memory, LLM stubs, modular tools, and a full pipeline demonstrated inside updated_multi_agent_syllabus_generator.ipynb.

🚀 Features
Multi-Agent Pipeline

Planner Agent — Detects chapters, builds task plans

Worker Agent — Generates summaries, objectives, subtopics, MCQs

Evaluator Agent — Validates output and assigns quality score

Session Memory & Context Engineering

Stores raw text, chapter data, and intermediate outputs

Clean chunking and prompt templates

Modular Architecture

Tools folder for future OCR / PDF parsing

Swappable LLM backend (stub included)

Runs Completely in Jupyter / Google Colab

The notebook builds the entire folder structure

Generates all project files automatically

Produces JSON-style structured outputs for each chapter

📁 Project Structure (Generated Automatically)
project/
 ├─ agents/
 │   ├─ planner.py
 │   ├─ worker.py
 │   └─ evaluator.py
 ├─ core/
 │   ├─ context_engineering.py
 │   └─ a2a_protocol.py
 ├─ memory/
 │   └─ session_memory.py
 ├─ tools/
 │   └─ tools.py
 ├─ services/
 │   └─ llm_client.py
 ├─ main_agent.py
 ├─ run_demo.py
 └─ requirements.txt

🧠 How It Works

User provides syllabus text

Planner detects chapters

Worker generates content per chapter

Evaluator checks quality

Notebook displays final structured output

Everything is orchestrated inside the notebook to make testing easy.

📄 Notebook Included
updated_multi_agent_syllabus_generator.ipynb

This notebook:

Creates the entire project directory

Writes all Python modules

Contains test cases

Demonstrates end-to-end execution

Prints structured syllabus output

This file is meant to be the core entry point for running the whole system.

🧩 Technologies Used

Python 3

Lightweight LLM stub (replaceable with OpenAI or others)

Modular agent-based architecture

JSON-style message passing

Jupyter Notebook / Google Colab

🎯 Goals

Help students quickly understand syllabus content

Provide structured study materials

Prepare AI agent workflows for real-world deployment

📦 Installation (Inside Notebook Only)

No manual installation needed.
Just open the notebook and run all cells — it generates every dependency file automatically.

🧪 Testing

Use:

from project.main_agent import run_agent
print(run_agent("Unit 1: Intro to AI\nApplications..."))
