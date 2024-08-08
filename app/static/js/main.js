```javascript
let activeJob = null;
let setupTime = null;
let runTime = null;
let partStatus = null;

function selectJob(job) {
    activeJob = job;
    document.getElementById('jobSelect').value = job;
    // Emit jobSelected message
}

function pullMaterial(materialId, size, shape) {
    // Record the material pulled
    document.getElementById('materialInput').value = `${materialId}, ${size}, ${shape}`;
    // Emit materialPulled message
}

function pullTools(tools) {
    // Check off the tools pulled
    tools.forEach(tool => {
        document.getElementById(`toolChecklist-${tool}`).checked = true;
    });
    // Emit toolsPulled message
}

function setupMachine() {
    // Start the setup timer
    setupTime = Date.now();
    document.getElementById('setupTimer').start();
}

function pauseSetupMachine() {
    // Pause the setup timer and record the time
    setupTime = Date.now() - setupTime;
    document.getElementById('setupTimer').pause();
    // Emit machineSetup message
}

function runPart() {
    // Start the run timer
    runTime = Date.now();
    document.getElementById('runTimer').start();
}

function stopPart(status) {
    // Stop the run timer and record the time and status
    runTime = Date.now() - runTime;
    partStatus = status;
    document.getElementById('runTimer').stop();
    document.getElementById(`partStatusButtons-${status}`).checked = true;
    // Emit partRun message
}

function fillInspectionReport(report) {
    // Fill out the inspection report
    document.getElementById('inspectionForm').value = report;
    // Emit inspectionDone message
}

function performFinalChecks(checkData) {
    // Perform the final checks
    document.getElementById('finalCheckForm').value = checkData;
    // Emit finalCheckDone message
}

function submitJob() {
    // Submit the job
    document.getElementById('jobSubmitButton').click();
    // Emit jobCompleted message
}
```