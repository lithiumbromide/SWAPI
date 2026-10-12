---
title: "InsertMoveFace3 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoveFace3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace3.html"
---

# InsertMoveFace3 Method (IFeatureManager)

Moves the selected faces on a solid or surface model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoveFace3( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double, _
   ByVal TranslationParams As System.Object, _
   ByVal RotationParams As System.Object, _
   ByVal EndConditionType As System.Integer, _
   ByVal OffsetDistance As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim MoveType As System.Integer
Dim ReverseDir As System.Boolean
Dim Angle As System.Double
Dim Distance As System.Double
Dim TranslationParams As System.Object
Dim RotationParams As System.Object
Dim EndConditionType As System.Integer
Dim OffsetDistance As System.Double
Dim value As Feature

value = instance.InsertMoveFace3(MoveType, ReverseDir, Angle, Distance, TranslationParams, RotationParams, EndConditionType, OffsetDistance)
```

### C#

```csharp
Feature InsertMoveFace3(
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.object TranslationParams,
   System.object RotationParams,
   System.int EndConditionType,
   System.double OffsetDistance
)
```

### C++/CLI

```cpp
Feature^ InsertMoveFace3(
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.Object^ TranslationParams,
   System.Object^ RotationParams,
   System.int EndConditionType,
   System.double OffsetDistance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MoveType`: Type of move as defined in [swMoveFaceType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMoveFaceType_e.html)
- `ReverseDir`: True to reverse the direction, false to not
- `Angle`: Angle at which to draft the faces; valid only if MoveType is swMoveFaceType_e.swMoveFaceTypeRotate (see **Remarks**)
- `Distance`: Distance to translate or offset the faces; valid only if MoveType is one of the following:

  - swMoveFaceType_e.swMoveFaceTypeOffset
  - swMoveFaceType_e.swMoveFaceTypeTranslate and EndConditionType is swEndConditions_e.swEndCondBlind (see **Remarks**)
- `TranslationParams`: Array of three doubles for the delta x, delta y, and delta z direction translation (see **Remarks**)
- `RotationParams`: Array of six doubles:

  - First three doubles are the x, y, and z rotation origin
  - Last three doubles are the x, y, and z rotation angle

  (see **Remarks**)
- `EndConditionType`: End condition as defined in [swEndConditions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html); valid only if MoveType is swMoveFaceType_e.swMoveFaceTypeTranslate

  Only the following end condition types are valid:

  - swEndConditions_e.swEndCondBlind
  - swEndConditions_e.swEndCondUpToVertex
  - swEndConditions_e.swEndCondUpToSurface
  - swEndConditions_e.swEndCondOffsetFromSurface
  - swEndConditions_e.swEndCondUpToBody
- `OffsetDistance`: Offset from surface; valid only if MoveType is swMoveFaceType_e.swMoveFaceTypeTranslate and EndConditionType is swEndConditions_e.swEndCondOffsetFromSurface

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertMoveFace3](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoveFace3.html).

## Examples

[Create and Modify Move Face Feature (VBA)](Create_and_Modify_Move_Face_Feature_Example_VB.htm)
[Create and Modify Move Face Feature (VB.NET)](Create_and_Modify_Move_Face_Feature_Example_VBNET.htm)
[Create and Modify Move Face Feature (C#)](Create_and_Modify_Move_Face_Feature_Example_CSharp.htm)

## Remarks

Before calling this method, you need to select specific entities.

| If MoveFaceType is swMoveFaceType_e... | And EndConditionType is swEndConditions_e... | Call IModelDocExtension::SelectByID2 to select... | With mark... |
| --- | --- | --- | --- |
| Any option | Any option | Face to move | 1 |
| swMoveFaceTypeTranslate | Any option | Direction reference (plane, planar face, linear edge, or reference axis) | 2 |
| swMoveFaceTypeTranslate | swEndCondUpToVertex swEndCondUpToSurface swEndCondOffsetFromSurface swEndCondUpToBody | Up-to vertex Up-to surface Offset-from surface Up-to body | 8 |
| swMoveFaceTypeRotate | N/A | Axis reference (linear edge or reference axis) | 4 |

If you specify a value for TranslationParms or RotationParams, then do not specify a value for Distance or Angle, respectively. The translation or rotation parameters are calculated internally when Distance or Angle is specified.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
