---
title: "GetPolygonSizeAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetPolygonSizeAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonSizeAtIndex.html"
---

# GetPolygonSizeAtIndex Method (IDisplayData)

Gets the number of array elements returned by [IDisplayData::GetPolygonAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolygonAtIndex.html) and [IDisplayData::IGetPolygonAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolygonSizeAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetPolygonSizeAtIndex(Index)
```

### C#

```csharp
System.int GetPolygonSizeAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetPolygonSizeAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index for the polygon

### Return Value

Number of array elements returned by [IDisplayData::GetPolygonAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolygonAtIndex.html) and [IDisplayData::IGetPolygonAtIndex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetPolygonAtIndex.html)

## VBA Syntax

See [DisplayData::GetPolygonSizeAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetPolygonSizeAtIndex.html).

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetPolygonCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolygonCount.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
