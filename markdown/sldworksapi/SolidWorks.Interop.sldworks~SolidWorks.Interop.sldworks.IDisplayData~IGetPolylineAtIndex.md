---
title: "IGetPolylineAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetPolylineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPolylineAtIndex.html"
---

# IGetPolylineAtIndex Method (IDisplayData)

Obsolete. Superseded by [IDisplayData::IGetPolylineAtIndex2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~IGetPolylineAtIndex2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPolylineAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetPolylineAtIndex(Index)
```

### C#

```csharp
System.double IGetPolylineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetPolylineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [DisplayData::IGetPolylineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~IGetPolylineAtIndex.html).

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
