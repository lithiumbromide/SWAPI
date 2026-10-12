---
title: "GetVertexChamferDistance Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "GetVertexChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetVertexChamferDistance.html"
---

# GetVertexChamferDistance Method (IChamferFeatureData2)

Gets the vertex chamfer distance.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexChamferDistance( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim value As System.Double

value = instance.GetVertexChamferDistance(Side)
```

### C#

```csharp
System.double GetVertexChamferDistance(
   System.int Side
)
```

### C++/CLI

```cpp
System.double GetVertexChamferDistance(
   System.int Side
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Feature direction (see **Remarks**)

### Return Value

Vertex chamfer distance

## VBA Syntax

See [ChamferFeatureData2::GetVertexChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~GetVertexChamferDistance.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## Remarks

There are three edges of a vertex. Set the Side parameter to 0, 1, or 2. The Side parameter is relevant only for vertex-type of chamfers.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::SetVertexChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetVertexChamferDistance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
