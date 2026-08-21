@echo off
cd /d "%~dp0"

where git >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 当前系统未找到 git 命令。
    echo 请安装 Git for Windows：https://git-scm.com/download/win
    echo 安装时保持默认选项（Add to PATH）即可，装好后重新双击本文件。
    pause
    exit /b 1
)

git push -u origin main
if %errorlevel% neq 0 (
    echo [错误] 推送到 GitHub 失败，请检查网络或仓库权限。
    pause
    exit /b 1
)

echo [完成] 已成功推送到 GitHub。
pause
