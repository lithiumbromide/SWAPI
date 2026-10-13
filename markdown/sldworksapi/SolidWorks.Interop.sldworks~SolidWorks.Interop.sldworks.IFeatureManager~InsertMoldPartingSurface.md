---
title: "InsertMoldPartingSurface Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoldPartingSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingSurface.html"
---

# InsertMoldPartingSurface Method (IFeatureManager)

Inserts a mold parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoldPartingSurface( _
   ByVal Radiate As System.Integer, _
   ByVal ReverseAlignment As System.Boolean, _
   ByVal ReverseOffset As System.Boolean, _
   ByVal OffsetDistance As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Smooth As System.Integer, _
   ByVal SmoothDistance As System.Double, _
   ByVal Knit As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Radiate As System.Integer
Dim ReverseAlignment As System.Boolean
Dim ReverseOffset As System.Boolean
Dim OffsetDistance As System.Double
Dim Angle As System.Double
Dim Smooth As System.Integer
Dim SmoothDistance As System.Double
Dim Knit As System.Boolean
Dim value As Feature

value = instance.InsertMoldPartingSurface(Radiate, ReverseAlignment, ReverseOffset, OffsetDistance, Angle, Smooth, SmoothDistance, Knit)
```

### C#

```csharp
Feature InsertMoldPartingSurface(
   System.int Radiate,
   System.bool ReverseAlignment,
   System.bool ReverseOffset,
   System.double OffsetDistance,
   System.double Angle,
   System.int Smooth,
   System.double SmoothDistance,
   System.bool Knit
)
```

### C++/CLI

```cpp
Feature^ InsertMoldPartingSurface(
   System.int Radiate,
   System.bool ReverseAlignment,
   System.bool ReverseOffset,
   System.double OffsetDistance,
   System.double Angle,
   System.int Smooth,
   System.double SmoothDistance,
   System.bool Knit
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Radiate`: Radiate mold parting surface as defined by [swPartingSurfaceMoldParmType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceMoldParmType_e.html)
- `ReverseAlignment`: True to reverse alignment, false to not; only available when radiate set to swPartingSurfaceMoldParmNormal and a parting line does not yet exist (see **Remarks**)
- `ReverseOffset`: True to reverse offset direction, false to not
- `OffsetDistance`: True to reverse offset direction, false to not
- `Angle`: Angle of mold parting surface; only available when radiate set to either swPartingSurfaceMoldParmTangent or swPartingSurfaceMoldParmNormal
- `Smooth`: Smooth mold parting surface as defined by [swPartingSurfaceSmoothingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceSmoothingType_e.html)
- `SmoothDistance`: Distance to smooth mold parting surface; only available when smooth set to swPartingSurfaceSmooth
- `Knit`: True to knit all surfaces, false to not

### Return Value

Pointer to [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertMoldPartingSurface](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoldPartingSurface.html).

## Remarks

f a parting line feature does not yet exist in the model, you must first select the direction of pull and the edges for the parting line using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html). For example, a face (direction of pull) has a mark of 1 and edges (parting lines) a mark of 4.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.html)
[IFeatureManager::InsertMoldPartingLine Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine.html)
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
