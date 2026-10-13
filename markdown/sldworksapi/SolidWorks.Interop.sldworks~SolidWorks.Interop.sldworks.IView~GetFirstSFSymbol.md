---
title: "GetFirstSFSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstSFSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.html"
---

# GetFirstSFSymbol Method (IView)

Gets the first surface-finish symbols in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstSFSymbol() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstSFSymbol()
```

### C#

```csharp
System.object GetFirstSFSymbol()
```

### C++/CLI

```cpp
System.Object^ GetFirstSFSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [surface-finish symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)

## VBA Syntax

See [View::GetFirstSFSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstSFSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[ISFSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.html)
[ISFSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetNext.html)
[IView::IGetFirstSFSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstSFSymbol.html)
[IView::IGetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols.html)
[IView::GetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.html)
