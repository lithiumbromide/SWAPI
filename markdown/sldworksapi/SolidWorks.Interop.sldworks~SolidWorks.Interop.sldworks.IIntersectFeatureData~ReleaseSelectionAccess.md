---
title: "ReleaseSelectionAccess Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IIntersectFeatureData)

Releases access to the selections for this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData

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

See [IntersectFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IIntersectFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did.

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
