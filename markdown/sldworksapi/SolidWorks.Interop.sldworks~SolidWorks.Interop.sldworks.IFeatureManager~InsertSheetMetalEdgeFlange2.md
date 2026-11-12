---
title: "InsertSheetMetalEdgeFlange2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalEdgeFlange2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalEdgeFlange2.html"
---

# InsertSheetMetalEdgeFlange2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalEdgeFlange2( _
   ByVal FlangeEdges As System.Object, _
   ByVal SketchFeats As System.Object, _
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
Dim FlangeEdges As System.Object
Dim SketchFeats As System.Object
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

value = instance.InsertSheetMetalEdgeFlange2(FlangeEdges, SketchFeats, BooleanOptions, FlangeAngle, FlangeRadius, BendPosition, FlangeOffsetDist, ReliefType, FlangeReliefRatio, FlangeReliefWidth, FlangeReliefDepth, FlangeSharpType, CustomBendAllowance)
```

### C#

```csharp
Feature InsertSheetMetalEdgeFlange2(
   System.object FlangeEdges,
   System.object SketchFeats,
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
Feature^ InsertSheetMetalEdgeFlange2(
   System.Object^ FlangeEdges,
   System.Object^ SketchFeats,
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

- `FlangeEdges`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to which to apply a flange
- `SketchFeats`: Array of [sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html) to use for the flange
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

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) object

## VBA Syntax

See [FeatureManager::InsertSheetMetalEdgeFlange2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalEdgeFlange2.html).

## Examples

[Insert Sheet Metal Edge Flange (VBA)](Insert_Sheet_Metal_Edge_Flange_Example_VB.htm)
[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

## Remarks

Before calling this method, call [IModelDoc2::InsertSketchForEdgeFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertSketchForEdgeFlange.html) and create a profile for the flange. After creating the profile, call this method to create the flange.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
