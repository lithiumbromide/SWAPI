---
title: "IGetFirstWeldSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstWeldSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstWeldSymbol.html"
---

# IGetFirstWeldSymbol Method (IView)

Gets the first weld symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstWeldSymbol() As WeldSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As WeldSymbol

value = instance.IGetFirstWeldSymbol()
```

### C#

```csharp
WeldSymbol IGetFirstWeldSymbol()
```

### C++/CLI

```cpp
WeldSymbol^ IGetFirstWeldSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [weld symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [View::IGetFirstWeldSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstWeldSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstWeldSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldSymbol.html)
[IWeldSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetNext.html)
[IWeldSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetNext.html)
