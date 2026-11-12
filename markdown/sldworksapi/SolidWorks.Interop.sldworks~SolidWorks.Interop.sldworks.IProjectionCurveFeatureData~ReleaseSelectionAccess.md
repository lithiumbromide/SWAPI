---
title: "ReleaseSelectionAccess Method (IProjectionCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IProjectionCurveFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IProjectionCurveFeatureData)

Releases access to the selections that created this projected curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IProjectionCurveFeatureData

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

See [ProjectionCurveFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ProjectionCurveFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IProjectionCurveFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionCurveFeatureData~AccessSelections.html) and [IProjectionCurveFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IProjectionCurveFeatureData~IAccessSelections2.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.html)
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
