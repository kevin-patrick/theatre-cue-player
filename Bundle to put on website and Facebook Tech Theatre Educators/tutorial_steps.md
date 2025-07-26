# Theatre Cue Player Tutorial Steps

This document provides the complete tutorial step configuration and implementation details for the Theatre Cue Player tutorial system. Use this as a reference when implementing the tutorial in updated versions of the application.

## Tutorial System Architecture

### Core Components
- **TutorialManager Class**: Manages tutorial state, step progression, and UI interactions
- **Tutorial Overlay**: Semi-transparent overlay that controls user interaction
- **Tutorial Content Window**: Draggable window containing step instructions
- **UI Highlighting**: System to highlight specific interface elements
- **Success Triggers**: Automated detection of user actions to advance steps

### Key Features Implemented
1. **Draggable Tutorial Windows**: Users can drag tutorial windows by the header
2. **Responsive Design**: Works on desktop, tablets, and Chromebooks
3. **Multiple Interaction Modes**: Overlay, spotlight, selective button, and transparent modes
4. **Automatic Step Progression**: Based on user actions and success triggers
5. **Viewport Boundary Constraints**: Tutorial windows stay within browser bounds

## Tutorial Steps Configuration

### Step 1: Welcome
```javascript
{
    stepNumber: 1,
    title: "Welcome to Theatre Cue Player",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Welcome to Theatre Cue Player! This tutorial will teach you the basics of managing audio cues for theatre productions.\n\nAll the tutorial windows can be moved by grabbing the top bar of the window.\n\nClick Next to begin.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 2: Load Show Folder
```javascript
{
    stepNumber: 2,
    title: "Load Show Folder",
    uiTarget: "Load Show Folder button",
    position: "below",
    overlayText: "First, let's load a show folder with audio files. Click the 'Load Show Folder' button to browse for a folder containing audio files.",
    userAction: "click_element",
    successTrigger: "folder_selected"
}
```

### Step 3: Show Information
```javascript
{
    stepNumber: 3,
    title: "Show Information",
    uiTarget: "Show Info",
    position: "below",
    overlayText: "Great! Your show folder has been loaded. The show information displays in the header. You can click on the show name to rename it.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 4: Edit Mode
```javascript
{
    stepNumber: 4,
    title: "Edit Mode",
    uiTarget: "Edit Mode",
    position: "below",
    overlayText: "To modify cues, you need to enter Edit Mode. This prevents accidental changes during a show. Click 'Edit Mode' to begin editing.",
    userAction: "click_element",
    successTrigger: "edit_mode_active"
}
```

### Step 5: Cue List Overview
```javascript
{
    stepNumber: 5,
    title: "Cue List Overview",
    uiTarget: "Next",
    position: "centered",
    overlayText: "This is your cue list! Each row represents an audio cue with properties like volume, pan, fade times, and more. The columns let you control every aspect of audio playback.\n\nClick Next to learn about adding cues.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 6: Add Audio Cue
```javascript
{
    stepNumber: 6,
    title: "Add Audio Cue",
    uiTarget: "Add Audio Cue",
    position: "below",
    overlayText: "Let's add your first audio cue. Click the 'Add Audio Cue' button to create a new cue and select an audio file.",
    userAction: "click_element",
    successTrigger: "audio_cue_added"
}
```

### Step 7: File Selection
```javascript
{
    stepNumber: 7,
    title: "Select Audio File",
    uiTarget: "Next",
    position: "bottom-center",
    overlayText: "Choose an audio file from the list. You can see files organized by folders. Pick any file you'd like for your first cue.\n\nClick Next after selecting a file.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 8: Cue Properties
```javascript
{
    stepNumber: 8,
    title: "Cue Properties",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Excellent! Your cue has been added to the list. Notice all the properties you can adjust: Volume, Pan, Fade In/Out, Loop count, and more.\n\nClick Next to learn about playback controls.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 9: Actions Column
```javascript
{
    stepNumber: 9,
    title: "Actions",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Each individual cue also has playback controls. Sometimes we want to play cues out of order. Sometimes we click \"GO\" before it was the right time.\n\nIn Theatre Cue Player, you can stop or fade out individual cues without having to stop the whole show.\n\nTry playing a longer cue with its individual green play button, then fade it out with the yellow slash. Click Next after you've experimented with this.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 10: Show Control
```javascript
{
    stepNumber: 10,
    title: "Show Control",
    uiTarget: "GO button",
    position: "left",
    overlayText: "The main 'GO' button plays cues in sequence. It will play the currently selected cue (highlighted in blue). Try clicking GO to play your first cue.",
    userAction: "click_element",
    successTrigger: "audio_playing"
}
```

### Step 11: Navigation Controls
```javascript
{
    stepNumber: 11,
    title: "Navigation",
    uiTarget: "Next",
    position: "left",
    overlayText: "Use the arrow buttons or keyboard arrow keys to navigate between cues. The STOP button stops all playing audio. The PAUSE button pauses the current cue.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 12: Add More Cues
```javascript
{
    stepNumber: 12,
    title: "Add More Cues",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Let's add a few more cues to build a sequence. Add 2-3 more audio cues using the 'Add Audio Cue' button. Choose different files to create variety.\n\nClick Next when you have at least 3 cues total.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 13: Cue Numbering
```javascript
{
    stepNumber: 13,
    title: "Cue Numbers",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Notice that cues are automatically numbered (1, 2, 3...). You can click on any cue number to change it. This is useful for inserting cues between existing ones (like 1.5, 2.5).\n\nClick Next to learn about renaming cues.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 14: Rename Cue
```javascript
{
    stepNumber: 14,
    title: "Rename Cue",
    uiTarget: "Cue Label",
    position: "right",
    overlayText: "Click on any cue name in the 'Cue Label' column to rename it. Give your cues descriptive names like 'Preshow Music' or 'Thunder Sound'.",
    userAction: "click_element",
    successTrigger: "cue_renamed"
}
```

### Step 15: Volume Control
```javascript
{
    stepNumber: 15,
    title: "Volume Control",
    uiTarget: "Volume",
    position: "right",
    overlayText: "Click on the Volume column to adjust cue volume. You can set it from 0 (silent) to 200 (double volume). 100 is the original file volume.\n\nTry adjusting the volume of one of your cues.",
    userAction: "click_element",
    successTrigger: "volume_changed"
}
```

### Step 16: Rename and Renumber Cue
```javascript
{
    stepNumber: 16,
    title: "Rename and Renumber Cue",
    uiTarget: "Cue #",
    position: "right",
    overlayText: "Click on the Cue Label column and name it \"Cue\".\n\nThen click on the Cue # column and type in 2 then OK.\n\nClick Next when done.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 17: Reorder Cues
```javascript
{
    stepNumber: 17,
    title: "Reorder Cue",
    uiTarget: "Next",
    position: "below",
    overlayText: "We need to move the cue to the right place. Click on Reorder cues and use the arrow keys to place it between \"Theatre\" and \"Player\". Then press Done.\n\nClick Next when finished.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 18: Autofollow Tag
```javascript
{
    stepNumber: 18,
    title: "Notice the Autofollow tag",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Did you notice the → got added to the cue name? And the row changed to a light gray? Why is that?\n\nLook at the cue above it. The Auto Follow column is marked. That means when the first cue completes, the next cue will automatically Follow it and play by itself. Press the Green play button on Cue 1 and see it in action.\n\nClick Next when ready.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 19: Add Autofollow
```javascript
{
    stepNumber: 19,
    title: "Add autofollow",
    uiTarget: "Next",
    position: "below",
    overlayText: "Let's add an AutoFollow to Cue 2.\n\nFind the row with Cue 2 and the column labeled \"Autofollow\". Click inside the box so it looks like ☑.\n\nNotice that the Autofollow indicator arrow has been added to the name of cue 3.\n\nClick Next when done.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 20: Play Sequence
```javascript
{
    stepNumber: 20,
    title: "Play the sequence",
    uiTarget: "GO button",
    position: "centered",
    overlayText: "Let's try the first sequence now. If you aren't on Cue 1, you can press Jump to First, type in 1 then press Jump, or just move with the up and down arrow keys.\n\nThen Press Go to hear the sequence.",
    userAction: "click_element",
    successTrigger: "audio_playing"
}
```

### Step 21: Trim Audio
```javascript
{
    stepNumber: 21,
    title: "Trim audio",
    uiTarget: "Next",
    position: "left",
    overlayText: "Let's see if we can make that sound a little better by getting rid of the pauses between the words. The easiest way is with the Waveform Editor. Click the ~ button for Cue 1.\n\nClick Next when you have the waveform editor open.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 22: Waveform Editor
```javascript
{
    stepNumber: 22,
    title: "Waveform editor Intro",
    uiTarget: "Next",
    position: "left",
    overlayText: "We're now in the Waveform editor. You can click on the Help button here to see what the other buttons do.\n\nBut first, let's trim that silence! Use your mouse and click right where you first start seeing soundwaves. Do you see a white line? That's called the playhead.\n\nNow find Trim Start, and click the \"Set at Playhead\" button below it. You've just trimmed the silence at the beginning of the sound. Press the blue Play Selection button and compare it with Play Full.\n\nNow do the same process but trim the silence at the end. You can zoom in with the magnifying glass for more precision.\n\nWhen you're done, click \"Apply Changes\". Click Next when finished.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 23: Test Trimmed Audio
```javascript
{
    stepNumber: 23,
    title: "Test Trimmed Audio",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Make sure you are on Cue 1 and press GO. Notice that Cue #2 autofollows much quicker now. You can edit Cues 2 and 3 in the waveform editor if you like.\n\nClick Next when done.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 24: Music and Fade Cues
```javascript
{
    stepNumber: 24,
    title: "Music",
    uiTarget: "Add Fade Cue",
    position: "centered",
    overlayText: "Let's look at cue 4. Go ahead and play a bit of it. You can use the Show Control GO button or the cue row Play button.\n\nWe don't need to listen to the whole song, so let's add a fade out cue. Click the yellow \"Add Fade Cue\", found on the top bar.",
    userAction: "click_element",
    successTrigger: "add_fade_cue_button"
}
```

### Step 25: Configure Fade Cue
```javascript
{
    stepNumber: 25,
    title: "Rename and move",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Do you know what to do now?\n\n  *Change the Cue # to 5.\n  *Rename it to \"Fade Drama Queen Dreams\".\n  *Click Target to assign the fade to Cue 4.\n\n  *Finally, click on Reorder Cues and move it to the right place in the cue stack.\n\nThen press GO on Cue 4 to play the sound, and GO again to run the fade.\n\nClick Next to go to the next step.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 26: Fade In
```javascript
{
    stepNumber: 26,
    title: "Notice Fade In",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Did you notice the fade happened? Fade cues gradually change the volume of their target cue over time. You can set fade duration and target volume.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 27: Add Another Audio Cue
```javascript
{
    stepNumber: 27,
    title: "Add another audio cue",
    uiTarget: "Add Audio Cue",
    position: "below",
    overlayText: "Let's add one more audio cue to demonstrate pan effects. Click 'Add Audio Cue' again.",
    userAction: "click_element",
    successTrigger: "audio_cue_added"
}
```

### Step 28: Select Audio File
```javascript
{
    stepNumber: 28,
    title: "Select audio file",
    uiTarget: "Next",
    position: "bottom-center",
    overlayText: "Notice in the audio selection window that we can see how our sounds are organized by folders. These examples use the root folder, Music/ and SFX/.\n\nClick Target to open the file selector. Pick any sound, but maybe SFX/bbc_footsteps-_07074187.mp3 from the BBC Sound Effects Library is a good choice.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 29: Pan Controls
```javascript
{
    stepNumber: 29,
    title: "Pan to the left",
    uiTarget: "Next",
    position: "below",
    overlayText: "Go ahead and play the sound.\n\nNow let's make it move from left to right. First step is to click the Pan column for this cue.\n\nClick Next when you see the \"Set Pan\" window.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 30: Set Pan Left
```javascript
{
    stepNumber: 30,
    title: "Set pan left",
    uiTarget: "Next",
    position: "centered",
    overlayText: "In the Pan window, drag the slider all the way to the left (-100) or type -100 in the text box. This will make the sound come entirely from the left speaker.\n\nClick 'Set Pan' when done, then Click Next.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 31: Test Pan
```javascript
{
    stepNumber: 31,
    title: "Test pan",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Play the cue and listen to how it only comes from the left speaker. Pan values range from -100 (full left) to +100 (full right), with 0 being center.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 32: Save Project
```javascript
{
    stepNumber: 32,
    title: "Save Project",
    uiTarget: "Save Show",
    position: "below",
    overlayText: "Now let's save your work! Click 'Save Show' to save your cue list. This creates a .tcp file that contains all your cue settings.",
    userAction: "click_element",
    successTrigger: "project_saved"
}
```

### Step 33: Hotkeys
```javascript
{
    stepNumber: 33,
    title: "Hotkeys",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Theatre Cue Player supports keyboard shortcuts for live performance:\n\n• Spacebar: GO (play next cue)\n• ← →: Navigate between cues\n• S: STOP all audio\n• P: PAUSE current cue\n• Numbers 1-9: Jump to cue number\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 34: Loop Settings
```javascript
{
    stepNumber: 34,
    title: "Loop Settings",
    uiTarget: "Loop",
    position: "right",
    overlayText: "Click on the Loop column for any cue to set how many times it repeats. 1 = play once (default), 2 = play twice, 999 = infinite loop.\n\nTry setting a cue to loop 3 times.",
    userAction: "click_element",
    successTrigger: "loop_set"
}
```

### Step 35: Fade Times
```javascript
{
    stepNumber: 35,
    title: "Fade Times",
    uiTarget: "Fade In",
    position: "right",
    overlayText: "The Fade In and Fade Out columns let you gradually change volume at the start and end of cues. Values are in seconds.\n\nTry setting a 2-second fade in on a cue.",
    userAction: "click_element",
    successTrigger: "fade_time_set"
}
```

### Step 36: Auto Continue
```javascript
{
    stepNumber: 36,
    title: "Auto Continue vs Auto Follow",
    uiTarget: "Next",
    position: "centered",
    overlayText: "Two ways to chain cues automatically:\n\n• Auto Follow: Next cue starts when current cue finishes\n• Auto Continue: Next cue starts immediately when current cue begins\n\nBoth are useful for different performance needs.\n\nClick Next to continue.",
    userAction: "click_next",
    successTrigger: ""
}
```

### Step 37: Exit Edit Mode
```javascript
{
    stepNumber: 37,
    title: "Show Mode",
    uiTarget: "Exit Edit",
    position: "below",
    overlayText: "We've made our edits and saved our cue file. Let's go into Show Mode so we don't accidentally change any cues.\n\nClick Exit Edit.",
    userAction: "click_element",
    successTrigger: "edit_mode_inactive"
}
```

### Step 38: Tutorial Complete
```javascript
{
    stepNumber: 38,
    title: "End Tutorial",
    uiTarget: "Next",
    position: "centered",
    overlayText: "You've made it through the tutorial. We've hit the major elements. Please explore the parts we didn't cover, like Auto Continue, Delay, Loops, and Renumber Cues.\n\nClick Next to end the tutorial.",
    userAction: "click_next",
    successTrigger: ""
}
```

## Implementation Requirements

### Draggable Tutorial Windows

```css
.tutorial-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #eee;
    cursor: move;
    user-select: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
}

.tutorial-header:active {
    cursor: grabbing;
}
```

```javascript
initializeDragging() {
    const header = this.content.querySelector('.tutorial-header');
    if (!header) return;
    
    let isDragging = false;
    let startX, startY, startLeft, startTop;
    
    const handleStart = (e) => {
        isDragging = true;
        const clientX = e.type === 'touchstart' ? e.touches[0].clientX : e.clientX;
        const clientY = e.type === 'touchstart' ? e.touches[0].clientY : e.clientY;
        
        startX = clientX;
        startY = clientY;
        startLeft = parseInt(window.getComputedStyle(this.content).left, 10) || 0;
        startTop = parseInt(window.getComputedStyle(this.content).top, 10) || 0;
        
        e.preventDefault();
    };
    
    const handleMove = (e) => {
        if (!isDragging) return;
        
        const clientX = e.type === 'touchmove' ? e.touches[0].clientX : e.clientX;
        const clientY = e.type === 'touchmove' ? e.touches[0].clientY : e.clientY;
        
        const deltaX = clientX - startX;
        const deltaY = clientY - startY;
        
        let newLeft = startLeft + deltaX;
        let newTop = startTop + deltaY;
        
        // Keep within viewport bounds
        const rect = this.content.getBoundingClientRect();
        const viewportWidth = window.innerWidth;
        const viewportHeight = window.innerHeight;
        
        newLeft = Math.max(0, Math.min(newLeft, viewportWidth - rect.width));
        newTop = Math.max(0, Math.min(newTop, viewportHeight - rect.height));
        
        this.content.style.left = newLeft + 'px';
        this.content.style.top = newTop + 'px';
        
        e.preventDefault();
    };
    
    const handleEnd = () => {
        isDragging = false;
    };
    
    // Mouse events
    header.addEventListener('mousedown', handleStart);
    document.addEventListener('mousemove', handleMove);
    document.addEventListener('mouseup', handleEnd);
    
    // Touch events
    header.addEventListener('touchstart', handleStart, { passive: false });
    document.addEventListener('touchmove', handleMove, { passive: false });
    document.addEventListener('touchend', handleEnd);
}
```

### Tutorial Completion Handler

```javascript
completeTutorial() {
    this.isActive = false;
    tutorialActive = false;
    this.overlay.classList.remove('active');
    this.clearHighlights();
    
    // Hide the tutorial window
    this.overlay.style.display = 'none';
    this.content.style.display = 'none';
    
    alert('🎉 Congratulations! You\'ve completed the Theatre Cue Player tutorial.\n\nYou\'re now ready to manage audio cues like a pro!');
    
    localStorage.setItem('tcp_tutorial_completed', 'true');
    console.log('Tutorial completed');
}
```

### Success Triggers

```javascript
const successTriggers = {
    "folder_selected": () => project && project.cues && project.cues.length > 0,
    "edit_mode_active": () => editMode === true,
    "audio_cue_added": () => project && project.cues && project.cues.length > 0,
    "cue_renamed": () => true, // Detect when cue name changes
    "volume_changed": () => true, // Detect when volume is modified
    "project_saved": () => true, // Detect when save operation completes
    "audio_playing": () => playingCues.size > 0,
    "edit_mode_inactive": () => editMode === false,
    "add_fade_cue_button": () => true, // Detect Add Fade Cue button click
    "fade_time_set": () => true, // Detect fade time modification
    "loop_set": () => true, // Detect loop setting change
};
```

### UI Target Selectors

```javascript
const uiTargetSelectors = {
    "Tutorial Button": "#tutorialButton",
    "Load Show Folder button": "button[onclick*='loadShowFolder']",
    "Show Info": ".show-info",
    "Edit Mode": "button[onclick*='editMode']",
    "Add Audio Cue": "button[onclick*='addAudioCue']",
    "Add Fade Cue": "button[onclick*='addFadeCue']",
    "Save Show": "button[onclick*='saveShow']",
    "GO button": "#goButton",
    "Exit Edit": "button[onclick*='exitEdit']",
    "Cue Label": ".cue-label",
    "Cue #": ".cue-number",
    "Volume": ".volume-control",
    "Pan": ".pan-control",
    "Loop": ".loop-control",
    "Fade In": ".fade-in-control",
    "Fade Out": ".fade-out-control",
    "Next": ".tutorial-next"
};
```

## Integration Notes

1. **Preserve Base Functionality**: All tutorial code should be additive and not interfere with the core Theatre Cue Player functionality.

2. **Responsive Design**: Tutorial windows must work on desktop, tablet, and Chromebook devices.

3. **State Management**: Tutorial state should be stored in localStorage to prevent showing completed tutorials.

4. **Error Handling**: Include proper error handling for missing UI elements or user actions.

5. **Performance**: Tutorial should not impact application performance when inactive.

6. **Accessibility**: Tutorial windows should be keyboard accessible and screen reader friendly.

## File Structure

- Main tutorial code should be embedded in the HTML file
- Tutorial steps array should be easily modifiable
- CSS styles should be included in the main stylesheet
- Success triggers should be customizable based on application changes

This documentation provides all necessary information to implement the complete tutorial system in any updated version of Theatre Cue Player while maintaining compatibility with the base application functionality.