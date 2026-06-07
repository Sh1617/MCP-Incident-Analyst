# MCP Incident Analyst

AI-Powered Multi-Agent Incident Investigation Platform built using LangGraph, Ollama, ChromaDB, PostgreSQL, FastAPI, and OpenTelemetry.

## Overview

MCP Incident Analyst automates Root Cause Analysis (RCA) by orchestrating multiple AI agents that analyze logs, correlate GitHub commits, retrieve historical incidents, search documentation, and generate investigation reports.

The platform follows an Agentic AI architecture where specialized agents collaborate to investigate incidents and produce actionable RCA reports.

---

## Features

### Multi-Agent Workflow

- Supervisor Agent
- Log Analysis Agent
- GitHub Correlation Agent
- RCA Generation Agent

### AI & LLM

- Ollama Integration
- TinyLlama Local LLM
- Retrieval-Augmented Generation (RAG)
- ChromaDB Vector Database

### Incident Investigation

- Log Analysis
- Historical Incident Correlation
- Git Commit Analysis
- Automated Root Cause Analysis
- Confidence Scoring

### Observability

- Structured Logging
- Agent Execution Metrics
- OpenTelemetry Tracing

### Persistence

- PostgreSQL Database
- Investigation History
- RCA Report Storage
- RCA Report Retrieval

### APIs

- Health Check API
- Investigation API
- Reports API
- Investigations API
- Metrics API

---

## Architecture

User Query
│
▼
FastAPI
│
▼
LangGraph Workflow
│
├── Supervisor Agent
├── Log Agent
├── GitHub Agent
└── RCA Agent
│
▼
Ollama LLM
│
├── ChromaDB (RAG)
├── PostgreSQL
└── GitHub Repository
│
▼
Root Cause Analysis Report

---

## Tech Stack

### AI / LLM

- LangGraph
- LangChain
- Ollama
- TinyLlama

### Data

- PostgreSQL
- ChromaDB

### Backend

- FastAPI
- Pydantic

### Observability

- OpenTelemetry
- Structured Logging

### Development

- Python 3.12
- Git
- GitHub

---

## API Endpoints

### Health Check

```http
GET /health
```

### Investigate Incident

```http
POST /investigate
```

Request

```json
{
  "query": "Why did my website login fail on Sunday?"
}
```

### Reports

```http
GET /reports
```

### Get Report

```http
GET /reports/{report_id}
```

### Investigations

```http
GET /investigations
```

### Metrics

```http
GET /metrics
```

---

## Example RCA Output

```text
Executive Summary

The login service experienced authentication failures due to invalid credentials.

Evidence Collected

- Login failure logs detected
- Historical incidents matched
- Documentation identified credential issues

Root Cause

Misconfigured credentials caused authentication failures.

Impact Analysis

Users were unable to authenticate successfully.

Remediation Steps

1. Verify credentials
2. Update authentication configuration
3. Validate login workflows

Confidence Score

0.90
```

---

## Project Structure

```text
backend/
│
├── agents/
│   ├── supervisor_agent.py
│   ├── log_agent.py
│   ├── github_agent.py
│   └── rca_agent.py
│
├── api/
│   ├── health.py
│   ├── investigate.py
│   ├── reports.py
│   ├── investigations.py
│   └── metrics.py
│
├── graphs/
│   └── workflow.py
│
├── repositories/
│   └── investigation_repository.py
│
├── mcp/
│   ├── clients/
│   └── manager.py
│
├── llm/
│   └── factory.py
│
└── main.py
```

---

## Key Achievements

- Built an Agentic AI system using LangGraph
- Implemented automated Root Cause Analysis
- Integrated local LLM inference using Ollama
- Added Retrieval-Augmented Generation using ChromaDB
- Persisted investigations and reports in PostgreSQL
- Implemented OpenTelemetry tracing and metrics
- Exposed production-style REST APIs using FastAPI

---
