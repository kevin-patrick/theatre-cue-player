# Theatre Cue Player Manual
**Version 0.3.29 | June 17, 2025**

*Designed by Kevin Patrick, Technical Theatre Arts Director, Blinn College-Brenham Campus*
*Released under the MIT License*

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Loading Audio Files and Cues](#loading-audio-files-and-cues)
3. [Creating and Editing Cues](#creating-and-editing-cues)
4. [Running Your Show](#running-your-show)
5. [Advanced Features](#advanced-features)
6. [Help System](#help-system)
7. [File Management](#file-management)
8. [Troubleshooting](#troubleshooting)
9. [Technical Requirements](#technical-requirements)

---

## Getting Started

### What is Theatre Cue Player?
Theatre Cue Player is a professional audio cue management system designed specifically for live theatre productions. It allows you to organize, edit, and play audio cues with precise control over timing, volume, and transitions.

### First Launch
When you open Theatre Cue Player, you'll see the welcome screen with three main options:

- **Load Audio Folder** - Select a folder containing your audio files
- **Load Cue File** - Load an existing cue list (.json file)
- **New Project** - Start with an empty cue list

### Key Benefits
- **Professional Features**: Fade in/out, auto-continue, auto-follow
- **Flexible File Management**: Audio files and cue lists can be stored separately
- **Safe Operation**: Help mode prevents accidental button presses
- **Theatre-Friendly**: Designed by theatre professionals for theatre use

---

## Loading Audio Files and Cues

### Loading Audio Files
1. Click **Load Audio Folder**
2. Select a folder containing your audio files
3. Supported formats: MP3, WAV, OGG, M4A, AAC, FLAC, WMA
4. All audio files in the folder become available for assignment to cues

**Tip**: Keep your audio library in a shared location so multiple shows can access the same files.

### Loading Existing Cues
1. Click **Load Cue File**
2. Select a `.json` cue file from any location
3. The system will automatically try to connect cues to available audio files
4. Missing audio files will be marked for easy identification

### Starting Fresh
1. Click **New Project**
2. Creates an empty cue list
3. You can load audio files later using **Load Audio Folder**
4. Automatically enters Edit Mode for immediate cue creation

### File Management Flexibility
- **Audio files** and **cue files** are completely independent
- Use the same audio library for multiple shows
- Save show-specific cue files anywhere you want
- Perfect for schools with shared audio resources

---

## Creating and Editing Cues

### Entering Edit Mode
Click **Edit Mode** in the header to enable editing features. When active:
- Button changes to **Exit Edit** (yellow/warning color)
- Additional editing buttons appear
- Cue fields become clickable for editing
- Reorder arrows appear in the table

### Adding Audio Cues
1. Enter Edit Mode
2. Click **Add Audio Cue**
3. A new cue appears with default settings
4. Click the **Target** field to assign an audio file
5. Edit other properties by clicking on them

### Adding Fade Cues
1. Enter Edit Mode
2. Click **Add Fade Cue**
3. Automatically targets the most recent audio cue
4. Set fade duration and target volume
5. Use for fade-outs, crossfades, or volume changes

### Editing Cue Properties
Click any field to edit (when in Edit Mode):

- **Cue #**: Unique identifier (can use decimals like 2.5)
- **Cue Label**: Descriptive name for the cue
- **Target**: Audio file (for audio cues) or target cue (for fade cues)
- **Auto Continue**: Start next cue immediately when this one begins
- **Delay**: Wait time before cue starts (in seconds)
- **Start Time**: Where to begin in the audio file
- **Fade In**: Gradual volume increase from silence
- **Volume**: Playback level (0-110%, where 110% is boosted)
- **End Time**: Where to stop in the audio file
- **Fade Out**: Gradual volume decrease before ending
- **Auto Follow**: Start next cue when this one finishes

### Reordering Cues
- Use **↑** and **↓** arrows to move cues up or down
- Available in Edit Mode only
- Automatically adjusts the "Next Cue" pointer

### Deleting Cues
1. Click **Delete Cue**
2. Select cue from dropdown list
3. Confirm deletion
4. Stops cue if currently playing

---

## Running Your Show

### Show Control Basics
The **Show Control** section contains your primary playback tools:

- **GO**: Play the next cue and advance the sequence
- **STOP ALL**: Immediately stop all playing audio
- **HELP**: Toggle help mode on/off

### The GO Button
- Plays the cue shown in "Next Cue"
- Automatically advances to the next cue
- Handles both audio cues and fade cues
- This is your main button during a show

### Manual Controls
Each cue has individual control buttons:
- **▶ (Play)**: Start this specific cue
- **⧵ (Fade)**: Fade this cue to silence over 5 seconds
- **■ (Stop)**: Immediately stop this cue

### Next Cue Display
- Shows which cue will play when you press GO
- Type a cue number to jump to that cue
- Use **Jump** to go to the entered cue
- **Jump to First** resets to the beginning

### Visual Feedback
Cues change appearance to show their status:
- **Blue highlight**: Current/next cue in sequence
- **Green background**: Currently playing
- **Yellow background**: Currently fading

---

## Advanced Features

### Auto Continue vs Auto Follow

**Auto Continue**:
- Starts the next cue immediately when this one begins
- Creates layered/overlapping audio
- Perfect for background music under sound effects

**Auto Follow**:
- Starts the next cue when this one finishes
- Creates seamless transitions
- Perfect for sequential music or scene changes

### Volume Control
- Range: 0-110%
- 100% = normal playback level
- 110% = boosted (approximately double volume)
- Uses logarithmic scaling for natural sound perception

### Fade Cues
Fade cues provide dynamic volume control:
- **Target**: Which audio cue to affect
- **Duration**: How long the fade takes
- **Volume**: Target volume level (often 0% for fade-outs)
- **Delay**: Wait before starting the fade

### S-Curve Fading
All fades use professional S-curve algorithms:
- Sounds more natural than linear fades
- Faster change at the beginning and end
- Smoother transition in the middle
- Used in professional audio equipment

### Timing Controls
- **Start/End Time**: Play only portions of audio files
- **Fade In/Out**: Professional-quality fade transitions
- **Delay**: Precise timing control for complex sequences

---

## Help System

### Accessing Help
1. Click **HELP** in Show Control
2. Yellow question marks (❓) appear throughout the interface
3. Click any ❓ to see help for that feature
4. Help text appears in the Show Control area

### Safe Exploration
When Help Mode is active:
- All action buttons are disabled
- Only help icons and EXIT HELP work
- Safe to explore without accidentally triggering cues
- Click **EXIT HELP** to return to normal operation

### Learning the Interface
- Every column header has a help icon
- All buttons include detailed explanations
- Help text uses theatre terminology, not technical jargon

---

## File Management

### Saving Your Work
- **Save Cue File As...**: Save cues to a named .json file
- Choose descriptive names like "spring-musical-cues.json"
- Files can be saved anywhere on your computer
- Include show name, date, or version in filename

### Project Organization
**Recommended Structure**:
```
Audio Library/
├── Music/
├── Sound Effects/
└── Voice/

Show Files/
├── spring-musical-cues.json
├── fall-play-cues.json
└── competition-cues.json
```

### Backup Strategy
- Regularly save your cue files
- Keep audio files in a shared, backed-up location
- Save multiple versions during development
- Test cue files on performance computer before show

### Sharing Projects
- Send .json cue files to other operators
- Ensure they have access to the same audio files
- Consider packaging audio files if sharing with other schools
- Document any special requirements or notes

---

## Troubleshooting

### Audio Files Not Loading
**Problem**: "No audio files found" or files won't play
**Solutions**:
- Check file formats (use MP3 or WAV for best compatibility)
- Ensure files aren't corrupted
- Try a different folder location
- Check browser audio permissions

### Cues Show as "Missing"
**Problem**: Cue status shows "missing" or "error"
**Solutions**:
- Reload the audio folder
- Check that audio filenames match exactly
- Ensure audio files haven't been moved or renamed
- Try reassigning the audio file manually

### Audio Doesn't Start
**Problem**: GO button pressed but no sound
**Solutions**:
- Check computer volume settings
- Click anywhere to ensure browser has audio permission
- Verify audio file is assigned to the cue
- Try playing the cue manually with ▶ button

### Performance Issues
**Problem**: Lag or stuttering during playback
**Solutions**:
- Use smaller audio files when possible
- Close other browser tabs and applications
- Ensure adequate computer memory
- Consider using local files instead of network storage

### Browser Compatibility
**Problem**: Features don't work properly
**Solutions**:
- Use Chrome, Firefox, or Safari (latest versions)
- Enable JavaScript in browser settings
- Clear browser cache and reload
- Avoid Internet Explorer (not supported)

---

## Technical Requirements

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux
- **Browser**: Chrome 88+, Firefox 85+, Safari 14+, Edge 88+
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: Varies based on audio file size
- **Audio**: Built-in or external audio interface

### Audio File Recommendations
- **Format**: MP3 (320kbps) or WAV (44.1kHz/16-bit)
- **Size**: Keep individual files under 50MB for best performance
- **Organization**: Use clear, descriptive filenames
- **Backup**: Maintain copies of all audio files

### Network Considerations
- **Local Files**: Fastest performance, recommended for shows
- **Network Storage**: Acceptable for rehearsals, test during tech
- **Internet Streaming**: Not recommended for live performance
- **Backup**: Always have local copies available

### Show Computer Setup
- **Dedicated Use**: Close unnecessary applications during performance
- **Audio Interface**: Test all outputs before show
- **Volume Levels**: Set consistent levels during tech rehearsal
- **Backup Plan**: Have alternative playback method ready

### Browser Settings
- **Allow Audio**: Grant permission for audio playback
- **Full Screen**: Press F11 for distraction-free operation
- **Zoom Level**: Use 100% zoom for proper interface scaling
- **Extensions**: Disable ad blockers and audio modifiers

---

## Best Practices

### Preparation
1. **Tech Rehearsal**: Test every cue with actual audio levels
2. **Backup Files**: Keep copies of both audio and cue files
3. **Documentation**: Print cue list as backup reference
4. **Sound Check**: Verify all outputs before audience arrives

### During Performance
1. **Focus**: Minimize distractions on the computer
2. **Visual Cues**: Watch for status changes in the interface
3. **Manual Control**: Use individual cue buttons if needed
4. **Stay Calm**: STOP ALL button is always available

### After Performance
1. **Save Changes**: Update cue file with any modifications
2. **Notes**: Document any issues for future reference
3. **Archive**: Keep final cue files for remount or reference
4. **Feedback**: Share experiences with other users

---

## Support and Updates

### Getting Help
- **Email**: kevin.patrick@blinn.edu
- **Help System**: Use built-in help for feature explanations
- **Documentation**: Refer to this manual for detailed procedures

### Reporting Issues
When reporting problems, please include:
- Theatre Cue Player version number
- Browser type and version
- Description of the issue
- Steps to reproduce the problem
- Audio file formats being used

### Version History
- **0.3.29**: Current beta release
- Features separated loading system
- Professional credits and manual
- Enhanced help system

---

## Glossary

**Audio Cue**: A cue that plays an audio file
**Auto Continue**: Feature that starts the next cue immediately when current cue begins
**Auto Follow**: Feature that starts the next cue when current cue finishes
**Cue**: A single audio event or fade instruction
**Fade Cue**: A cue that changes the volume of a playing audio cue
**GO Button**: Main button used to advance through cues during performance
**Help Mode**: Safe mode for exploring interface without triggering actions
**S-Curve Fade**: Professional audio fade algorithm for natural-sounding transitions

---

*This manual covers Theatre Cue Player version 0.3.29. For the latest updates and support, contact kevin.patrick@blinn.edu*