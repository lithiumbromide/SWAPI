---
title: "GetPolylineSizeAtIndex2 Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetPolylineSizeAtIndex2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolylineSizeAtIndex2.html"
---

# GetPolylineSizeAtIndex2 Method (IDisplayData)

Gets the number of array elements returned by [IDisplayData::GetPolylineAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolylineAtIndex2.html) and [IDisplayData::IGetPolylineAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPolylineSizeAtIndex2( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetPolylineSizeAtIndex2(Index)
```

### C#

```csharp
System.int GetPolylineSizeAtIndex2(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetPolylineSizeAtIndex2(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired polyline where the index begins at zero

### Return Value

Number array elements returned by [IDisplayData::GetPolylineAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolylineAtIndex2.html) and [IDisplayData::IGetPolylineAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2.html)

## VBA Syntax

See [DisplayData::GetPolylineSizeAtIndex2](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetPolylineSizeAtIndex2.html).

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetPolyLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPolyLineCount.html)
