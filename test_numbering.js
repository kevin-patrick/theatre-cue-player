
class ProjectState {
    constructor() {
        this.cues = [
            { cueNumber: "1" },
            { cueNumber: "2" },
            { cueNumber: "3" },
            { cueNumber: "4" },
            { cueNumber: "5" }
        ];
        this.numberingMode = 'numeric';
    }

    cueExists(num) {
        return this.cues.some(c => c.cueNumber === num);
    }

    incrementPart(part) {
        const num = parseInt(part, 10);
        if (!isNaN(num)) return (num + 1).toString();
        return "B"; // Simplified alpha
    }

    calculateNextCueNumber(currentNumStr) {
        // Mocking the snippet from the file
        const isAlpha = /[A-Za-z]/.test(currentNumStr);
        if (isAlpha) return "ALPHA_PATH";

        const parts = currentNumStr.split('.');
        const lastPart = parts[parts.length - 1];
        let nextLastPart = this.incrementPart(lastPart);
        let candidate = [...parts.slice(0, -1), nextLastPart].join('.');

        console.log(`Checking candidate: ${candidate}`);

        if (!this.cueExists(candidate)) {
            // Case 1: Simple Increment
            if (!this.cueExists(candidate)) return candidate;
        }

        // Case 2: Conflict
        console.log("Conflict found (or logic skipped), trying decimal...");
        candidate = currentNumStr + ".1";
        while (this.cueExists(candidate)) {
            // Simplified loop mock
            candidate += ".1";
        }
        return candidate;
    }
}

const state = new ProjectState();
console.log("Current Cues:", state.cues.map(c => c.cueNumber));
console.log("Next for '5':", state.calculateNextCueNumber("5"));

state.cues.push({ cueNumber: "6" });
console.log("\nAfter adding 6...");
console.log("Next for '5':", state.calculateNextCueNumber("5"));
