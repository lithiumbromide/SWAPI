---
title: "GetDowelSymbolCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDowelSymbolCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbolCount.html"
---

# GetDowelSymbolCount Method (IView)

Gets the number of dowel symbols in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDowelSymbolCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetDowelSymbolCount()
```

### C#

```csharp
System.int GetDowelSymbolCount()
```

### C++/CLI

```cpp
System.int GetDowelSymbolCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of dowel symbols

## VBA Syntax

See [View::GetDowelSymbolCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetDowelSymbolCount.html)

## Remarks

Call this method before calling [IView::IGetDowelSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetDowelSymbols.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
