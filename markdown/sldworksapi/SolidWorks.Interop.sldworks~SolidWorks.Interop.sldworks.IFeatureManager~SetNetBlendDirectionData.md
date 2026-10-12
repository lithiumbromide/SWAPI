---
title: "SetNetBlendDirectionData Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "SetNetBlendDirectionData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendDirectionData.html"
---

# SetNetBlendDirectionData Method (IFeatureManager)

Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetNetBlendDirectionData( _
   ByVal Direction As System.Short, _
   ByVal InfluenceType As System.Short, _
   ByVal TrimCurves As System.Short, _
   ByVal BlendClosed As System.Boolean, _
   ByVal SplitSurfaces As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Direction As System.Short
Dim InfluenceType As System.Short
Dim TrimCurves As System.Short
Dim BlendClosed As System.Boolean
Dim SplitSurfaces As System.Boolean
Dim value As Feature

value = instance.SetNetBlendDirectionData(Direction, InfluenceType, TrimCurves, BlendClosed, SplitSurfaces)
```

### C#

```csharp
Feature SetNetBlendDirectionData(
   System.short Direction,
   System.short InfluenceType,
   System.short TrimCurves,
   System.bool BlendClosed,
   System.bool SplitSurfaces
)
```

### C++/CLI

```cpp
Feature^ SetNetBlendDirectionData(
   System.short Direction,
   System.short InfluenceType,
   System.short TrimCurves,
   System.bool BlendClosed,
   System.bool SplitSurfaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Direction`: - 0 = Direction 1
  - 1 = Direction 2
- `InfluenceType`: - 0 = Global
  - 1 = To Next Curve
  - 2 = To Next Sharp
  - 3 = To Next Edge
- `TrimCurves`: - 0 = False to trim curves
  - 1 = True to trim curves
- `BlendClosed`: True closes this boundary feature or boundary surface feature, false leaves this boundary feature or boundary surface feature open
- `SplitSurfaces`: Not used

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::SetNetBlendDirectionData](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~SetNetBlendDirectionData.html).

## Examples

[Insert Boundary Surface Feature (VBA)](Insert_Boundary_Surface_Feature_Example_VB.htm)
[Insert Boundary Feature (C#)](Insert_Boundary_Feature_Example_CSharp.htm)
[Insert Boundary Feature (VB.NET)](Insert_Boundary_Feature_Example_VBNET.htm)
[Insert Boundary Feature (VBA)](Insert_Boundary_Feature_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertNetBlend Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertNetBlend.html)
[IFeatureManager::SetNetBlendCurveData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetNetBlendCurveData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
