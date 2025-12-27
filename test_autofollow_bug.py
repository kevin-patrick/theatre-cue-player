import os
import re
import time
from playwright.sync_api import sync_playwright, expect

# Configuration
# Note: Ensure this path points to the correct v0.9.4 HTML file
HTML_FILE = r"e:\OneDrive\Documents\GitHub\theatre-cue-player\versions\v0.9.4\v0.9.4.theatre-cue-player.html"

# The specific test bundle folder
# Use raw string for Windows paths
TEST_AUDIO_PATH = r"E:\OneDrive\Documents\GitHub\theatre-cue-player\Bundle to put on website and Facebook Tech Theatre Educators"

def run():
    print("Starting Auto-Follow Reproduction Test...")
    
    with sync_playwright() as p:
        # 1. Setup
        try:
            # Launch with headless=False to watch the test
            browser = p.chromium.launch(headless=False)
        except Exception as e:
            print(f"Failed to launch browser: {e}")
            return

        page = browser.new_page()

        # 2. Handle Dialogs (Accept "Project loaded" alerts)
        page.on("dialog", lambda dialog: dialog.accept())

        # Load the application
        print(f"Loading: {HTML_FILE}")
        page.goto(f"file:///{HTML_FILE}")

        # 3. Action (Upload)
        print("Uploading Show Folder...")
        
        # Verify path exists
        if not os.path.exists(TEST_AUDIO_PATH):
             print(f"ERROR: Test Audio Path not found: {TEST_AUDIO_PATH}")
             browser.close()
             return

        # Upload files to the hidden input
        # Corrected: Passing the directory path string directly because input has webkitdirectory attribute
        print(f"Setting input files to directory: {TEST_AUDIO_PATH}")
        page.locator("#showFolderInput").set_input_files(TEST_AUDIO_PATH)

        # 4. Verify Load
        print("Waiting for Cue Table...")
        # Wait for at least one cue row to appear
        # Selector correction: The rows are plain <tr> elements inside .cue-table
        try:
            page.wait_for_selector("table.cue-table tbody tr", timeout=10000)
            rows = page.locator("table.cue-table tbody tr")
            count = rows.count()
            print(f"Cue Table Loaded. Found {count} cues.")
        except:
             print("ERROR: Cue table did not load within timeout.")
             browser.close()
             return

        # 5. Action (Playback)
        print("Starting Cue #1...")
        
        # Ensure Cue 1 is selected (should be by default)
        # Click Global GO
        page.locator("button[onclick*='goNext']").click()
        
        # 6. Observation (The Test)
        row1 = rows.nth(0)
        row2 = rows.nth(1)
        
        # Verify Cue 1 is playing
        print("Verifying Cue 1 is playing...")
        try:
            expect(row1).to_have_class(re.compile(r"playing"), timeout=2000)
            print("Cue 1 started successfully.")
        except AssertionError:
            print("ERROR: Cue 1 did not start.")
            browser.close()
            return
        
        # Wait for Cue 1 to finish
        print("Waiting for Cue 1 to finish...")
        # Wait for 'playing' class to be removed
        # Increasing timeout to ensure we cover the duration of the audio
        expect(row1).not_to_have_class(re.compile(r"playing"), timeout=60000) 
        print("Cue 1 finished.")
        
        # CRITICAL ASSERTION: Verify Auto-Follow trigger
        print("Checking if Cue 2 started automatically (Auto-Follow)...")
        
        try:
            expect(row2).to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: Cue 2 started automatically. Auto-Follow works.")
        except AssertionError:
            print("FAILURE: Cue 2 did NOT start automatically. Auto-Follow bug confirmed.")
            # Keep browser open briefly to see state
            time.sleep(5)
            browser.close()
            return

        # 7. Action (Jump to Cue 7)
        print("Testing Jump to Cue 7...")
        # cueJumpInput might require a value
        page.locator("#cueJumpInput").fill("7")
        # Click Jump button (siblings or nearby) - looking for onclick="jumpToCue()"
        page.locator("button[onclick*='jumpToCue']").click()
        
        # Verify Cue 7 is 'current-cue'
        # Note: Cue 7 is at index 6 (0-based) assuming contiguous 1..8
        row7 = rows.nth(6) # Direct index access is more reliable here
        try:
            expect(row7).to_have_class(re.compile(r"current-cue"), timeout=5000)
            print("SUCCESS: Jumped to Cue 7.")
        except AssertionError:
            print("FAILURE: Did not jump to Cue 7 (Check if 'current-cue' class is applied).")

        # 8. Action (Play Cue 7)
        print("Playing Cue 7...")
        # row7.locator("button.btn-success").click() # Play button in row
        # OR Global GO
        page.locator("button[onclick*='goNext']").click()
        
        try:
            expect(row7).to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: Cue 7 is playing.")
        except AssertionError:
            print("FAILURE: Cue 7 did not start.")

        # Let it play for a moment
        time.sleep(1)

        # 9. Action (Jump to First)
        print("Testing Jump to First...")
        page.locator("button[onclick*='jumpToFirst']").click()
        
        row1 = rows.nth(0) # Cue 1
        try:
            expect(row1).to_have_class(re.compile(r"current-cue"), timeout=2000)
            print("SUCCESS: Jumped back to First Cue.")
        except AssertionError:
            print("FAILURE: Did not jump to First Cue.")

        # 10. Shortcut Tests
        # Ensure focus is cleared from any inputs (like Jump Input)
        page.eval_on_selector("input", "el => el.blur()")
        page.locator("body").click(force=True)

        # A. Spacebar (Go Next)
        print("Testing Shortcut: Spacebar (Go Next)...")
        # Ensure focus is on body/window (click cues area safely)
        page.locator("body").click(force=True)
        page.keyboard.press("Space")
        
        try:
            expect(rows.nth(0)).to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: Spacebar started Cue 1.")
        except AssertionError:
            print("FAILURE: Spacebar did not start Cue 1.")

        time.sleep(1)

        # B. ESC (Stop All)
        print("Testing Shortcut: ESC (Stop All)...")
        page.keyboard.press("Escape")
        try:
            expect(rows.nth(0)).not_to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: ESC stopped playback.")
        except AssertionError:
            print("FAILURE: ESC did not stop playback.")
        
        # C. Up/Down Arrows (Navigation)
        print("Testing Shortcut: Arrow Keys (Navigation)...")
        # Ensure we are at Cue 1 (index 0)
        # Down -> Cue 2
        page.keyboard.press("ArrowDown")
        try:
            expect(rows.nth(1)).to_have_class(re.compile(r"current-cue"), timeout=2000)
            print("SUCCESS: ArrowDown selected Cue 2.")
        except AssertionError:
            print("FAILURE: ArrowDown did not select Cue 2.")
        
        # Up -> Cue 1
        page.keyboard.press("ArrowUp")
        try:
            expect(rows.nth(0)).to_have_class(re.compile(r"current-cue"), timeout=2000)
            print("SUCCESS: ArrowUp selected Cue 1.")
        except AssertionError:
            print("FAILURE: ArrowUp did not select Cue 1.")

        # D. Enter (Play Selected)
        print("Testing Shortcut: Enter (Play Selected)...")
        # Assuming Cue 1 is selected from previous step
        page.keyboard.press("Enter")
        try:
            expect(rows.nth(0)).to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: Enter started Cue 1.")
        except AssertionError:
            print("FAILURE: Enter did not start Cue 1.")

        # E. Backspace (Stop Current)
        print("Testing Shortcut: Backspace (Stop Current)...")
        # Wait 0.5s as requested
        time.sleep(0.5)
        page.keyboard.press("Backspace")
        
        try:
            expect(rows.nth(0)).not_to_have_class(re.compile(r"playing"), timeout=2000)
            print("SUCCESS: Backspace stopped Cue 1.")
        except AssertionError:
            print("FAILURE: Backspace did not stop Cue 1.")


        browser.close()
        print("Test Complete.")

if __name__ == "__main__":
    run()
