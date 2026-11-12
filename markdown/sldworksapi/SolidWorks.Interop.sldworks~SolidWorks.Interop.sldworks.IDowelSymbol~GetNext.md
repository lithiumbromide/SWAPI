---
title: "GetNext Method (IDowelSymbol)"
project: "SOLIDWORKS API Help"
interface: "IDowelSymbol"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.html"
---

# GetNext Method (IDowelSymbol)

Gets the next dowel symbol in the current sheet, view, or model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDowelSymbol
Dim value As System.Object

value = instance.GetNext()
```

### C#

```csharp
System.object GetNext()
```

### C++/CLI

```cpp
System.Object^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next dowel symbol

## VBA Syntax

See [DowelSymbol::GetNext](ms-its:sldworksapivb6.chm::/sldworks~DowelSymbol~GetNext.html).

## See Also

[IDowelSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)
[IDowelSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html)
[IDowelSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetNext.html)
[IView::GetFirstDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDowelSymbol.html)
[IView::IGetFirstDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDowelSymbol.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
