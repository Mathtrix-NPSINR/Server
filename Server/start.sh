#!/usr/bin/env sh
uvicorn app:app --reload --workers 1 --host 0.0.0.0 --port 8000
