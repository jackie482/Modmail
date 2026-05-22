#!/bin/bash
python -m http.server $PORT &
python bot.py
