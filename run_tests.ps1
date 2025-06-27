$env:PYTHONPATH = "..;$env:PYTHONPATH"

Write-Output "Running unit tests for MusicFolderHelper..."
py .\tests\test_ArtistFolder.py

Write-Output "Running integration tests for MusicFolderHelper..."
.\run_MusicFolderHelperOn.bat .\tests\testData