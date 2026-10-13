---
title: "IInterferenceDetectionMgr Interface Members"
project: "SOLIDWORKS API Help"
interface: "IInterferenceDetectionMgr_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html"
---

# IInterferenceDetectionMgr Interface Members

The following tables list the members exposed by [IInterferenceDetectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CreateFastenersFolder | Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners. |
| Property | IgnoreHiddenBodies | Gets or sets whether to ignore hidden bodies during interference detection. |
| Property | IncludeMultibodyPartInterferences | Gets or sets whether to report interferences between bodies within multibody parts. |
| Property | MakeInterferingPartsTransparent | Gets or sets whether to display the components of the selected interference in transparent mode. |
| Property | NonInterferingComponentDisplay | Gets or sets the mode to display non-interfering components. |
| Property | ShowIgnoredInterferences | Gets or sets whether to show ignored interferences. |
| Property | TreatCoincidenceAsInterference | Gets or sets whether to treat coincident entities as interference. |
| Property | TreatSubAssembliesAsComponents | Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported. |
| Property | UseTransform | Gets or sets whether to use transforms in interference detection. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | Done | Stops the interference detection. |
| Method | ExportResults | Saves interference detection results to a file. |
| Method | GetComponentsAndTransforms | Gets the interfering components and their transforms. |
| Method | GetComponentsTransformInterference | Calculates and gets the interfering components for the specified components and math transform. |
| Method | GetComponentsTransformInterferenceCount | Calculates and gets the number of interfering components for the specified components and math transform. |
| Method | GetInterferenceComponentCount | Calculates and gets the number of interfering components. |
| Method | GetInterferenceComponents | Calculates and gets the interfering components. |
| Method | GetInterferenceCount | Calculates and gets the number of interferences. |
| Method | GetInterferences | Calculates and gets the interferences. |
| Method | IGetComponentsTransformInterference | Calculates and gets the interfering components for the specified components and math transform. |
| Method | IGetInterferenceComponents | Calculates and gets the interfering components. |
| Method | IGetInterferences | Calculates and gets the interferences. |
| Method | SetComponentsAndTransforms | Sets the interfering components and their transforms. |

[Top](#topBookmark)

## See Also

[IInterferenceDetectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IInterference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference.html)
[IModeler::CheckInterferenceBetweenTwoBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CheckInterferenceBetweenTwoBodies.html)
