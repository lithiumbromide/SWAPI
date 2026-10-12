---
title: "GetWeldSymbolCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWeldSymbolCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbolCount.html"
---

# GetWeldSymbolCount Method (IView)

Gets the number of weld symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldSymbolCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetWeldSymbolCount()
```

### C#

```csharp
System.int GetWeldSymbolCount()
```

### C++/CLI

```cpp
System.int GetWeldSymbolCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Total number of weld symbols on this drawing view

## VBA Syntax

See [View::GetWeldSymbolCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetWeldSymbolCount.html).

## Remarks

Call this method before calling [IView::IGetWeldSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetWeldSymbols.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
