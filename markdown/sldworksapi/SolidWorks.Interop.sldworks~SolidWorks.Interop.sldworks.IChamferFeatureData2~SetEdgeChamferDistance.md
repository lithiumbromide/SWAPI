---
title: "SetEdgeChamferDistance Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "SetEdgeChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~SetEdgeChamferDistance.html"
---

# SetEdgeChamferDistance Method (IChamferFeatureData2)

Sets the edge chamfer distance on either side of the edge.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetEdgeChamferDistance( _
   ByVal Side As System.Integer, _
   ByVal Distance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Side As System.Integer
Dim Distance As System.Double

instance.SetEdgeChamferDistance(Side, Distance)
```

### C#

```csharp
void SetEdgeChamferDistance(
   System.int Side,
   System.double Distance
)
```

### C++/CLI

```cpp
void SetEdgeChamferDistance(
   System.int Side,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Feature direction (see **Remarks**)
- `Distance`: Edge chamfer distance

## VBA Syntax

See [ChamferFeatureData2::SetEdgeChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~SetEdgeChamferDistance.html).

## Remarks

Set the Side parameter to 0 or 1. For angle-distance chamfers, set side to 0.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::GetEdgeChamferDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~GetEdgeChamferDistance.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
