---
title: "IGetNext Method (IWeldSymbol)"
project: "SOLIDWORKS API Help"
interface: "IWeldSymbol"
member: "IGetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetNext.html"
---

# IGetNext Method (IWeldSymbol)

Gets the next weld symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNext() As WeldSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldSymbol
Dim value As WeldSymbol

value = instance.IGetNext()
```

### C#

```csharp
WeldSymbol IGetNext()
```

### C++/CLI

```cpp
WeldSymbol^ IGetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [weld symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html) in the drawing view

## VBA Syntax

See [WeldSymbol::IGetNext](ms-its:sldworksapivb6.chm::/sldworks~WeldSymbol~IGetNext.html).

## See Also

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html)
[IWeldSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetNext.html)
[IView::GetFirstWeldSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldSymbol.html)
[IView::IGetFirstWeldSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstWeldSymbol.html)
