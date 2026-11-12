---
title: "ICWStaticStudyOptions Interface Members"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions_members"
member: ""
kind: "members"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html"
---

# ICWStaticStudyOptions Interface Members

The following tables list the members exposed by [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AdaptiveMethodType | Gets or sets the type of adaptive meshing to use to achieve more accurate results. |
| Property | CheckFlowPressure | Obsolete. Superseded by ICWStaticStudyOptions::CheckFlowPressure2 . |
| Property | CheckFlowPressure2 | Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file. |
| Property | CheckRunAsLegacy | Obsolete. Superseded by ICWStaticStudyOptions::CheckRunAsLegacy2 . |
| Property | CheckRunAsLegacy2 | Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file. |
| Property | ComputeFreeBodyForce | Obsolete. Superseded by ICWStaticStudyOptions::ComputeFreeBodyForce2 . |
| Property | ComputeFreeBodyForce2 | Gets or sets whether to prepare the grid force balance at every node. |
| Property | ContactPenaltyStiffnessScaleFactor | Gets or sets the contact penalty stiffness scale factor for this static study. |
| Property | ContactPenaltyStiffnessScaleFactorGlobalDefault | Gets or sets the global default for the contact penalty stiffness scale factor. |
| Property | DefinedReferencePressure | Gets or sets the reference pressure offset to subtract from imported pressure values. |
| Property | EMail | Obsolete. Superseded by ICWStaticStudyOptions::EMail2 . |
| Property | EMail2 | Gets or sets whether to email notifications during simulations. |
| Property | EMailInterval | Gets or sets the time interval for sending email notifications during simulations. |
| Property | EMailIntervalUnit | Gets or sets the units of time for ICWStaticStudyOptions::EMailInterval . |
| Property | EMailTimebased | Obsolete. Superseded by ICWStaticStudyOptions::EMailTimebased2 . |
| Property | EMailTimebased2 | Gets or sets whether to send email notifications during simulations. |
| Property | EMailTo | Gets or sets the recipient of email notifications. |
| Property | FlowPressureFile | Gets or sets the SOLIDWORKS Flow Simulation results file from which to import fluid pressure loads. |
| Property | FlowTemperatureFile | Gets or sets the SOLIDWORKS Flow Simulation results file from which to import flow temperatures. |
| Property | FrictionCoefficient | Gets or sets the value of the coefficient of friction. |
| Property | HAdaptiveAccuracyBias | Gets or sets the accuracy bias for the h-adaptive mesh iteration. |
| Property | HAdaptiveMaxNoIterations | Gets or sets the maximum number of h-adaptive mesh iterations. |
| Property | HAdaptiveMeshCoarsening | Obsolete. Superseded by ICWStaticStudyOptions::HAdaptiveMeshCoarsening2 . |
| Property | HAdaptiveMeshCoarsening2 | Gets or sets whether to allow h-adaptive mesh coarsening. |
| Property | HAdaptiveTargetAccuracy | Gets or sets the target accuracy of the h-adaptive mesh iteration. |
| Property | IgnoreClearanceForSurfaceContact | Obsolete. Superseded by ICWStaticStudyOptions::IgnoreClearanceForSurfaceContact2 . |
| Property | IgnoreClearanceForSurfaceContact2 | Gets or sets whether to consider contact conditions regardless of the initial distance between user-defined face pairs. |
| Property | IncludeGlobalFriction | Obsolete. Superseded by ICWStaticStudyOptions::IncludeGlobalFriction2 . |
| Property | IncludeGlobalFriction2 | Gets or sets whether to include global friction. |
| Property | IncludeRemarkInReport | Obsolete. Superseded by ICWStaticStudyOptions::IncludeRemarkInReport2 . |
| Property | IncludeRemarkInReport2 | Gets or sets whether to include a remark in the report. |
| Property | IncompatibleBondingOption | Gets or sets the incompatible bonding option. |
| Property | LargeDisplacement | Obsolete. Superseded by ICWStaticStudyOptions::LargeDisplacement2 . |
| Property | LargeDisplacement2 | Gets or sets whether loads are applied gradually and uniformly in steps up to their full values, performing contact iterations at every step. |
| Property | NoPenetration | Obsolete. Superseded by ICWStaticStudyOptions::NoPenetration2 . |
| Property | NoPenetration2 | Gets or sets whether to improve accuracy for no penetration contacting surfaces. |
| Property | PAdaptiveConvergenceCriteria | Gets or sets the criterion with which to determine convergence of the p-adaptive mesh iteration. |
| Property | PAdaptiveErrorLimit | Gets or sets the highest percent change in ICWStaticStudyOptions::PAdaptiveConvergenceCriteria at which to end the p-adaptive mesh iteration. |
| Property | PAdaptiveMaxIterations | Gets or sets the maximum number of p-adaptive mesh iterations. |
| Property | PAdaptiveMaxPOrder | Gets or sets the maximum polynomial order of the mesh at which to end the p-adaptive mesh iteration. |
| Property | PAdaptiveStartingPOrder | Gets or sets the polynomial order at which to start the p-adaptive mesh iteration. |
| Property | PAdaptiveStrainEnergyErrorLimit | Gets or sets the lowest relative strain energy error percent in model areas for which to apply a p-adaptive mesh iteration. |
| Property | ReferencePressureOption | Gets or sets whether to use the reference pressure offset defined in the Flow Simulation results file to subtract from imported pressure values. |
| Property | RemarkComment | Gets or sets a report remark. |
| Property | ResultFolder | Gets or sets the path name of the folder that stores the results of the study. |
| Property | SolverType | Gets or sets the solver type associated with the study. |
| Property | ThermalResults | Gets or sets the source of temperatures in this static study. |
| Property | ThermalStudyName | Gets or sets the thermal study from which to import temperature values for this static study. |
| Property | TimeStep | Gets or sets the time step at which to import a single temperature from a transient thermal study. |
| Property | UseInertialRelief | Obsolete. Superseded by ICWStaticStudyOptions::UseInertialRelief2 . |
| Property | UseInertialRelief2 | Gets or sets whether to solve using inertial relief. |
| Property | UseInPlaneEffect | Obsolete. Superseded by ICWStaticStudyOptions::UseInPlaneEffect2 . |
| Property | UseInPlaneEffect2 | Gets or sets whether to solve using inplane effect. |
| Property | UseSoftSpring | Obsolete. Superseded by ICWStaticStudyOptions::UseSoftSpring2 . |
| Property | UseSoftSpring2 | Gets or sets whether to solve using a soft spring to stabilize the model. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | GetZeroStrainTemperature | Gets the temperature at zero strain and its units. |
| Method | SetZeroStrainTemperature | Sets the temperature at zero strain and its units. |

[Top](#topBookmark)

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudyManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyManager.html)
