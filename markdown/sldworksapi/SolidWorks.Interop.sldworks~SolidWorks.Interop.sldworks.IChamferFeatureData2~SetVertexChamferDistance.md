---
title: "SetVertexChamferDistance Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "SetVertexChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetVertexChamferDistance.html"
---

# SetVertexChamferDistance Method (IChamferFeatureData2)

Sets the vertex chamfer distance.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVertexChamferDistance( _
   ByVal Side As System.Integer, _
   ByVal Distance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim Distance As System.Double

instance.SetVertexChamferDistance(Side, Distance)
```

### C#

```csharp
void SetVertexChamferDistance(
   System.int Side,
   System.double Distance
)
```

### C++/CLI

```cpp
void SetVertexChamferDistance(
   System.int Side,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Feature direction (see **Remarks**)
- `Distance`: Vertex chamfer distance

## VBA Syntax

See [ChamferFeatureData2::SetVertexChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~SetVertexChamferDistance.html).

## Remarks

There are three edges of a vertex. Set the Side parameter to 0, 1, or 2 to specify the edge. The Side parameter is relevant only for vertex-type chamfers.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::GetVertexChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetVertexChamferDistance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
