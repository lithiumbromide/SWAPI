---
title: "GetWeldSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetWeldSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbols.html"
---

# GetWeldSymbols Method (IView)

Gets all of the weld symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWeldSymbols() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetWeldSymbols()
```

### C#

```csharp
System.object GetWeldSymbols()
```

### C++/CLI

```cpp
System.Object^ GetWeldSymbols();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [weld symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol.html)

## VBA Syntax

See [View::GetWeldSymbols](ms-its:sldworksapivb6.chm::/sldworks~View~GetWeldSymbols.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

This method can be used to obtain the array of annotations all at once instead of calling [IView::GetFirstWeldSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstWeldSymbol.html) and then repeatedly calling [IWeldSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldSymbol~GetNext.html) to obtain the annotations.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetWeldSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetWeldSymbolCount.html)
[IView::IGetWeldSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetWeldSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
