---
title: "GetVertexChamferDistance Method (IChamferFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData"
member: "GetVertexChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData~GetVertexChamferDistance.html"
---

# GetVertexChamferDistance Method (IChamferFeatureData)

Obsolete. Superseded by [IChamferFeatureData2::GetVertexChamferDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~GetVertexChamferDistance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVertexChamferDistance( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData
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

- `Side`:

## VBA Syntax

See [ChamferFeatureData::GetVertexChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData~GetVertexChamferDistance.html).

## See Also

[IChamferFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData.html)
[IChamferFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData_members.html)
