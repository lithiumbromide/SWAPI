---
title: "ICWFrequencyStudyOptions Interface Properties"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions_properties"
member: ""
kind: "properties"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_properties.html"
---

# ICWFrequencyStudyOptions Interface Properties

For a list of all members of this type, see [ICWFrequencyStudyOptions members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CheckDecouple | Gets and sets whether to decouple the mixed free body modes of this frequency study. |
| Property | CheckFlowPressure | Obsolete. Superseded by ICWFrequencyStudyOptions::CheckFlowPressure2 . |
| Property | CheckFlowPressure2 | Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file. |
| Property | CheckRunAsLegacy | Obsolete. Superseded by ICWFrequencyStudyOptions::CheckRunAsLegacy2 . |
| Property | CheckRunAsLegacy2 | Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file. |
| Property | DefinedReferencePressure | Gets or sets the reference pressure offset to subtract from imported pressure values. |
| Property | EMail | Obsolete. Superseded by ICWFrequencyStudyOptions::Email2 . |
| Property | EMail2 | Gets or sets whether to email notifications during simulations. |
| Property | EMailInterval | Gets or sets the time interval for sending email notifications during simulations. |
| Property | EMailIntervalUnit | Gets or sets the units of time for ICWFrequencyStudyOptions::EMailInterval . |
| Property | EMailTimebased | Obsolete. Superseded by ICWFrequencyStudyOptions::EmailTimebased2 . |
| Property | EMailTimebased2 | Gets or sets whether to send time-based email notifications during simulations. |
| Property | EMailTo | Gets or sets the recipient of email notifications. |
| Property | FlowPressureFile | Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads. |
| Property | FlowTemperatureFile | Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures. |
| Property | FrequencyCapOption | Gets or sets the frequency cap for this frequency study. |
| Property | FrequencyCapValue | Gets or sets the frequency cap value for this frequency study. |
| Property | LowerBoundFrequency | Gets or sets the frequency to which frequencies closest are calculated in this frequency study. |
| Property | NoOfFrequencies | Gets or sets the number of frequencies in this frequency study. |
| Property | Options | Gets or sets the frequency option for this frequency study. |
| Property | ReferencePressureOption | Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values. |
| Property | ResultFolder | Gets or sets the path name of the folder that contains results of this frequency study. |
| Property | SolverType | Gets or sets the solver type associated with this frequency study. |
| Property | ThermalResults | Gets or sets the source of temperatures in this frequency study. |
| Property | ThermalStudyName | Gets or sets the thermal study used to obtain temperature values. |
| Property | TimeStep | Gets or sets the time step for which to import a single temperature from a transient thermal study. |
| Property | UpperBoundFrequency | Gets or sets the upper-bound frequency for this frequency study. |
| Property | UseLowerBoundFrequency | Obsolete. Superseded by ICWFrequencyStudyOptions::UseLowerBoundFrequency2 . |
| Property | UseLowerBoundFrequency2 | Gets or sets whether to calculate frequencies closest to a specified frequency in this frequency study. |
| Property | UseSoftSpring | Obsolete. Superseded by ICWFrequencyStudyOptions::UseSoftSpring2 . |
| Property | UseSoftSpring2 | Gets or sets whether to use soft springs to stabilize the model in this frequency study. |

[Top](#topBookmark)

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
