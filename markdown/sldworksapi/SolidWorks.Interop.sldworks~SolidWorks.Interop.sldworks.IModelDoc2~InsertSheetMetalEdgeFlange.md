---
title: "InsertSheetMetalEdgeFlange Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSheetMetalEdgeFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalEdgeFlange.html"
---

# InsertSheetMetalEdgeFlange Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalEdgeFlange2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalEdgeFlange( _
   ByVal FlangeEdge As System.Object, _
   ByVal SketchFeat As System.Object, _
   ByVal BooleanOptions As System.Integer, _
   ByVal DAngle As System.Double, _
   ByVal DRadius As System.Double, _
   ByVal BendPosition As System.Integer, _
   ByVal DOffsetDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal DReliefRatio As System.Double, _
   ByVal DReliefWidth As System.Double, _
   ByVal DReliefDepth As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim FlangeEdge As System.Object
Dim SketchFeat As System.Object
Dim BooleanOptions As System.Integer
Dim DAngle As System.Double
Dim DRadius As System.Double
Dim BendPosition As System.Integer
Dim DOffsetDist As System.Double
Dim ReliefType As System.Integer
Dim DReliefRatio As System.Double
Dim DReliefWidth As System.Double
Dim DReliefDepth As System.Double
Dim value As System.Object

value = instance.InsertSheetMetalEdgeFlange(FlangeEdge, SketchFeat, BooleanOptions, DAngle, DRadius, BendPosition, DOffsetDist, ReliefType, DReliefRatio, DReliefWidth, DReliefDepth)
```

### C#

```csharp
System.object InsertSheetMetalEdgeFlange(
   System.object FlangeEdge,
   System.object SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth
)
```

### C++/CLI

```cpp
System.Object^ InsertSheetMetalEdgeFlange(
   System.Object^ FlangeEdge,
   System.Object^ SketchFeat,
   System.int BooleanOptions,
   System.double DAngle,
   System.double DRadius,
   System.int BendPosition,
   System.double DOffsetDist,
   System.int ReliefType,
   System.double DReliefRatio,
   System.double DReliefWidth,
   System.double DReliefDepth
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

## VBA Syntax

See [ModelDoc2::InsertSheetMetalEdgeFlange](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSheetMetalEdgeFlange.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
