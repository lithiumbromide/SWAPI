---
title: "ReleaseSelectionAccess Method (ICompositeCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICompositeCurveFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICompositeCurveFeatureData)

Releases access to the selections that define this composite curve.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICompositeCurveFeatureData

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

See [CompositeCurveFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CompositeCurveFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ICompositeCurveFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICompositeCurveFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) ir [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ICompositeCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData.html)
[ICompositeCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
