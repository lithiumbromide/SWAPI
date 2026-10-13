---
title: "IClearanceVerificationMgr Interface Members"
project: "SOLIDWORKS API Help"
interface: "IClearanceVerificationMgr_members"
member: ""
kind: "members"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr_members.html"
---

# IClearanceVerificationMgr Interface Members

The following tables list the members exposed by [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html).

## Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | CheckClearanceBetween | Gets or sets the type of clearance check: between selected items or between selected items and the rest of the assembly. |
| Property | IgnoreClearanceEqualToSpecifiedValue | Gets or sets whether to ignore clearances equal to or greater than IClearanceVerificationMgr::GetMinimumAcceptableClearance . |
| Property | TreatSubAssembliesAsComponents | Gets or sets whether to treat subassemblies as single components for clearance verification. |

[Top](#topBookmark)

## Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | CalculateClearances | Runs a clearance check of selected assembly components and/or faces. |
| Method | GetComponentsOrFacesToCheck | Gets the components and/or faces for which to check clearance. |
| Method | GetMinimumAcceptableClearance | Gets the minimum acceptable clearance value. |
| Method | SetComponentsOrFacesToCheck | Sets the components or faces for which to check clearances. |
| Method | SetMinimumAcceptableClearance | Sets the minimum acceptable clearance value. |

[Top](#topBookmark)

## See Also

[IClearanceVerificationMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)
