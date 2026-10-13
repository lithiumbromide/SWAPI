---
title: "IInsertSheetMetalEdgeFlange2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IInsertSheetMetalEdgeFlange2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertSheetMetalEdgeFlange2.html"
---

# IInsertSheetMetalEdgeFlange2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertSheetMetalEdgeFlange2( _
   ByVal EdgeCount As System.Integer, _
   ByRef FlangeEdges As Edge, _
   ByVal SketchFeatCount As System.Integer, _
   ByRef SketchFeat As Feature, _
   ByVal BooleanOptions As System.Integer, _
   ByVal FlangeAngle As System.Double, _
   ByVal FlangeRadius As System.Double, _
   ByVal BendPosition As System.Integer, _
   ByVal FlangeOffsetDist As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal FlangeReliefRatio As System.Double, _
   ByVal FlangeReliefWidth As System.Double, _
   ByVal FlangeReliefDepth As System.Double, _
   ByVal FlangeSharpType As System.Integer, _
   ByVal CustomBendAllowance As CustomBendAllowance _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim EdgeCount As System.Integer
Dim FlangeEdges As Edge
Dim SketchFeatCount As System.Integer
Dim SketchFeat As Feature
Dim BooleanOptions As System.Integer
Dim FlangeAngle As System.Double
Dim FlangeRadius As System.Double
Dim BendPosition As System.Integer
Dim FlangeOffsetDist As System.Double
Dim ReliefType As System.Integer
Dim FlangeReliefRatio As System.Double
Dim FlangeReliefWidth As System.Double
Dim FlangeReliefDepth As System.Double
Dim FlangeSharpType As System.Integer
Dim CustomBendAllowance As CustomBendAllowance
Dim value As Feature

value = instance.IInsertSheetMetalEdgeFlange2(EdgeCount, FlangeEdges, SketchFeatCount, SketchFeat, BooleanOptions, FlangeAngle, FlangeRadius, BendPosition, FlangeOffsetDist, ReliefType, FlangeReliefRatio, FlangeReliefWidth, FlangeReliefDepth, FlangeSharpType, CustomBendAllowance)
```

### C#

```csharp
Feature IInsertSheetMetalEdgeFlange2(
   System.int EdgeCount,
   ref Edge FlangeEdges,
   System.int SketchFeatCount,
   ref Feature SketchFeat,
   System.int BooleanOptions,
   System.double FlangeAngle,
   System.double FlangeRadius,
   System.int BendPosition,
   System.double FlangeOffsetDist,
   System.int ReliefType,
   System.double FlangeReliefRatio,
   System.double FlangeReliefWidth,
   System.double FlangeReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance CustomBendAllowance
)
```

### C++/CLI

```cpp
Feature^ IInsertSheetMetalEdgeFlange2(
   System.int EdgeCount,
   Edge^% FlangeEdges,
   System.int SketchFeatCount,
   Feature^% SketchFeat,
   System.int BooleanOptions,
   System.double FlangeAngle,
   System.double FlangeRadius,
   System.int BendPosition,
   System.double FlangeOffsetDist,
   System.int ReliefType,
   System.double FlangeReliefRatio,
   System.double FlangeReliefWidth,
   System.double FlangeReliefDepth,
   System.int FlangeSharpType,
   CustomBendAllowance^ CustomBendAllowance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeCount`: Number of edges for the flange
- `FlangeEdges`: Array of edge to which to apply a flange
- `SketchFeatCount`: Number of sketches for the flange
- `SketchFeat`: Array of sketch [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) to use for the flange
- `BooleanOptions`: Flange options as defined by [swInsertEdgeFlangeOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertEdgeFlangeOptions_e.html)
- `FlangeAngle`: Flange angle
- `FlangeRadius`: Bend radius
- `BendPosition`: Flange bend position as defined by [swFlangePositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html)
- `FlangeOffsetDist`: Length of flange
- `ReliefType`: Relief type as defined by [swSheetMetalReliefTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalReliefTypes_e.html)
- `FlangeReliefRatio`: Relief ratio
- `FlangeReliefWidth`: Relief width
- `FlangeReliefDepth`: Relief depth
- `FlangeSharpType`: Flange virtual sharp type as defined by [swFlangeDimTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeDimTypes_e.html)
- `CustomBendAllowance`:

  | If... | Then... |
  | --- | --- |
  | non-NULL | Pointer to ICustomBendAllowance object for which required values have been set |
  | NULL | Parent bend's bend allowance is used |

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::IInsertSheetMetalEdgeFlange2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~IInsertSheetMetalEdgeFlange2.html).

## Remarks

Before calling this method, call [IModelDoc2::IInsertSketchForEdgeFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertSketchForEdgeFlange.html) and create a profile for the flange. After creating the profile, call this method to create the flange.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::InsertSheetMetalEdgeFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalEdgeFlange.html)
[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
