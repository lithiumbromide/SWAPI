---
title: "GetEdgeChamferDistance Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "GetEdgeChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetEdgeChamferDistance.html"
---

# GetEdgeChamferDistance Method (IChamferFeatureData2)

Gets the edge chamfer distance on either side of the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeChamferDistance( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim value As System.Double

value = instance.GetEdgeChamferDistance(Side)
```

### C#

```csharp
System.double GetEdgeChamferDistance(
   System.int Side
)
```

### C++/CLI

```cpp
System.double GetEdgeChamferDistance(
   System.int Side
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Feature direction (see **Remarks**)

### Return Value

Edge chamfer distance

## VBA Syntax

See [ChamferFeatureData2::GetEdgeChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~GetEdgeChamferDistance.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## Remarks

Set the Side parameter to 0 or 1. For angle-distance chamfers, set side to 0.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::SetEdgeChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetEdgeChamferDistance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
