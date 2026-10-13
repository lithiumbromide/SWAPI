---
title: "InsertGussetFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertGussetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGussetFeature.html"
---

# InsertGussetFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertGussetFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertGussetFeature3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGussetFeature( _
   ByVal Depth As System.Double, _
   ByVal DirType As System.Short, _
   ByVal LocType As System.Short, _
   ByVal BIsProfile As System.Boolean, _
   ByVal ProfileD1 As System.Double, _
   ByVal ProfileD2 As System.Double, _
   ByVal ProfileD3 As System.Double, _
   ByVal ProfileAngle As System.Double, _
   ByVal ProfileD4 As System.Double, _
   ByVal BOffset As System.Boolean, _
   ByVal DProfileOffset As System.Double, _
   ByVal CrvIndex As System.Integer, _
   ByVal BReverseDir As System.Boolean, _
   ByVal BReverseFace As System.Boolean, _
   ByVal BUseLenDim As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Depth As System.Double
Dim DirType As System.Short
Dim LocType As System.Short
Dim BIsProfile As System.Boolean
Dim ProfileD1 As System.Double
Dim ProfileD2 As System.Double
Dim ProfileD3 As System.Double
Dim ProfileAngle As System.Double
Dim ProfileD4 As System.Double
Dim BOffset As System.Boolean
Dim DProfileOffset As System.Double
Dim CrvIndex As System.Integer
Dim BReverseDir As System.Boolean
Dim BReverseFace As System.Boolean
Dim BUseLenDim As System.Boolean
Dim value As Feature

value = instance.InsertGussetFeature(Depth, DirType, LocType, BIsProfile, ProfileD1, ProfileD2, ProfileD3, ProfileAngle, ProfileD4, BOffset, DProfileOffset, CrvIndex, BReverseDir, BReverseFace, BUseLenDim)
```

### C#

```csharp
Feature InsertGussetFeature(
   System.double Depth,
   System.short DirType,
   System.short LocType,
   System.bool BIsProfile,
   System.double ProfileD1,
   System.double ProfileD2,
   System.double ProfileD3,
   System.double ProfileAngle,
   System.double ProfileD4,
   System.bool BOffset,
   System.double DProfileOffset,
   System.int CrvIndex,
   System.bool BReverseDir,
   System.bool BReverseFace,
   System.bool BUseLenDim
)
```

### C++/CLI

```cpp
Feature^ InsertGussetFeature(
   System.double Depth,
   System.short DirType,
   System.short LocType,
   System.bool BIsProfile,
   System.double ProfileD1,
   System.double ProfileD2,
   System.double ProfileD3,
   System.double ProfileAngle,
   System.double ProfileD4,
   System.bool BOffset,
   System.double DProfileOffset,
   System.int CrvIndex,
   System.bool BReverseDir,
   System.bool BReverseFace,
   System.bool BUseLenDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Depth`: Depth of the gusset
- `DirType`: Direction in which to extrude the gusset:

  - 0 = left side
  - 1 = center
  - 2 = right side
- `LocType`: Location of the reference plane for the sketch of the gusset:

  - 0 = start point
  - 1 = midpoint
  - 2 = end point
- `BIsProfile`: True to use a polygon profile, false to use a triangle
- `ProfileD1`: Length for [Direction 1](sldworksAPIProgGuide.chm::/Miscellaneous/FeatureManager__InsertGussetFeature_image.htm)
- `ProfileD2`: Length for [Direction 2](sldworksAPIProgGuide.chm::/Miscellaneous/FeatureManager__InsertGussetFeature_image.htm)
- `ProfileD3`: Length for [Direction 3](sldworksAPIProgGuide.chm::/Miscellaneous/FeatureManager__InsertGussetFeature_image.htm)
- `ProfileAngle`: Value for [profile angle](sldworksAPIProgGuide.chm::/Miscellaneous/FeatureManager__InsertGussetFeature_image.htm)
- `ProfileD4`: Length for [Direction 4](sldworksAPIProgGuide.chm::/Miscellaneous/FeatureManager__InsertGussetFeature_image.htm)
- `BOffset`: True to offset the reference plane for the sketch, false to not
- `DProfileOffset`: Value by which to offset the reference plane for the sketch
- `CrvIndex`: Index of the edge to use if multiple intersecting edges exist
- `BReverseDir`: If BOffset set to true, then true to reverse direction, false to not
- `BReverseFace`: Reverse ProfileD1 and ProfileD2 if triangle profile

  - or -

  Reverse ProfileD1 and ProfileD2 and reverse ProfileD3 and ProfileD4 if polygon profile
- `BUseLenDim`: True to use ProfileD4, false to use ProfileAngle

### Return Value

Pointer to the newly created [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertGussetFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertGussetFeature.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IFeatureManager::InsertGussetFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGussetFeature2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
