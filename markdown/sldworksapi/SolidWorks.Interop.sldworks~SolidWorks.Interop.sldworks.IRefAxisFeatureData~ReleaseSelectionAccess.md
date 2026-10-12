---
title: "ReleaseSelectionAccess Method (IRefAxisFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRefAxisFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IRefAxisFeatureData)

Releases access to the selections that define this reference axis feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IRefAxisFeatureData

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RefAxisFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~RefAxisFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Selections for Reference Axis Feature (C#)](Get_Selections_for_Reference_Axis_Feature_Example_CSharp.htm)
[Get Selections for Reference Axis Feature (VB.NET)](Get_Selections_for_Reference_Axis_Feature_Example_VBNET.htm)
[Get Selections for Reference Axis Feature (VBA)](Get_Selections_for_Reference_Axis_Feature_Example_VB.htm)

## Remarks

[IRefAxisFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxisFeatureData~AccessSelections.html) and [IRefAxisFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefAxisFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IRefAxisFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData.html)
[IRefAxisFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
