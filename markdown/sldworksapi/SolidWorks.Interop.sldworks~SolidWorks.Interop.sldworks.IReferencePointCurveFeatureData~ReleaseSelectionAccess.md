---
title: "ReleaseSelectionAccess Method (IReferencePointCurveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IReferencePointCurveFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IReferencePointCurveFeatureData)

Releases access to the selections that define this reference-point curve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IReferencePointCurveFeatureData

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

See [ReferencePointCurveFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ReferencePointCurveFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [IReferencePointCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html) examples.

## Remarks

[IReferencePointCurveFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IReferencePointCurveFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IReferencePointCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData.html)
[IReferencePointCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
