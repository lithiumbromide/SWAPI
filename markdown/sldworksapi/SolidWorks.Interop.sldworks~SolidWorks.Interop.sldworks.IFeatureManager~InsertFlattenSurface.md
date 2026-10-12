---
title: "InsertFlattenSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFlattenSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface.html"
---

# InsertFlattenSurface Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertFlattenSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFlattenSurface( _
   ByVal AccuracyFactor As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim AccuracyFactor As System.Integer
Dim value As Feature

value = instance.InsertFlattenSurface(AccuracyFactor)
```

### C#

```csharp
Feature InsertFlattenSurface(
   System.int AccuracyFactor
)
```

### C++/CLI

```cpp
Feature^ InsertFlattenSurface(
   System.int AccuracyFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AccuracyFactor`: 10 >= Accuracy of flattened triangle mesh >= 1; 1 is highest accuracy

### Return Value

Surface-flatten [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertFlattenSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFlattenSurface.html).

## Remarks

| Before calling this method, select... | By calling IModelDocExtension::SelectByID2 with Mark... |
| --- | --- |
| Faces or surfaces to flatten | 1 |
| Anchor point from which to flatten | 16 |
| Edges to guide the shape and length of the flattened surface | 2 |

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
