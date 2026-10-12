---
title: "IGetSFSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetSFSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols.html"
---

# IGetSFSymbols Method (IView)

Gets all of the surface finish symbols in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSFSymbols( _
   ByVal NumSFSymbol As System.Integer _
) As SFSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumSFSymbol As System.Integer
Dim value As SFSymbol

value = instance.IGetSFSymbols(NumSFSymbol)
```

### C#

```csharp
SFSymbol IGetSFSymbols(
   System.int NumSFSymbol
)
```

### C++/CLI

```cpp
SFSymbol^ IGetSFSymbols(
   System.int NumSFSymbol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumSFSymbol`: Total number of surface finish symbols this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [surface finish symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of multi-jog leaders all at once instead of calling [IView::GetFirstSFSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstSFSymbol.html) and then repeatedly calling [ISFSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetNext.html) to obtain the remaining multi-jog leaders in the drawing view.

Before calling this method, call [IView::GetSFSymbolCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetSFSymbolCount.html) to get the value for numSFSymbol.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
