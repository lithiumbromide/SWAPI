---
title: "InsertSheetMetalEdgeFlange Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalEdgeFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange.html"
---

# InsertSheetMetalEdgeFlange Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalEdgeFlange( _
   ByVal FlangeEdge As Edge, _
   ByVal SketchFeat As Feature, _
   ByVal BooleanOptions As System.Integer, _
   ByVal DAngle As System.Double, _
   ByVal DRadius As System.Double, _
   ByVal BendPosition As System.Integer, _
   ByVal DOffsetDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal DReliefRatio As System.Double, _
   ByVal DReliefWidth As System.Double, _
   ByVal DReliefDepth As System.Double, _
   ByVal FlangeSharpType As System.Integer, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim FlangeEdge As Edge
Dim SketchFeat As Feature
Dim BooleanOptions As System.Integer
Dim DAngle As System.Double
Dim DRadius As System.Double
Dim BendPosition As System.Integer
Dim DOffsetDist As System.Double
Dim ReliefType As System.Integer
Dim DReliefRatio As System.Double
Dim DReliefWidth As System.Double
Dim DReliefDepth As System.Double
Dim FlangeSharpType As System.Integer
Dim PCBA As CustomBendAllowance
Dim value As Feature

value = instance.InsertSheetMetalEdgeFlange(FlangeEdge, SketchFeat, BooleanOptions, DAngle, DRadius, BendPosition, DOffsetDist, ReliefType, DReliefRatio, DReliefWidth, DReliefDepth, FlangeSharpType, PCBA)
```

### C#

```csharp
Feature InsertSheetMetalEdgeFlange(
   Edge FlangeEdge,
   Feature SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance PCBA
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalEdgeFlange(
   Edge^ FlangeEdge,
   Feature^ SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance^ PCBA
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FlangeEdge`:
- `SketchFeat`:
- `BooleanOptions`:
- `DAngle`:
- `DRadius`:
- `BendPosition`:
- `DOffsetDist`:
- `ReliefType`:
- `DReliefRatio`:
- `DReliefWidth`:
- `DReliefDepth`:
- `FlangeSharpType`:
- `PCBA`:

## VBA Syntax

See [FeatureManager::InsertSheetMetalEdgeFlange](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalEdgeFlange.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
