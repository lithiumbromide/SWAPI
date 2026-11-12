---
title: "ReleaseSelectionAccess Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISurfaceTrimFeatureData)

Releases access to the selections that created this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData

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

See [SurfaceTrimFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SurfaceTrimFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [ISurfaceTrimFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html) examples.

## Remarks

[ISurfaceTrimFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~AccessSelections.html) and [ISurfaceTrimFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
