---
title: "GetDowelSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetDowelSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbols.html"
---

# GetDowelSymbols Method (IView)

Gets all of the dowel symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDowelSymbols() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetDowelSymbols()
```

### C#

```csharp
System.object GetDowelSymbols()
```

### C++/CLI

```cpp
System.Object^ GetDowelSymbols();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [dowel symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [View::GetDowelSymbols](ms-its:sldworksapivb6.chm::/sldworks~View~GetDowelSymbols.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

Use this method to obtain the array of dowel symbols all at once instead of calling [IView::GetFirstDowelSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstDowelSymbol.html) and then repeatedly calling [IDowelSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol~GetNext.html) to obtain the remaining dowel symbols on this drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetDowelSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDowelSymbolCount.html)
[IView::IGetDowelSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetDowelSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
