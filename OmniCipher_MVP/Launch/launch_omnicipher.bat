@echo off
title OmniCipher Launcher

echo ============================================
echo    Launching OmniCipher Whitebox System
echo ============================================

:: Change directory to project root (one level above this .bat file)
cd /d "%~dp0..\"

:: Launch the AI controller
python Core\run_ai.py

pause
