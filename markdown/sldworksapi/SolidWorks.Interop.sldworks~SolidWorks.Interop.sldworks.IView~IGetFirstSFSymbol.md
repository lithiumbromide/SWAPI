---
title: "IGetFirstSFSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstSFSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstSFSymbol.html"
---

# IGetFirstSFSymbol Method (IView)

Gets the first surface-finish symbols in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstSFSymbol() As SFSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As SFSymbol

value = instance.IGetFirstSFSymbol()
```

### C#

```csharp
SFSymbol IGetFirstSFSymbol()
```

### C++/CLI

```cpp
SFSymbol^ IGetFirstSFSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [surface-finish symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)

## VBA Syntax

See [View::IGetFirstSFSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstSFSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstSFSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstSFSymbol.html)
[ISFSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetNext.html)
[ISFSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetNext.html)
