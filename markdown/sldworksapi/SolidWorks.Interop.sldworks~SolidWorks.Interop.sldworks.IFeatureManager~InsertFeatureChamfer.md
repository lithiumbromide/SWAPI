---
title: "InsertFeatureChamfer Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFeatureChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureChamfer.html"
---

# InsertFeatureChamfer Method (IFeatureManager)

Inserts a chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFeatureChamfer( _
   ByVal Options As System.Integer, _
   ByVal ChamferType As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal OtherDist As System.Double, _
   ByVal VertexChamDist1 As System.Double, _
   ByVal VertexChamDist2 As System.Double, _
   ByVal VertexChamDist3 As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Options As System.Integer
Dim ChamferType As System.Integer
Dim Width As System.Double
Dim Angle As System.Double
Dim OtherDist As System.Double
Dim VertexChamDist1 As System.Double
Dim VertexChamDist2 As System.Double
Dim VertexChamDist3 As System.Double
Dim value As Feature

value = instance.InsertFeatureChamfer(Options, ChamferType, Width, Angle, OtherDist, VertexChamDist1, VertexChamDist2, VertexChamDist3)
```

### C#

```csharp
Feature InsertFeatureChamfer(
   System.int Options,
   System.int ChamferType,
   System.double Width,
   System.double Angle,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

### C++/CLI

```cpp
Feature^ InsertFeatureChamfer(
   System.int Options,
   System.int ChamferType,
   System.double Width,
   System.double Angle,
   System.double OtherDist,
   System.double VertexChamDist1,
   System.double VertexChamDist2,
   System.double VertexChamDist3
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Options as defined by [swFeatureChamferOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureChamferOption_e.html)
- `ChamferType`: Chamfer type as defined by [swChamferType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swChamferType_e.html)
- `Width`: If ChamferType is swChamferAngleDistance, then specify width of chamfer
- `Angle`: If ChamferType is swChamferAngleDistance, then specify the angle of the chamfer
- `OtherDist`: If ChamferType is swChamferEqualDistance, then you can specify a single value so that all distances are equal
- `VertexChamDist1`: If ChamferType is swChamferDistanceDistance or swChamferVertex, then specify a value for the distance on first side
- `VertexChamDist2`: If ChamferType is swChamferDistanceDistance or swChamferVertex, then specify a value for the distance on second side
- `VertexChamDist3`: If ChamferType is swChamferVertex, then specify a value for the distance on third side

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertFeatureChamfer](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFeatureChamfer.html).

## Examples

See the [IChamferFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html) examples.

## Remarks

Both swChamferType_e.swChamferAngleDistance and swChamferType_e.swChamferDistanceDistance are edge chamfers. This means that all measurements are from edges. An angle-distance chamfer requires an angle and a distance; a distance-distance chamfer requires two distances, one for each side of the chamfered edge.

A swChamferType_e.swChamferVertex chamfer only works on a vertex with three adjacent edges of the same convexity. A vertex chamfer requires three distances along three adjacent edges. For non-linear edges, this value is an arc length value; it is not a chordal value. See [IVertex::EnumEdgesOriented](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex~EnumEdgesOriented.html) to determine the edge order used by this method.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
