---
title: "ReleaseSelectionAccess Method (IGroundPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGroundPlaneFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IGroundPlaneFeatureData)

Releases access to the selections that define this ground plane feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IGroundPlaneFeatureData

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

See [GroundPlaneFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~GroundPlaneFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IGroundPlaneFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this ground plane feature.

Use this method to restore the rollback state if you did not modify the ground plane feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the ground plane feature.

## See Also

[IGroundPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html)
[IGroundPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
