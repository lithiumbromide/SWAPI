---
title: "GetEdgeChamferDistance Method (IChamferFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData"
member: "GetEdgeChamferDistance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData~GetEdgeChamferDistance.html"
---

# GetEdgeChamferDistance Method (IChamferFeatureData)

Obsolete. Superseded by [IChamferFeatureData2::GetEdgeChamferDistance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IChamferFeatureData2~GetEdgeChamferDistance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEdgeChamferDistance( _
   ByVal Side As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData
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

- `Side`:

## VBA Syntax

See [ChamferFeatureData::GetEdgeChamferDistance](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData~GetEdgeChamferDistance.html).

## See Also

[IChamferFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData.html)
[IChamferFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData_members.html)
