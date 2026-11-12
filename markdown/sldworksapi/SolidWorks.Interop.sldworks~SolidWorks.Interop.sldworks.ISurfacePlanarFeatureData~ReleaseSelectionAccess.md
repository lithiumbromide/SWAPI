---
title: "ReleaseSelectionAccess Method (ISurfacePlanarFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfacePlanarFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISurfacePlanarFeatureData)

Releases access to the selections for this planar surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfacePlanarFeatureData

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

See [SurfacePlanarFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SurfacePlanarFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [ISurfacePlanarFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html) examples.

## Remarks

[ISurfacePlanarFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfacePlanarFeatureData~AccessSelections.html) and [ISurfacePlanarFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfacePlanarFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)
[ISurfacePlanarFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
