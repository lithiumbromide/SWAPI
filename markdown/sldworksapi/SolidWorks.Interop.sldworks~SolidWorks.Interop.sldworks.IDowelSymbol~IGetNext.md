---
title: "IGetNext Method (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetNext.html"
---

# IGetNext Method (IDowelSymbol)

Gets the next dowel symbol in the current sheet, view, or model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As DowelSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As DowelSymbol

value = instance.IGetNext()
```

### C#

```csharp
DowelSymbol IGetNext()
```

### C++/CLI

```cpp
DowelSymbol^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the next [dowel symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [DowelSymbol::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~DowelSymbol~IGetNext.html).

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)
[IDowelSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
