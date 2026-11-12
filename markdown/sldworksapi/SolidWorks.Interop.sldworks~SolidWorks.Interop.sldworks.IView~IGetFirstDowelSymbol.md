---
title: "IGetFirstDowelSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstDowelSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDowelSymbol.html"
---

# IGetFirstDowelSymbol Method (IView)

Gets the first dowel symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstDowelSymbol() As DowelSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As DowelSymbol

value = instance.IGetFirstDowelSymbol()
```

### C#

```csharp
DowelSymbol IGetFirstDowelSymbol()
```

### C++/CLI

```cpp
DowelSymbol^ IGetFirstDowelSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [dowel symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [View::IGetFirstDowelSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~IGetFirstDowelSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDowelSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.html)
[IDowelSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetNext.html)
[IView::GetFirstDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDowelSymbol.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
