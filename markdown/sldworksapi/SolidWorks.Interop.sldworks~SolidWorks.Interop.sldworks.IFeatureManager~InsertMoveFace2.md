---
title: "InsertMoveFace2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoveFace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace2.html"
---

# InsertMoveFace2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertMoveFace3.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveFace3.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoveFace2( _
   ByVal MoveType As System.Integer, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle As System.Double, _
   ByVal Distance As System.Double, _
   ByVal TranslationParams As System.Object, _
   ByVal RotationParams As System.Object _
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
Dim value As Feature

value = instance.InsertMoveFace2(MoveType, ReverseDir, Angle, Distance, TranslationParams, RotationParams)
```

### C#

```csharp
Feature InsertMoveFace2(
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.object TranslationParams,
   System.object RotationParams
)
```

### C++/CLI

```cpp
Feature^ InsertMoveFace2(
   System.int MoveType,
   System.bool ReverseDir,
   System.double Angle,
   System.double Distance,
   System.Object^ TranslationParams,
   System.Object^ RotationParams
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MoveType`: Type of move:

  - 0 = Offset
  - 1 = Translate
  - 2 = Rotate
- `ReverseDir`: True to reverse the direction, false to not
- `Angle`: If MoveType is Rotate, then specify the angle at which to draft the faces
- `Distance`: Distance to offset or translate the faces
- `TranslationParams`: Array of three doubles for the delta x, delta y, and delta z direction translation
- `RotationParams`: Array of six doubles:

  - First three doubles are the x, y, and z rotation origin
  - Last three doubles are the x, y, and z rotation angle

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMoveFace2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoveFace2.html).

## Remarks

Use the following marks with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html):

- 1 = face
- 2 = direction reference (plane, planar face, linear edge, or reference axis) for translate
- 4 = axis reference (linear edge or reference axis) for rotate

If you specify a value for TranslationParms or RotationParams, then do not specify a value for Distance or Angle, respectively. The translation or rotation parameters are calculated internally when Distance or Angle is specified.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::IInsertMoveFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMoveFace2.html)
[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
