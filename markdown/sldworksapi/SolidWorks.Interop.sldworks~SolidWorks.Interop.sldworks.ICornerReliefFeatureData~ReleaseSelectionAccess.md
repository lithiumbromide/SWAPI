---
title: "ReleaseSelectionAccess Method (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICornerReliefFeatureData)

Releases access to the selections that define this sheet metal corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData

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

See [CornerReliefFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ICornerReliefFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did.

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
