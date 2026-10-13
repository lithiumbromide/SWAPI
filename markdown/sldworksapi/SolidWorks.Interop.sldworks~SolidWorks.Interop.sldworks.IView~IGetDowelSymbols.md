---
title: "IGetDowelSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetDowelSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols.html"
---

# IGetDowelSymbols Method (IView)

Gets all of the dowel symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDowelSymbols( _
   ByVal NumDowelSymbol As System.Integer _
) As DowelSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumDowelSymbol As System.Integer
Dim value As DowelSymbol

value = instance.IGetDowelSymbols(NumDowelSymbol)
```

### C#

```csharp
DowelSymbol IGetDowelSymbols(
   System.int NumDowelSymbol
)
```

### C++/CLI

```cpp
DowelSymbol^ IGetDowelSymbols(
   System.int NumDowelSymbol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumDowelSymbol`: Total number of dowel symbols on this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [dowel symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-Process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of dowel symbols all at once instead of calling [IView::GetFirstDowelSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDowelSymbol.html) and then repeatedly calling [IDowelSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol~GetNext.html) to obtain the remaining dowel symbols on this drawing view.

Before calling this method, call [IView::GetDowelSymbolCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetDowelSymbolCount.html) to get the value for numDowelSymbol.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
