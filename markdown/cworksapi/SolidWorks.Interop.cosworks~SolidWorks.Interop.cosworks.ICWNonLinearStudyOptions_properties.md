---
title: "ICWNonLinearStudyOptions Interface Properties"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions_properties"
member: ""
kind: "properties"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_properties.html"
---

# ICWNonLinearStudyOptions Interface Properties

For a list of all members of this type, see [ICWNonLinearStudyOptions members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CheckFlowPressure | Obsolete. Superseded by ICWNonLinearStudyOptions::CheckFlowPressure2 . |
| Property | CheckFlowPressure2 | Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file. |
| Property | CheckRunAsLegacy | Obsolete. Superseded by ICWNonLinearStudyOptions::CheckRunAsLegacy2 . |
| Property | CheckRunAsLegacy2 | Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file. |
| Property | CheckUseTempFromThermalStudy | Obsolete. Superseded by ICWNonLinearStudyOptions::CheckUseTempFromThermalStudy2 . |
| Property | CheckUseTempFromThermalStudy2 | Gets or sets whether to use the temperature from the corresponding time of a transient thermal analysis at each nonlinear time step. |
| Property | ContactPenaltyStiffnessScaleFactor | Gets or sets the surface-to-surface contact penalty stiffness scale factor for this nonlinear study. |
| Property | ContactPenaltyStiffnessScaleFactorGlobalDefault | Gets or sets the global default value of the surface-to-surface contact penalty stiffness scale factor for this nonlinear study. |
| Property | ControlMethodType | Gets or sets the type of control method. |
| Property | DefinedReferencePressure | Gets or sets the reference pressure offset to subtract from imported pressure values. |
| Property | EMail | Obsolete. Superseded by ICWNonLinearStudyOptions::Email2 . |
| Property | EMail2 | Gets or sets whether to email notifications during simulations. |
| Property | EMailInterval | Gets or sets the time interval for sending email notifications during simulations. |
| Property | EMailIntervalUnit | Gets or sets the units of time for ICWNonLinearStudyOptions::EMailInterval . |
| Property | EMailTimebased | Obsolete. Superseded by ICWNonLinearStudyOptions::EmailTimebased2 . |
| Property | EMailTimebased2 | Gets or sets whether to send email notifications during simulations. |
| Property | EMailTo | Gets or sets the recipient of email notifications. |
| Property | EndTime | Gets or sets the end time (solution time) for the nonlinear study. |
| Property | FixedTimeIncrement | Gets or sets a value for the solution increment. |
| Property | FlowPressureFile | Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads. |
| Property | FlowTemperatureFile | Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures. |
| Property | IntegrationMethodType | Gets or sets the type of numerical integration method. |
| Property | IterativeMethodType | Gets or sets the type of iterative solution method. |
| Property | KeepBoltPreStress | Obsolete. Superseded by ICWNonLinearStudyOptions::KeepBoltPreStress2 . |
| Property | KeepBoltPreStress2 | Gets or sets whether to keep bolt pre-stress. |
| Property | ReferencePressureOption | Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values. |
| Property | ResultFolderPath | Gets or sets the path name of the folder that stores the results of this study. |
| Property | SaveDataForRestartingAnalysis | Obsolete. Superseded by ICWNonLinearStudyOptions::SaveDataForRestartingAnalysis2 . |
| Property | SaveDataForRestartingAnalysis2 | Gets or sets whether to save data for restarting the analysis. |
| Property | SolverType | Gets or sets the solver type associated with the study. |
| Property | StartTime | Gets the start time. |
| Property | ThermalResults | Gets or sets the source of temperatures in this nonlinear study. |
| Property | ThermalStudyName | Gets or sets the thermal study used to obtain temperature values. |
| Property | TimeIncrement | Gets or sets the fixed time increment. |
| Property | TimeStep | Gets or sets the time step at which to import a single temperature from a transient thermal study. |
| Property | UseLargeDisplacement | Obsolete. Superseded by ICWNonLinearStudyOptions::UseLargeDisplacement2 . |
| Property | UseLargeDisplacement2 | Gets or sets whether to use large displacement formulation. |
| Property | UseLargeStrain | Obsolete. Superseded by ICWNonLinearStudyOptions::UseLargeStrain2 . |
| Property | UseLargeStrain2 | Gets or sets whether to use large strain formulation. |
| Property | UseUpdateLoadDirection | Obsolete. Superseded by ICWNonLinearStudyOptions::UseUpdateLoadDirection2 . |
| Property | UseUpdateLoadDirection2 | Gets or sets whether the direction of the applied load (uniform press, normal force, torque) is updated at every solution step with deflection. |

[Top](#topBookmark)

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
