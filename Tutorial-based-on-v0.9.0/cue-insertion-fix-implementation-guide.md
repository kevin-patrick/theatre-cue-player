# Cue Insertion Fix Implementation Guide

## Overview
This document provides complete instructions to fix the cue insertion bug in Theatre Cue Player v0.9.0 where new cues were always being added to the bottom of the cue list instead of after the selected cue.

## Problem Description
- **Issue**: When users select a cue and click "Add Audio Cue" or "Add Fade Cue", the new cue is always inserted at the bottom of the cue list instead of after the selected cue
- **Root Cause**: The `selectedCueIndex` variable was always -1 because navigation methods (arrow keys, jump functions) only updated `currentCueIndex` (for playback position) but not `selectedCueIndex` (for insertion position)
- **Additional Issue**: The autonumbering system didn't handle decimal increments properly for tight insertion scenarios

## Files to Modify
- Main application file (typically `index.html` or similar containing the Theatre Cue Player JavaScript)

## Implementation Steps

### Step 1: Add selectedCueIndex Variable Declaration
Find the global variable declarations section and ensure `selectedCueIndex` is declared:

```javascript
let selectedCueIndex = -1; // Add this if it doesn't exist
```

### Step 2: Update Arrow Key Navigation Function
Find the `navigateCue` function and modify it to update both indices:

**Find this code:**
```javascript
function navigateCue(direction) {
    const newIndex = Math.max(0, Math.min(project.cues.length - 1, currentCueIndex + direction));
    if (newIndex !== currentCueIndex) {
        currentCueIndex = newIndex;
        updateCueJumpDisplay();
        updateUI();
        
        const cue = project.cues[currentCueIndex];
        if (cue) {
            showTemporaryFeedback(`Selected: ${cue.cueNumber} - ${cue.label}`);
        }
    }
}
```

**Replace with:**
```javascript
function navigateCue(direction) {
    const newIndex = Math.max(0, Math.min(project.cues.length - 1, currentCueIndex + direction));
    if (newIndex !== currentCueIndex) {
        currentCueIndex = newIndex;
        selectedCueIndex = newIndex; // Also update selectedCueIndex for cue insertion
        updateCueJumpDisplay();
        updateUI();
        
        const cue = project.cues[currentCueIndex];
        if (cue) {
            showTemporaryFeedback(`Selected: ${cue.cueNumber} - ${cue.label}`);
        }
    }
}
```

### Step 3: Update Jump Functions
Find and update both jump functions:

**Find `jumpToCue` function and add selectedCueIndex update:**
```javascript
function jumpToCue() {
    const input = document.getElementById('cueJumpInput');
    const targetCueNumber = input.value.trim();
    
    if (!targetCueNumber) return;
    
    const cueIndex = project.cues.findIndex(c => c.cueNumber === targetCueNumber);
    if (cueIndex !== -1) {
        currentCueIndex = cueIndex;
        selectedCueIndex = cueIndex; // Add this line
        updateCueJumpDisplay();
        updateUI();
        // ... rest of function
    }
}
```

**Find `jumpToFirst` function and add selectedCueIndex update:**
```javascript
function jumpToFirst() {
    if (project.cues.length > 0) {
        currentCueIndex = 0;
        selectedCueIndex = 0; // Add this line
        updateCueJumpDisplay();
        updateUI();
        console.log('Jumped to first cue');
    } else {
        console.log('No cues available to jump to');
    }
}
```

### Step 4: Add/Update Row Selection Function
Add or update the `selectCueForInsertion` function:

```javascript
function selectCueForInsertion(index) {
    selectedCueIndex = index;
    updateUI(); // Refresh to show selection highlighting
}
```

### Step 5: Update Table Generation for Row Selection
Find the HTML table generation code (usually in a function that builds the cue table). Update the table row to include onclick for selection:

**Find the `<tr>` tag generation and ensure it has:**
```javascript
<tr class="${rowClasses.join(' ')}" onclick="selectCueForInsertion(${i})" style="cursor: pointer;">
```

**Ensure individual `<td>` cells only call their edit functions in edit mode:**
```javascript
<td onclick="${editMode ? `editField('cueNumber', '${cue.cueNumber}'); event.stopPropagation();` : ''}">${cue.cueNumber}</td>
<td onclick="${editMode ? `editField('label', '${cue.cueNumber}'); event.stopPropagation();` : ''}">${displayLabel}</td>
```

**Key principle**: In edit mode, cells should call their edit function AND `event.stopPropagation()`. In non-edit mode, cells should have empty onclick, letting the row onclick handle selection.

### Step 6: Add CSS for Selection Highlighting
Ensure these CSS rules exist for showing selected cues:

```css
.cue-table tr.selected-cue {
    background: rgba(255, 193, 7, 0.3) !important;
    border: 2px solid #ffc107;
}

.cue-table tr.selected-cue td {
    background: rgba(255, 193, 7, 0.2);
    border-color: #ffc107;
}
```

### Step 7: Update Table Row Class Logic
In the table generation, ensure the row gets the `selected-cue` class:

```javascript
let rowClasses = [];
if (isCurrentCue) rowClasses.push('current-cue');
if (i === selectedCueIndex) rowClasses.push('selected-cue'); // Add this line
if (isPlaying) rowClasses.push('playing');
// ... other row class logic
```

### Step 8: Implement Smart Autonumbering System

**Find and replace the `getSmartCueNumber` function:**

```javascript
function getSmartCueNumber(insertAfterIndex) {
    // If no cues exist, start with 1
    if (project.cues.length === 0) {
        return '1';
    }
    
    // If inserting at the end (no selection or selected last cue)
    if (insertAfterIndex === -1 || insertAfterIndex >= project.cues.length - 1) {
        // Find highest existing cue number and add 1
        let maxCueNumber = 0;
        for (const cue of project.cues) {
            const cueNum = parseFloat(cue.cueNumber);
            if (!isNaN(cueNum) && cueNum > maxCueNumber) {
                maxCueNumber = cueNum;
            }
        }
        return (Math.floor(maxCueNumber) + 1).toString();
    }
    
    // Get the cue we're inserting after
    const afterCue = project.cues[insertAfterIndex];
    const afterNumber = parseFloat(afterCue.cueNumber);
    
    // If the cue number isn't a valid number, fall back to end insertion
    if (isNaN(afterNumber)) {
        return getSmartCueNumber(-1);
    }
    
    // Try next integer first
    const nextInteger = Math.floor(afterNumber) + 1;
    if (!cueNumberExists(nextInteger.toString())) {
        return nextInteger.toString();
    }
    
    // Handle decimal increments intelligently
    const baseNumber = Math.floor(afterNumber);
    
    // Check if we're inserting after a decimal cue (like 5.1)
    if (afterNumber % 1 !== 0) {
        // We're after a decimal cue like 5.1
        const currentDecimalPart = Math.round((afterNumber % 1) * 10) / 10; // Extract .1 from 5.1
        
        // Check if the immediate next decimal exists (5.1 → check if 5.2 exists)
        const nextDecimal = currentDecimalPart + 0.1;
        if (nextDecimal < 1) {
            const nextNumber = baseNumber + nextDecimal;
            if (!cueNumberExists(nextNumber.toFixed(1))) {
                // Next decimal is free, use it (5.1 → 5.2)
                return nextNumber.toFixed(1);
            } else {
                // Next decimal is taken, use higher precision for tight insertion (5.1 → 5.11)
                for (let i = 1; i <= 9; i++) {
                    const tightDecimal = afterNumber + (i / 100);
                    if (!cueNumberExists(tightDecimal.toFixed(2))) {
                        return tightDecimal.toFixed(2);
                    }
                }
            }
        }
        
        // If that didn't work, try other decimal slots (5.3, 5.4, etc.)
        for (let i = 2; i <= 9; i++) {
            const nextDecimal = currentDecimalPart + (i / 10);
            if (nextDecimal < 1) {
                const newNumber = baseNumber + nextDecimal;
                if (!cueNumberExists(newNumber.toFixed(1))) {
                    return newNumber.toFixed(1);
                }
            }
        }
        
        // Final fallback: try more precise decimals
        for (let i = 1; i <= 99; i++) {
            const preciseDecimal = currentDecimalPart + (i / 100);
            if (preciseDecimal < 1) {
                const newNumber = baseNumber + preciseDecimal;
                if (!cueNumberExists(newNumber.toFixed(2))) {
                    return newNumber.toFixed(2);
                }
            }
        }
    } else {
        // We're after a whole number like 6
        // First try X.1 format
        const firstDecimal = baseNumber + 0.1;
        if (!cueNumberExists(firstDecimal.toFixed(1))) {
            return firstDecimal.toFixed(1);
        }
        
        // Then try X.2, X.3, X.4, etc.
        for (let i = 2; i <= 9; i++) {
            const decimalNumber = baseNumber + (i / 10);
            if (!cueNumberExists(decimalNumber.toFixed(1))) {
                return decimalNumber.toFixed(1);
            }
        }
        
        // Finally try X.01, X.02, X.03, etc. for very tight insertion
        for (let i = 1; i <= 99; i++) {
            const decimalNumber = baseNumber + (i / 100);
            const numberStr = decimalNumber.toFixed(2);
            if (!cueNumberExists(numberStr)) {
                return numberStr;
            }
        }
    }
    
    // Fallback: add to end
    return getSmartCueNumber(-1);
}

function cueNumberExists(cueNumber) {
    return project.cues.some(cue => cue.cueNumber === cueNumber);
}
```

## Autonumbering Logic Explanation

The smart autonumbering system works as follows:

### After Whole Numbers (e.g., cue 6):
1. Try next integer: 6 → 7
2. If taken, try decimals: 6 → 6.1 → 6.2 → 6.3...
3. If 6.1-6.9 taken, try precise: 6 → 6.01 → 6.02...

### After Decimal Numbers (e.g., cue 6.1):
1. Try next decimal: 6.1 → 6.2
2. If 6.2 exists, use tight insertion: 6.1 → 6.11 → 6.12...
3. If tight insertion full, try other decimals: 6.1 → 6.3 → 6.4...

### Tight Insertion Examples:
- Between 5.1 and 5.2: Creates 5.11, 5.12, 5.13...
- Between 6 and 7 when 6.1 exists: Creates 6.2, 6.3, 6.4...

## Testing Checklist

After implementation, test these scenarios:

1. **Arrow key navigation**: Use ↑/↓ keys, then add cue - should insert after selected cue
2. **Jump functions**: Use "Jump to First" or type cue number and "Jump", then add cue
3. **Row clicking**: Click table rows (in non-edit mode), then add cue
4. **Basic numbering**: Select cue 5, add cue → should create cue 6
5. **Decimal start**: Have cues 1-6, select cue 5, add cue → should create 5.1
6. **Decimal sequence**: Have cue 6.1, select it, add cue → should create 6.2
7. **Tight insertion**: Have cues 5.1 and 5.2, select 5.1, add cue → should create 5.11

## Common Issues and Solutions

1. **Selection highlighting not working**: Check CSS rules are applied and `selected-cue` class is added to rows
2. **Still inserting at bottom**: Verify `selectedCueIndex` is being updated in all navigation functions
3. **Cell clicks not working in edit mode**: Ensure `event.stopPropagation()` is called in edit mode cell clicks
4. **Autonumbering not working**: Verify `cueNumberExists` function is implemented and `getSmartCueNumber` is called correctly

## File Backup Recommendation

Before implementing these changes, create a backup of your main application file. The changes affect core navigation and cue creation functionality.