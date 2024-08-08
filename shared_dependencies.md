Shared Dependencies:

1. Exported Variables:
    - activeJob: The currently selected job.
    - jobList: List of all jobs.
    - materialList: List of all materials.
    - toolList: List of all tools.
    - setupTime: Time taken for machine setup.
    - runTime: Time taken for part run.
    - partStatus: Status of the part (Good, Quarantine, Scrap).
    - inspectionReport: Report of the inspection.
    - finalCheck: Final check data.

2. Data Schemas:
    - JobSchema: Schema for job data.
    - MaterialSchema: Schema for material data.
    - ToolSchema: Schema for tool data.
    - InspectionReportSchema: Schema for inspection report data.

3. DOM Element IDs:
    - jobSelect: Dropdown for job selection.
    - materialInput: Input for material data.
    - toolChecklist: Checklist for tools.
    - setupTimer: Timer for machine setup.
    - runTimer: Timer for part run.
    - partStatusButtons: Buttons for part status.
    - inspectionForm: Form for inspection report.
    - finalCheckForm: Form for final checks.
    - jobSubmitButton: Button for job submission.

4. Message Names:
    - jobSelected: Message when a job is selected.
    - materialPulled: Message when material is pulled.
    - toolsPulled: Message when tools are pulled.
    - machineSetup: Message when machine setup is done.
    - partRun: Message when part run is done.
    - inspectionDone: Message when inspection is done.
    - finalCheckDone: Message when final checks are done.
    - jobCompleted: Message when job is completed.

5. Function Names:
    - selectJob: Function to select a job.
    - pullMaterial: Function to pull material.
    - pullTools: Function to pull tools.
    - setupMachine: Function to setup machine.
    - runPart: Function to run part.
    - fillInspectionReport: Function to fill inspection report.
    - performFinalChecks: Function to perform final checks.
    - submitJob: Function to submit job.