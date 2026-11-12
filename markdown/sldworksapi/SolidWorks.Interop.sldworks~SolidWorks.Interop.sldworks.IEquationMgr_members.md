---
title: "IEquationMgr Interface Members"
project: "SOLIDWORKS API Help"
interface: "IEquationMgr_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html"
---

# IEquationMgr Interface Members

The following tables list the members exposed by [IEquationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | AngularEquationUnits | Gets or sets the angular units used in equations. |
| Property | AutomaticRebuild | Gets or sets whether to automatically rebuild after modifications. |
| Property | AutomaticSolveOrder | Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results. |
| Property | Disabled | Gets or sets whether to disable the specified equation in the model. |
| Property | Equation | Gets or sets the equation at the specified index. |
| Property | FilePath | Gets or sets the path for an exported equation text ( .txt ) file. |
| Property | GlobalVariable | Gets whether the equation at the specified index is a global variable. |
| Property | LinkToFile | Gets or sets whether the equation is linked to an exported equation text ( .txt ) file. |
| Property | Status | Gets the status of the last equation that was executed. |
| Property | Suppression | Obsolete as of SOLIDWORKS 2014 and later. |
| Property | Value | Gets the value of the equation at the specified index. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Add | Obsolete. Superseded by IEquationMgr::Add2 . |
| Method | Add2 | Adds an equation at the specified index. |
| Method | Add3 | Adds an equation at the specified index for the specified configurations. |
| Method | ChangeSuppressionForAllConfigurations | Changes the suppression state of the specified equation in all configurations. |
| Method | ChangeSuppressionForConfiguration | Changes the suppression state of an equation in the specified configuration. |
| Method | Delete | Deletes the equation at the specified index. |
| Method | EvaluateAll | Evaluates all equations. |
| Method | GetConfigurationOption | Gets the configuration option for the equation at the specified index. |
| Method | GetCount | Gets the number of equations in the model. |
| Method | GetDisabledEquationCount | Gets the number of disabled equations in the model. |
| Method | IAdd3 | Adds an equation at the specified index for the specified configurations. |
| Method | ISetEquationAndConfigurationOption | Modifies the equation at the specified index for the specified configurations. |
| Method | SetEquationAndConfigurationOption | Modifies the equation at the specified index for the specified configurations. |
| Method | UpdateValuesFromExternalEquationFile | Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary. |

[Top](#topBookmark)

## See Also

[IEquationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
