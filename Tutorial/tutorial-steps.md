# Theatre Cue Player Tutorial - Complete Instruction Manual

This document provides a comprehensive guide for implementing the Theatre Cue Player tutorial system in updated versions. Each step contains exact overlay text, UI targets, positioning, and interaction requirements.

## Tutorial System Structure

- **Total Steps**: 38 interactive steps
- **Base Version**: 0.8.3
- **Tutorial Flow**: Linear progression with specific user actions and success triggers

## Complete Step-by-Step Instructions

### Step 1: Begin Tutorial
- **Title**: "Begin Tutorial"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
This is the Tutorial version of Theatre Cue Player, based on version 0.8.3.

Please use the most recent project version for class and production.

This tutorial will guide you through 40 interactive steps to learn all features of Theatre Cue Player.

If a tutorial window is blocking your view, you can drag it to a different location by grabbing the top bar
```

### Step 2: Load Show Folder
- **Title**: "Load Show Folder"
- **UI Target**: "Load Show Folder button"
- **Position**: "left"
- **User Action**: "click_element"
- **Success Trigger**: "show_loaded"
- **Overlay Text**: 
```
Click here to select the folder with the files and folder structure you downloaded. Make sure they are uncompressed.

Select the folder that includes Sample-Cue-Sheet.json and the audio files (some in folders).

NOTE you will not see the files when you click to select a folder.
```

### Step 3: Introduction
- **Title**: "Introduction"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
When you open a Show Folder, you begin in Show Mode. All edit functions are disabled. Let's look around and see what's here.
```

### Step 4: Show Title
- **Title**: "Show Title"
- **UI Target**: "Show Info"
- **Position**: "below"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Here's the title for your show and the filename for the cue file. We use the file format ".json" to store show and cue data.
```

### Step 5: Top bar
- **Title**: "Top bar"
- **UI Target**: "Help"
- **Position**: "below"
- **User Action**: "click_element"
- **Success Trigger**: "help_mode_active"
- **Overlay Text**: 
```
Here you can open a context-sensitive help menu, read the short manual, run a tutorial on playback, and enter Edit Mode.

Click the HELP button to activate context-sensitive help throughout the interface.
```

### Step 6: Explore Help Mode
- **Title**: "Explore Help Mode"
- **UI Target**: "Exit Help"
- **Position**: "bottom-center"
- **User Action**: "click_element"
- **Success Trigger**: "help_mode_inactive"
- **Overlay Text**: 
```
Great! Now you can see yellow question marks throughout the interface. Click on some question marks to see context-sensitive help content appear in the sidebar.

Click "Exit Help" to continue the tutorial.
```

### Step 7: Show Control
- **Title**: "Show Control"
- **UI Target**: "Next"
- **Position**: "bottom-center"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
The GO button is how you play and progress through the cues. You can also use the spacebar for GO.

Try playing some cues using GO, STOP ALL, FADE ALL, Jump, and Jump to First buttons. Notice the cue that is playing turns green and shows in "Currently Playing".

Click Next when ready to continue.
```

### Step 8: Jump to First
- **Title**: "Jump to First"
- **UI Target**: "Next"
- **Position**: "bottom-center"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Now that you've gone through some cues, it's time to move back to the first cue. Just click Jump to First, or type in 1 and click Jump.

Click Next to continue the tutorial.
```

### Step 9: Actions
- **Title**: "Actions"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Each individual cue also has playback controls. Sometimes we want to play cues out of order. Sometimes we click "GO" before it was the right time.

In Theatre Cue Player, you can stop or fade out individual cues without having to stop the whole show.

Try playing a longer cue with its individual green play button, then fade it out with the yellow slash. Click Next after you've experimented with this.
```

### Step 10: Keyboard Shortcuts
- **Title**: "Keyboard Shortcuts"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Theatre Cue Player utilizes many of the standard cue playback keyboard shortcuts. Try some out, and click Next when ready to continue.
```

### Step 11: Edit Mode
- **Title**: "Edit Mode"
- **UI Target**: "Edit Mode button"
- **Position**: "below"
- **User Action**: "click_element"
- **Success Trigger**: "edit_mode_active"
- **Overlay Text**: 
```
Let's go into edit mode to add and edit sound and fade cues
```

### Step 12: Edit Mode Intro
- **Title**: "Edit Mode Intro"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Not much changed visually. We have some more buttons at top. But now every cell for every cue is editable.
```

### Step 13: Add Audio Cue
- **Title**: "Add Audio Cue"
- **UI Target**: "Add Audio Cue Button"
- **Position**: "right"
- **User Action**: "click_element"
- **Success Trigger**: "cue_added"
- **Overlay Text**: 
```
Cue 2 is missing! Let's add it. Click Add Audio Cue
```

### Step 14: Select Target File
- **Title**: "Select Target File"
- **UI Target**: "Next"
- **Position**: "bottom-center"
- **User Action**: "wait_for_condition"
- **Success Trigger**: "file_selector_opened"
- **Overlay Text**: 
```
We added a cue, but now we need to say which file to play. Click on "No File" in the Target column of the cue we just added.
```

### Step 15: Select Audio File
- **Title**: "Select Audio File"
- **UI Target**: "Next"
- **Position**: "left"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Click on the dropdown to show all the audio files available in the show folder, then select "Cue-by-ttsmaker.mp3". Click Next when you've selected the file.
```

### Step 16: Rename and Renumber Cue
- **Title**: "Rename and Renumber Cue"
- **UI Target**: "Cue #"
- **Position**: "right"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Click on the Cue Label column and name it "Cue".

Then click on the Cue # column and type in 2 then OK.

Click Next when done.
```

### Step 17: Reorder Cue
- **Title**: "Reorder Cue"
- **UI Target**: "Next"
- **Position**: "below"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
We need to move the cue to the right place. Click on Reorder cues and use the arrow keys to place it between "Theatre" and "Player". Then press Done.

Click Next when finished.
```

### Step 18: Notice the Autofollow tag
- **Title**: "Notice the Autofollow tag"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Did you notice the → got added to the cue name? And the row changed to a light gray? Why is that?

Look at the cue above it. The Auto Follow column is marked. That means when the first cue completes, the next cue will automatically Follow it and play by itself. Press the Green play button on Cue 1 and see it in action.

Click Next when ready.
```

### Step 19: Add autofollow
- **Title**: "Add autofollow"
- **UI Target**: "Next"
- **Position**: "below"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Let's add an AutoFollow to Cue 2.

Find the row with Cue 2 and the column labeled "Autofollow". Click inside the box so it looks like ☑.

Notice that the Autofollow indicator arrow has been added to the name of cue 3.

Click Next when done.
```

### Step 20: Play the sequence
- **Title**: "Play the sequence"
- **UI Target**: "GO button"
- **Position**: "centered"
- **User Action**: "click_element"
- **Success Trigger**: "audio_playing"
- **Overlay Text**: 
```
Let's try the first sequence now. If you aren't on Cue 1, you can press Jump to First, type in 1 then press Jump, or just move with the up and down arrow keys.

Then Press Go to hear the sequence.
```

### Step 21: Trim audio
- **Title**: "Trim audio"
- **UI Target**: "Next"
- **Position**: "left"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Let's see if we can make that sound a little better by getting rid of the pauses between the words. The easiest way is with the Waveform Editor. Click the ~ button for Cue 1.

Click Next when you have the waveform editor open.
```

### Step 22: Waveform editor Intro
- **Title**: "Waveform editor Intro"
- **UI Target**: "Next"
- **Position**: "left"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
We're now in the Waveform editor. You can click on the Help button here to see what the other buttons do.

But first, let's trim that silence! Use your mouse and click right where you first start seeing soundwaves. Do you see a white line? That's called the playhead.

Now find Trim Start, and click the "Set at Playhead" button below it. You've just trimmed the silence at the beginning of the sound. Press the blue Play Selection button and compare it with Play Full.

Now do the same process but trim the silence at the end. You can zoom in with the magnifying glass for more precision.

When you're done, click "Apply Changes". Click Next when finished.
```

### Step 23: Test Trimmed Audio
- **Title**: "Test Trimmed Audio"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Make sure you are on Cue 1 and press GO. Notice that Cue #2 autofollows much quicker now. You can edit Cues 2 and 3 in the waveform editor if you like.

Click Next when done.
```

### Step 24: Music
- **Title**: "Music"
- **UI Target**: "Add Fade Cue"
- **Position**: "centered"
- **User Action**: "click_element"
- **Success Trigger**: "add_fade_cue_button"
- **Overlay Text**: 
```
Let's look at cue 4. Go ahead and play a bit of it. You can use the Show Control GO button or the cue row Play button.

We don't need to listen to the whole song, so let's add a fade out cue. Click the yellow "Add Fade Cue", found on the top bar.
```

### Step 25: Rename and move
- **Title**: "Rename and move"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Do you know what to do now?

  *Change the Cue # to 5.
  *Rename it to "Fade Drama Queen Dreams".
  *Click Target to assign the fade to Cue 4.

  *Finally, click on Reorder Cues and move it to the right place in the cue stack.

Then press GO on Cue 4 to play the sound, and GO again to run the fade.

Click Next to go to the next step.
```

### Step 26: Notice Fade In
- **Title**: "Notice Fade In"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Notice that Cue 4 has an integrated fade in time of 5 seconds. If you click on the Waveform Editor for Cue 4, you can even see the fade time shown.
```

### Step 27: Pan/Balance
- **Title**: "Pan/Balance"
- **UI Target**: "Add Audio Cue Button"
- **Position**: "centered"
- **User Action**: "click_element"
- **Success Trigger**: "cue_added"
- **Overlay Text**: 
```
Let's add another cue. Press Add Audio Cue
```

### Step 28: Select audio file
- **Title**: "Select audio file"
- **UI Target**: "Next"
- **Position**: "bottom-center"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Notice in the audio selection window that we can see how our sounds are organized by folders. These examples use the root folder, Music/ and SFX/.

Click Target to open the file selector. Pick any sound, but maybe SFX/bbc_footsteps-_07074187.mp3 from the BBC Sound Effects Library is a good choice.

Click Next to continue.
```

### Step 29: Pan to the left
- **Title**: "Pan to the left"
- **UI Target**: "Next"
- **Position**: "below"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Go ahead and play the sound.

Now let's make it move from left to right. First step is to click the Pan column for this cue.

Click Next when you see the "Set Pan" window.
```

### Step 30: Set Pan
- **Title**: "Set Pan"
- **UI Target**: "-100 = all to the Left button"
- **Position**: "bottom-center"
- **User Action**: "click_element"
- **Success Trigger**: "pan_set_left"
- **Overlay Text**: 
```
In Theatre Cue Player, a sound that plays only on the left speaker is numbered -100. A sound that plays equally on both speakers is set to 0. And a sound that plays only on the right speaker is 100.

You can type in a number in the box or press the shortcut button "-100 = all to the Left". For this tutorial, click the "-100 = all to the Left" button.
```

### Step 31: Add Fade Cue
- **Title**: "Add Fade Cue"
- **UI Target**: "Next"
- **Position**: "bottom-center"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Click "Add Fade Cue" on the top bar. Set the 'Target' for the fade cue to be the footsteps cue we just added.

To make the footsteps cue sound like it is walking from left to right, we need to set the Pan for the fade all the way to the right.

But don't stop there! Fade cues default to fading the volume out over 5 seconds. Because we don't want the volume to fade, click that cell in the Volume column and type in 100.

Play through the sequence and adjust timings to what sounds best. You can add an Auto Continue to the footsteps sound cue and a delay to the fade cue. Play around!

Click Next when you are ready to continue.
```

### Step 32: Begin Hot Keys
- **Title**: "Begin Hot Keys"
- **UI Target**: "Next"
- **Position**: "left"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Let's add one more Audio Cue. This time, select the airhorn sound in the SFX folder. You can name the cue if you want. Click Next when you have that cue loaded up.
```

### Step 33: Add Hot Key
- **Title**: "Add Hot Key"
- **UI Target**: "document (whole page)"
- **Position**: "centered"
- **User Action**: "keyboard_combo"
- **Success Trigger**: "hotkey_assigned"
- **Overlay Text**: 
```
Let's make that sound a hotkey. Sometimes you have a sound that needs to play based on stage action and not necessarily in order. Hot keys are great for that.

Press and hold Shift, then press F2
```

### Step 34: Assign Hot Key
- **Title**: "Assign Hot Key"
- **UI Target**: "OK button"
- **Position**: "below"
- **User Action**: "click_element"
- **Success Trigger**: "hotkey_confirmed"
- **Overlay Text**: 
```
Type in the cue number for the air horn to assign it, then press OK
```

### Step 35: Play the Hot Key
- **Title**: "Play the Hot Key"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
Press the F2 button on your keyboard. Are you hearing the air horn? Click Next when you're done being a DJ.
```

### Step 36: Saving the Cue File
- **Title**: "Saving the Cue File"
- **UI Target**: "Save Cue File As"
- **Position**: "centered"
- **User Action**: "click_element"
- **Success Trigger**: "file_saved"
- **Overlay Text**: 
```
Now it's time to save our cue file. Depending on your browser and computer settings, the cue file might save only to your Downloads folder or it might open a folder picker. Pay attention to where the file is going so you can move it into your show folder. Click on it now, name your show, and save your cue file.
```

### Step 37: Show Mode
- **Title**: "Show Mode"
- **UI Target**: "Exit Edit"
- **Position**: "below"
- **User Action**: "click_element"
- **Success Trigger**: "edit_mode_inactive"
- **Overlay Text**: 
```
We've made our edits and saved our cue file. Let's go into Show Mode so we don't accidentally change any cues.

Click Exit Edit.
```

### Step 38: End Tutorial
- **Title**: "End Tutorial"
- **UI Target**: "Next"
- **Position**: "centered"
- **User Action**: "click_next"
- **Success Trigger**: ""
- **Overlay Text**: 
```
You've made it through the tutorial. We've hit the major elements. Please explore the parts we didn't covered, like Auto Continue, Delay, Loops, and Renumber Cues.

Click Next to end the tutorial.
```

## UI Target Selector Mapping

The tutorial system uses the following selector mappings to identify UI elements:

```javascript
const uiTargetSelectors = {
    "Tutorial Button": "#tutorialButton",
    "Load Show Folder button": "button[onclick*='loadShowFolder'], .btn:contains('Load Show Folder')", 
    "Show Info": ".show-info",
    "Header Controls": ".header-controls",
    "Help": "#helpToggle",
    "Exit Help": "#helpToggle",
    "GO button": "button[onclick*='goNext']",
    "Jump to First": "button[onclick*='jumpToFirst']",
    "Edit Mode button": "button[onclick*='editModeFromLanding'], button[onclick*='toggleEditMode']",
    "Add Audio Cue Button": "button[onclick*='addAudioCue']", 
    "Add Fade Cue": "button[onclick*='addFadeCue']",
    "Save Cue File As": "button[onclick*='saveCueFile']",
    "Exit Edit": "button[onclick*='toggleEditMode']",
    "Reorder Cues": "button[onclick*='openReorderModal']",
    "Target button for the newly added cue": ".edit-field[data-field='target']:last-of-type",
    "No File Target Cell": "[onclick*='selectFile'], .target-field, .edit-field[data-field='target'], td[onclick*='selectFile'], .cue-table tbody tr:last-child td, .cue-table tbody tr:last-child .target, button[onclick*='selectFile']",
    "--Select Audio File--": "option:contains('Select Audio File')",
    "Cue-by-ttsmaker.mp3": "option:contains('Cue-by-ttsmaker.mp3')",
    "Cue Label": ".edit-field[data-field='label']:last-of-type",
    "Cue #": ".edit-field[data-field='cueNumber']:last-of-type", 
    "Green play button for cue 1": ".cue-table tbody tr:first-child .play-btn",
    "Autofollow button for cue 2": ".cue-table tbody tr:nth-child(2) .autofollow-btn",
    "Waveform editor for Cue 1": ".cue-table tbody tr:first-child .waveform-icon",
    "Apply Changes": "button[onclick*='applyWaveformChanges']",
    "Select an audio file": "option:contains('Select')",
    "Pan": ".edit-field[data-field='pan']:last-of-type",
    "-100 = all to the Left button": "button:contains('-100')",
    "OK button": "button:contains('OK')",
    "document (whole page)": "body",
    "Next": "next_button"
};
```

## Success Triggers

The tutorial system uses these success condition checks:

- **tutorial_started**: () => tutorialActive
- **show_loaded**: Checks for loaded project with cues and visible UI
- **help_mode_active**: () => helpMode
- **help_mode_inactive**: () => !helpMode
- **edit_mode_active**: () => editMode
- **edit_mode_inactive**: () => !editMode
- **cue_added**: () => project.cues.length > previousCueCount
- **file_saved**: () => currentFileName !== 'No file loaded'
- **file_selector_opened**: Checks for file selector DOM element
- **audio_playing**: () => playingCues.size > 0
- **hotkey_assigned**: () => hotkeyAssignments.size > 0
- **pan_set_left**: () => true (simplified check)
- **hotkey_confirmed**: () => true

## Special Overlay Modes

The tutorial implements different overlay interaction modes:

1. **Normal Mode**: Full overlay with limited interaction
2. **Help Exploration Mode** (Step 6): Transparent overlay, full interactivity
3. **Selective Button Mode** (Steps 7-10): Transparent overlay, specific buttons clickable
4. **Spotlight Mode** (Steps 11, 13, 17): Highlighted target elements
5. **Next-Only Mode** (Step 12): Only tutorial Next button clickable
6. **Free Interaction Mode** (Steps 14-16): Transparent overlay, allow free interaction

## Implementation Notes

1. **Version Adaptation**: Update version references from 0.8.3 to current version
2. **File References**: Update sample file names and paths as needed
3. **UI Element Mapping**: Verify all UI target selectors match current interface
4. **Success Condition Logic**: Adapt success triggers to current application state management
5. **Keyboard Shortcuts**: Ensure keyboard combinations (Shift+F2) work with current event handling
6. **Audio File Examples**: Update sample audio file names to match current tutorial assets
7. **Drag Functionality**: Maintain tutorial window dragging capability
8. **Responsive Positioning**: Ensure tutorial positioning works across different screen sizes

This instruction manual provides the complete framework for implementing the Theatre Cue Player tutorial in updated versions while maintaining the exact educational flow and user experience.