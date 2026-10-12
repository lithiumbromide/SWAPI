---
title: "ICWBucklingStudyOptions Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html"
---

# ICWBucklingStudyOptions Interface Members

The following tables list the members exposed by [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | BucklingModes | Gets or sets the number of buckling modes. |
| Property | CheckFlowPressure | Obsolete. Superseded by ICWBucklingStudyOptions::CheckFlowPressure2 . |
| Property | CheckFlowPressure2 | Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file. |
| Property | CheckRunAsLegacy | Obsolete. Superseded by ICWBucklingStudyOptions::CheckRunAsLegacy2 . |
| Property | CheckRunAsLegacy2 | Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file. |
| Property | DefinedReferencePressure | Gets or sets the reference pressure offset to subtract from imported pressure values. |
| Property | EMail | Obsolete. Superseded by ICWBucklingStudyOptions::Email2 . |
| Property | EMail2 | Gets or sets whether to email notifications during simulations. |
| Property | EMailInterval | Gets or sets the time interval for sending email notifications during simulations. |
| Property | EMailIntervalUnit | Gets or sets the units of time for ICWBucklingStudyOptions::EMailInterval . |
| Property | EMailTimebased | Obsolete. Superseded by ICWBucklingStudyOptions::EmailTimebased2 . |
| Property | EMailTimebased2 | Gets or sets whether to send time-based email notifications during simulations. |
| Property | EMailTo | Gets or sets the recipient of email notifications. |
| Property | ExtractPositiveBucklingFactorsOnly | Gets or sets whether to extract only positive buckling factors from this buckling study. |
| Property | FlowPressureFile | Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads. |
| Property | FlowTemperatureFile | Gets or sets the SOLIDWORKS Flow Simulation result file that is used to import flow temperatures. |
| Property | ReferencePressureOption | Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values. |
| Property | ResultFolder | Gets or sets the path to the folder for storing the results of the study. |
| Property | SolverType | Gets or sets the solver type. |
| Property | ThermalResults | Gets or sets the source of temperatures in this buckling study. |
| Property | ThermalStudyName | Gets or sets the thermal study used to obtain temperature values. |
| Property | TimeStep | Gets or sets the time step from which to import a single temperature from a transient thermal study. |
| Property | UseSoftSpring | Obsolete. Superseded by ICWBucklingStudyOptions::UseSoftSpring2 . |
| Property | UseSoftSpring2 | Gets or sets whether to use soft spring to stabilize the model. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetZeroStrainTemperature | Gets the reference temperature and its units at zero strain. |
| Method | SetZeroStrainTemperature | Sets the reference temperature and its units at zero strain. |

[Top](#topBookmark)

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
