$exclude = @("venv", "template_DesktopBOT_BotCity.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "template_DesktopBOT_BotCity.zip" -Force