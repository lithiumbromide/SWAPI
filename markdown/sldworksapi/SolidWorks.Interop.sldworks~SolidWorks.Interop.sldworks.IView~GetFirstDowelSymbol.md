---
title: "GetFirstDowelSymbol Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstDowelSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstDowelSymbol.html"
---

# GetFirstDowelSymbol Method (IView)

Gets the first dowel symbol in the view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstDowelSymbol() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstDowelSymbol()
```

### C#

```csharp
System.object GetFirstDowelSymbol()
```

### C++/CLI

```cpp
System.Object^ GetFirstDowelSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [dowel symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [View::GetFirstDowelSymbol](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstDowelSymbol.html).

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IDowelSymbol::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~GetNext.html)
[IDowelSymbol::IGetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol~IGetNext.html)
[IView::IGetFirstDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstDowelSymbol.html)
[IView::GetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.html)
[IView::IGetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
