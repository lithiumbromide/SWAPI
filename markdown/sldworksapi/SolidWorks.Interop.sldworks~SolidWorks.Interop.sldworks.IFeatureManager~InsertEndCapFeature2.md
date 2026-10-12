---
title: "InsertEndCapFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertEndCapFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertEndCapFeature2.html"
---

# InsertEndCapFeature2 Method (IFeatureManager)

Inserts an end cap feature using the specified end faces of a structural member.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEndCapFeature2( _
   ByVal Depth As System.Double, _
   ByVal BIsGivenOffset As System.Boolean, _
   ByVal BIsChamfer As System.Boolean, _
   ByVal OffsetValue As System.Double, _
   ByVal WallThicknessRatio As System.Double, _
   ByVal ChamferValue As System.Double, _
   ByVal Faces As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Depth As System.Double
Dim BIsGivenOffset As System.Boolean
Dim BIsChamfer As System.Boolean
Dim OffsetValue As System.Double
Dim WallThicknessRatio As System.Double
Dim ChamferValue As System.Double
Dim Faces As System.Object
Dim value As Feature

value = instance.InsertEndCapFeature2(Depth, BIsGivenOffset, BIsChamfer, OffsetValue, WallThicknessRatio, ChamferValue, Faces)
```

### C#

```csharp
Feature InsertEndCapFeature2(
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.object Faces
)
```

### C++/CLI

```cpp
Feature^ InsertEndCapFeature2(
   System.double Depth,
   System.bool BIsGivenOffset,
   System.bool BIsChamfer,
   System.double OffsetValue,
   System.double WallThicknessRatio,
   System.double ChamferValue,
   System.Object^ Faces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Depth`: Depth of the end cap
- `BIsGivenOffset`: True if end cap is offset, false if not
- `BIsChamfer`: True if end cap feature is chamfered, false If not
- `OffsetValue`: Value by which to offset the end cap
- `WallThicknessRatio`: Wall thickness ratio
- `ChamferValue`: Angle of the chamfer
- `Faces`: Array of [Face2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) objects

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertEndCapFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertEndCapFeature2.html).

## Examples

[Insert Weldment Features (VBA)](Insert_Weldment_Features_Example_VB.htm)
[Insert Weldment Features (VB.NET)](Insert_Weldment_Features_Example_VBNET.htm)
[Insert Weldment Features (C#)](Insert_Weldment_Features_Example_CSharp.htm)

## Remarks

Call [IFeatureManager::InsertEndCapFeature3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertEndCapFeature3.html) if you want to pre-select the faces to end-cap in the graphics area.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
