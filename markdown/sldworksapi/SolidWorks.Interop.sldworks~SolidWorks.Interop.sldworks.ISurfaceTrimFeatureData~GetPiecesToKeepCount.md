---
title: "GetPiecesToKeepCount Method (ISurfaceTrimFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceTrimFeatureData"
member: "GetPiecesToKeepCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~GetPiecesToKeepCount.html"
---

# GetPiecesToKeepCount Method (ISurfaceTrimFeatureData)

Gets the number of pieces to keep for this surface trim feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPiecesToKeepCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceTrimFeatureData
Dim value As System.Integer

value = instance.GetPiecesToKeepCount()
```

### C#

```csharp
System.int GetPiecesToKeepCount()
```

### C++/CLI

```cpp
System.int GetPiecesToKeepCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of pieces to keep

## VBA Syntax

See [SurfaceTrimFeatureData::GetPiecesToKeepCount](ms-its:sldworksapivb6.chm::/sldworks~SurfaceTrimFeatureData~GetPiecesToKeepCount.html).

## Examples

See the [ISurfaceTrimFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html) examples.

## Remarks

Call this method before calling [ISurfaceTrimFeatureData::IGetPiecesToKeep](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceTrimFeatureData~IGetPiecesToKeep.html) to get the size of the array for that method.

## See Also

[ISurfaceTrimFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData.html)
[ISurfaceTrimFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html)
[ISurfaceTrimFeatureData::ISetPiecesToKeep Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~ISetPiecesToKeep.html)
[ISurfaceTrimFeatureData::PiecesToKeep Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData~PiecesToKeep.html)

## Availability

SOLIDWORKS 2001Plus SP2, Revision Number 10.2
