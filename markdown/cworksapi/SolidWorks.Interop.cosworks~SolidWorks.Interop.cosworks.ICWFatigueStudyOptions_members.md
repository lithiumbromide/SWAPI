---
title: "ICWFatigueStudyOptions Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFatigueStudyOptions_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions_members.html"
---

# ICWFatigueStudyOptions Interface Members

The following tables list the members exposed by [ICWFatigueStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | ComputingAlternatingStressOption | Gets or sets the stress type used to calculate alternating stress. |
| Property | ConstantAmplitudeEventInteractionOption | Gets or sets the interaction between constant amplitude fatigue events. |
| Property | EMail | Obsolete. Superseded by ICWFatigueStudyOptions::Email2 . |
| Property | EMail2 | Gets or sets whether to email notifications during simulations. |
| Property | EMailInterval | Gets or sets the time interval for sending email notifications during simulations. |
| Property | EMailIntervalUnit | Gets or sets the units of time for ICWFatigueStudyOptions::EMailInterval . |
| Property | EMailTimebased | Obsolete. Superseded by ICWFatigueStudyOptions::EmailTimebased2 . |
| Property | EMailTimebased2 | Gets or sets whether to send email notifications during simulations. |
| Property | EMailTo | Gets or sets the recipient of email notifications. |
| Property | FatigueStrengthReductionFactor | Gets or sets the fatigue strength reduction factor to use when reading S-N curve data. |
| Property | LoadingEventCount | Gets the number of loading events in the fatigue study. |
| Property | MeanStressCorrectionOption | Gets or sets the mean stress correction method to use in calculating alternating stresses. |
| Property | RandomVibrationComputationalMethod | Gets or sets the random vibration computational method. |
| Property | ResultFolder | Gets or sets the folder for the results of the fatigue study. |
| Property | ShellFace | Gets or sets the shell face on which fatigue analysis is performed. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | AddFatigueEventForConstantAmplitude | Adds a fatigue event to a linear dynamic constant amplitude study. |
| Method | AddFatigueEventForHarmonic | Adds a fatigue event to a linear dynamic harmonic study. |
| Method | AddFatigueEventForRandomVibration | Adds a fatigue event to a linear dynamic random vibration study. |
| Method | AddFatigueEventForVariableAmplitude | Adds a fatigue event to a linear dynamic variable amplitude study. |
| Method | DeleteFatigueEvent | Deletes the specified fatigue event. |
| Method | GetFatigueEvent | Gets the specified fatigue event. |
| Method | GetInfiniteLifeSettings | Obsolete. Superseded by ICWFatigueStudyOptions::GetInfiniteLifeSettings2 . |
| Method | GetInfiniteLifeSettings2 | Gets the infinite life settings of the fatigue study. |
| Method | GetVariableAmplitudeEventOptions | Gets the options for variable amplitude fatigue events. |
| Method | SetInfiniteLifeSettings | Obsolete. Superseded by ICWFatigueStudyOptions::SetInfiniteLifeSettings2 . |
| Method | SetInfiniteLifeSettings2 | Sets the infinite life settings of the fatigue study. |
| Method | SetVariableAmplitudeEventOptions | Sets the options for variable amplitude fatigue events. |

[Top](#topBookmark)

## See Also

[ICWFatigueStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFatigueStudyOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
