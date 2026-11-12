---
title: "SetEdgeChamferDistance Method (IChamferFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData"
member: "SetEdgeChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData~SetEdgeChamferDistance.html"
---

# SetEdgeChamferDistance Method (IChamferFeatureData)

Obsolete. Superseded by [IChamferFeatureData2::SetEdgeChamferDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~SetEdgeChamferDistance.html).

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
Dim instance As IChamferFeatureData
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

- `Side`:
- `Distance`:

## VBA Syntax

See [ChamferFeatureData::SetEdgeChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData~SetEdgeChamferDistance.html).

## See Also

[IChamferFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData.html)
[IChamferFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData_members.html)
