---
title: "InsertSheetMetalMiterFlange Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalMiterFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalMiterFlange.html"
---

# InsertSheetMetalMiterFlange Method (IFeatureManager)

Inserts a meter flange in a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalMiterFlange( _
   ByVal UseDefaultRadius As System.Boolean, _
   ByVal GlobalRadius As System.Double, _
   ByVal RipGap As System.Double, _
   ByVal UseDefaultRelief As System.Boolean, _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal ReliefRatio As System.Double, _
   ByVal ReliefWidth As System.Double, _
   ByVal ReliefDepth As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal TrimSideBends As System.Boolean, _
   ByVal FlangePos As System.Integer, _
   ByVal OffsetDist1 As System.Double, _
   ByVal OffsetDist2 As System.Double, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim UseDefaultRadius As System.Boolean
Dim GlobalRadius As System.Double
Dim RipGap As System.Double
Dim UseDefaultRelief As System.Boolean
Dim UseReliefRatio As System.Boolean
Dim ReliefRatio As System.Double
Dim ReliefWidth As System.Double
Dim ReliefDepth As System.Double
Dim ReliefType As System.Integer
Dim TrimSideBends As System.Boolean
Dim FlangePos As System.Integer
Dim OffsetDist1 As System.Double
Dim OffsetDist2 As System.Double
Dim PCBA As CustomBendAllowance
Dim value As Feature

value = instance.InsertSheetMetalMiterFlange(UseDefaultRadius, GlobalRadius, RipGap, UseDefaultRelief, UseReliefRatio, ReliefRatio, ReliefWidth, ReliefDepth, ReliefType, TrimSideBends, FlangePos, OffsetDist1, OffsetDist2, PCBA)
```

### C#

```csharp
Feature InsertSheetMetalMiterFlange(
   System.bool UseDefaultRadius,
   System.double GlobalRadius,
   System.double RipGap,
   System.bool UseDefaultRelief,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.int ReliefType,
   System.bool TrimSideBends,
   System.int FlangePos,
   System.double OffsetDist1,
   System.double OffsetDist2,
   CustomBendAllowance PCBA
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalMiterFlange(
   System.bool UseDefaultRadius,
   System.double GlobalRadius,
   System.double RipGap,
   System.bool UseDefaultRelief,
   System.bool UseReliefRatio,
   System.double ReliefRatio,
   System.double ReliefWidth,
   System.double ReliefDepth,
   System.int ReliefType,
   System.bool TrimSideBends,
   System.int FlangePos,
   System.double OffsetDist1,
   System.double OffsetDist2,
   CustomBendAllowance^ PCBA
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDefaultRadius`: True to use default bend radius, false to use GlobalRadius
- `GlobalRadius`: Global bend radius
- `RipGap`: Rip-gap distance
- `UseDefaultRelief`: True to use parent bend's ratio, false to not
- `UseReliefRatio`: True to use custom relief ratio, false to not
- `ReliefRatio`: If useReliefRatio is True, then specify relief ratio
- `ReliefWidth`: If UseReliefRatio is True and ReliefType is swSheetMetalReliefRectangular or swSheetMetalReliefObround, then specify relief depth
- `ReliefDepth`: If UseReliefRatio is True and ReliefType is swSheetMetalReliefRectangular or swSheetMetalReliefObround, then specify relief depth
- `ReliefType`: Relief type as defined by [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html); valid selections:

  - swSheetMetalRelievObround
  - swSheetMetalReliefRectangular
  - swSheetMetalReliefTear
- `TrimSideBends`: True to trim side bends, false to not
- `FlangePos`: Flange position as defined by [swFlangePositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html); valid selections:

  - swFlangePositionTypeMaterialInside
  - swFlangePositionTypeMaterialOutside
  - swFlangePositionTypeBendOutside
- `OffsetDist1`: Starting offset distance if partial flange
- `OffsetDist2`: Ending offset distance if partial flange
- `PCBA`:

  | If... | Then... |
  | --- | --- |
  | non-NULL | Pointer to ICustomBendAllowance object for which required values have been set |
  | NULL | Parent bend's bend allowance is used |

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object or NULL

## VBA Syntax

See [FeatureManager::InsertSheetMetalMiterFlange](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalMiterFlange.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
