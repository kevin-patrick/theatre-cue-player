
$source = "e:\OneDrive\Documents\GitHub\theatre-cue-player\versions\v0.9.2\v0.9.2.theatre-cue-player.html"
$dest = "e:\OneDrive\Documents\GitHub\theatre-cue-player\versions\v0.9.4\v0.9.4.theatre-cue-player.html"
$artifactDir = "C:\Users\kevin\.gemini\antigravity\brain\7ee84b9b-07a7-4572-9c43-a7ea1d3ff858"

$core = Get-Content -Raw "$artifactDir\project_refactor_core.js"
$ui = Get-Content -Raw "$artifactDir\project_refactor_ui.js"
$wave = Get-Content -Raw "$artifactDir\project_refactor_waveform.js"
$glue = Get-Content -Raw "$artifactDir\project_refactor_glue.js"

$lines = Get-Content $source
# Script starts at 1547 (index 1546 '<script>')
# End script is near 6641.

# Keep HTML: Lines 1 to 1547 (Including <script>)
$top = $lines[0..1546]

# Keep End: Lines 6641 to End (Including </script> and closing html)
# We need to find exact closing line dynamically or use known index 6640 for </script>
$bottomIndex = 0
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i].Trim() -eq "</script>") {
        $bottomIndex = $i
        break
    }
}
$bottom = $lines[$bottomIndex..($lines.Count - 1)]

# Assemble
$finalContent = $top
$finalContent += $core
$finalContent += $ui
$finalContent += $wave
$finalContent += $glue
$finalContent += $bottom

$finalContent | Set-Content -Path $dest

Write-Host "Assembly Complete: $dest"
