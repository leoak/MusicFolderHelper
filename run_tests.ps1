$env:PYTHONPATH = "..;$env:PYTHONPATH"

Write-Host "Running unit tests for MusicFolderHelper..."
py .\tests\test_ArtistFolder.py

Write-Host ""
Write-Host "Running unit tests for MusicFolderHelper..."
py .\tests\test_CUEFile.py

Write-Host ""
Write-Host "Running integration tests for MusicFolderHelper..."
py .\tests\test_MAIN.py

Write-Host ""
Write-Host "Running on All Test date for MusicFolderHelper should not fail/crash"
.\run_MusicFolderHelperOn.bat .\tests\testData