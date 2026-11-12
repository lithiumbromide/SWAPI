---
title: "ReleaseSelectionAccess Method (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IClosedCornerFeatureData)

Releases access to selections that describe this closed corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData

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

See [ClosedCornerFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ClosedCornerFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IClosedCornerFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IClosedCornerFeatureData~AccessSelections.html) and [IClosedCornerFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IClosedCornerFeatureData~IAccessSelections2.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
