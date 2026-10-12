---
title: "GetFirstWeldSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstWeldSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstWeldSymbol.html"
---

# GetFirstWeldSymbol Method (IView)

Gets the first weld symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstWeldSymbol() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstWeldSymbol()
```

### C#

```csharp
System.object GetFirstWeldSymbol()
```

### C++/CLI

```cpp
System.Object^ GetFirstWeldSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [weld symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [View::GetFirstWeldSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstWeldSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IWeldSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetNext.html)
[IWeldSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~IGetNext.html)
[IView::GetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols.html)
[IView::IGetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldSymbols.html)
