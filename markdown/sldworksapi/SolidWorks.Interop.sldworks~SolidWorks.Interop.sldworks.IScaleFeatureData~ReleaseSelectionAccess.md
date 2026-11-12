---
title: "ReleaseSelectionAccess Method (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IScaleFeatureData)

Releases access to the selections used to define the scale feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData

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

See [ScaleFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Faces Affected By Scale Feature (VBA)](Get_Faces_Affected_by_Scale_Feature_Example_VB.htm)

## Remarks

[IScaleFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~AccessSelections.html) and [IScaleFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
