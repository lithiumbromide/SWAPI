---
title: "GetSFSymbols Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSFSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.html"
---

# GetSFSymbols Method (IView)

Gets all of the surface finish symbols in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSFSymbols() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetSFSymbols()
```

### C#

```csharp
System.object GetSFSymbols()
```

### C++/CLI

```cpp
System.Object^ GetSFSymbols();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [surface finish symbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol.html)

## VBA Syntax

See [View::GetSFSymbols](ms-its:sldworksapivb6.chm::/sldworks~View~GetSFSymbols.html).

## Examples

[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Use this method to obtain the array of surface finish symbols all at once instead of calling [IView::GetFirstSFSymbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstSFSymbol.html) and then repeatedly calling [ISFSymbol::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISFSymbol~GetNext.html) to obtain the remaining surface finish symbols in the drawing view.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSFSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbolCount.html)
[IView::IGetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetSFSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
