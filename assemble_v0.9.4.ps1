
$source = "e:\OneDrive\Documents\GitHub\theatre-cue-player\versions\v0.9.2\v0.9.2.theatre-cue-player.html"
$dest = "e:\OneDrive\Documents\GitHub\theatre-cue-player\versions\v0.9.4\v0.9.4.theatre-cue-player.html"
$artifactDir = "C:\Users\kevin\.gemini\antigravity\brain\7ee84b9b-07a7-4572-9c43-a7ea1d3ff858"

Write-Host "Starting Assembly..."

# Read Source
$lines = Get-Content $source
Write-Host "Source Header Read ($($lines.Count) lines)"

# Extract Top (HTML + CSS)
# Script starts at ~1547. We look for <script>
$scriptLineIndex = 0
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "<script>") {
        $scriptLineIndex = $i
        break
    }
}
Write-Host "Script tag found at $scriptLineIndex"
$top = $lines[0..$scriptLineIndex]

# Extract Bottom (Closing tags)
# We need to find </script> near the end.
# Actually, the original file has a big script block. We want to skip it.
# We search for </script> from the bottom up? Or just scan.
$endScriptIndex = 0
for ($i = $scriptLineIndex + 1; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "</script>") {
        $endScriptIndex = $i
        break
    }
}
Write-Host "End Script tag found at $endScriptIndex"
$bottom = $lines[$endScriptIndex..($lines.Count - 1)]

# Read New JS Components (Line Arrays)
$core = Get-Content "$artifactDir\project_refactor_core.js"
$ui = Get-Content "$artifactDir\project_refactor_ui.js"
$wave = Get-Content "$artifactDir\project_refactor_waveform.js"
$glue = Get-Content "$artifactDir\project_refactor_glue.js"

Write-Host "Core Lines: $($core.Count)"
Write-Host "UI Lines: $($ui.Count)"
Write-Host "Wave Files: $($wave.Count)"
Write-Host "Glue Lines: $($glue.Count)"

# Combine
$finalContent = @()
$finalContent += $top
$finalContent += ""
$finalContent += "// --- CORE ---"
$finalContent += $core
$finalContent += ""
$finalContent += "// --- UI ---"
$finalContent += $ui
$finalContent += ""
$finalContent += "// --- WAVEFORM ---"
$finalContent += $wave
$finalContent += ""
$finalContent += "// --- GLUE ---"
$finalContent += $glue
$finalContent += ""
$finalContent += $bottom

# Write
# Use Set-Content with Encoding UTF8 to avoid issues
$finalContent | Set-Content -Path $dest -Encoding UTF8

Write-Host "Assembly Complete: $dest"
