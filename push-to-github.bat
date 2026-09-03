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

if not exist ".github_token" (
    echo [错误] 未找到 .github_token，请把 GitHub PAT 放入该文件。
    pause
    exit /b 1
)

for /f "delims=" %%a in (.github_token) do set TOKEN=%%a
set TOKEN=%TOKEN: =%

git -c credential.helperselector= -c credential.helper= -c http.version=HTTP/1.1 push "https://%TOKEN%@github.com/shirleyleung5616-crypto/vortixkitchen.git" main
if %errorlevel% neq 0 (
    echo [错误] 推送到 GitHub 失败，请检查网络或仓库权限。
    pause
    exit /b 1
)

echo [完成] 已成功推送到 GitHub。
pause
