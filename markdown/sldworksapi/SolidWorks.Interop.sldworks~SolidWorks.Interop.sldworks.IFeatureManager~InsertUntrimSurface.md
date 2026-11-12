---
title: "InsertUntrimSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertUntrimSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface.html"
---

# InsertUntrimSurface Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertUntrimSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertUntrimSurface( _
   ByVal FaceUntrimType As System.Integer, _
   ByVal EdgeUntrimType As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal BMerge As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FaceUntrimType As System.Integer
Dim EdgeUntrimType As System.Integer
Dim Distance As System.Double
Dim BMerge As System.Boolean
Dim value As Feature

value = instance.InsertUntrimSurface(FaceUntrimType, EdgeUntrimType, Distance, BMerge)
```

### C#

```csharp
Feature InsertUntrimSurface(
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge
)
```

### C++/CLI

```cpp
Feature^ InsertUntrimSurface(
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceUntrimType`: Untrim face as defined in [swFaceUntrimType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceUntrimType_e.html)
- `EdgeUntrimType`: Untrim edge as defined in [swEdgeUntrimType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeUntrimType_e.html)
- `Distance`: Distance by which to untrim surface
- `BMerge`: True to create a surface extension that merges with the original surface, false to create a new, separate surface body

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertUntrimSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertUntrimSurface.html).

## Remarks

You must preselect the face or the edges you want to untrim.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)

## Availability

SOLIDWORKS 2004 SP5, Revision Number 12.5
