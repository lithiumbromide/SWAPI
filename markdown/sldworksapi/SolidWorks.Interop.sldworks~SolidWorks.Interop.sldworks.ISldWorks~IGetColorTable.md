---
title: "IGetColorTable Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetColorTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetColorTable.html"
---

# IGetColorTable Method (ISldWorks)

Gets a color table from the SOLIDWORKS Design application.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetColorTable() As ColorTable
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As ColorTable

value = instance.IGetColorTable()
```

### C#

```csharp
ColorTable IGetColorTable()
```

### C++/CLI

```cpp
ColorTable^ IGetColorTable();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Color table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable.html)

## VBA Syntax

See [SldWorks::IGetColorTable](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetColorTable.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetColorTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetColorTable.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
