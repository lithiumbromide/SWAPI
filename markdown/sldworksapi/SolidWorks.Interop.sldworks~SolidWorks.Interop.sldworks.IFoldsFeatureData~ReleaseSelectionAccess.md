---
title: "ReleaseSelectionAccess Method (IFoldsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFoldsFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IFoldsFeatureData)

Releases access to selections that describe this fold feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IFoldsFeatureData

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

See [FoldsFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~FoldsFeatureData~ReleaseSelectionAccess.html).

## Examples

[Insert and Access Fold Feature (C#)](Insert_and_Access_Fold_Feature_Example_CSharp.htm)
[Insert and Access Fold Feature (VB.NET)](Insert_and_Access_Fold_Feature_Example_VBNET.htm)
[Insert and Access Fold Feature (VBA)](Insert_and_Access_Fold_Feature_Example_VB.htm)

## Remarks

[IFoldsFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFoldsFeatureData~AccessSelections.html) and [IFoldsFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFoldsFeatureData~IAccessSelections2.html) put the model into a rollback state to allow access to the selections that define the fold feature.

Use this method to restore the rollback state if you did not modify the fold feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the fold feature.

## See Also

[IFoldsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData.html)
[IFoldsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
