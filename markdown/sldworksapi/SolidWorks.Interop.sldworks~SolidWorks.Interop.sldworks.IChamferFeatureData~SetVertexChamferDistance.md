---
title: "SetVertexChamferDistance Method (IChamferFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData"
member: "SetVertexChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData~SetVertexChamferDistance.html"
---

# SetVertexChamferDistance Method (IChamferFeatureData)

Obsolete. Superseded by [IChamferFeatureData2::SetVertexChamferDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~SetVertexChamferDistance.html).

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
Dim instance As IChamferFeatureData
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

- `Side`:
- `Distance`:

## VBA Syntax

See [ChamferFeatureData::SetVertexChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData~SetVertexChamferDistance.html).

## See Also

[IChamferFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData.html)
[IChamferFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData_members.html)
