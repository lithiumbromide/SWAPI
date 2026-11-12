---
title: "IGetWeldSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetWeldSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldSymbols.html"
---

# IGetWeldSymbols Method (IView)

Gets all of the weld symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetWeldSymbols( _
   ByVal NumWeldSymbol As System.Integer _
) As WeldSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumWeldSymbol As System.Integer
Dim value As WeldSymbol

value = instance.IGetWeldSymbols(NumWeldSymbol)
```

### C#

```csharp
WeldSymbol IGetWeldSymbols(
   System.int NumWeldSymbol
)
```

### C++/CLI

```cpp
WeldSymbol^ IGetWeldSymbols(
   System.int NumWeldSymbol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumWeldSymbol`: Total number of weld symbols on this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [weld symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of weld symbols all at once instead of calling [IView::GetFirstWeldSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstWeldSymbol.html) and then repeatedly calling [IWeldSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetNext.html) to obtain the weld symbols in the drawing view.

Before calling this method, call [IView::GetWeldSymbolCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetWeldSymbolCount.html) to get the value for numWeldSymbol.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
