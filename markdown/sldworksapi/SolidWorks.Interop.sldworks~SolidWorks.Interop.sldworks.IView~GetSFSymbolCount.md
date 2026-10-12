---
title: "GetSFSymbolCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetSFSymbolCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbolCount.html"
---

# GetSFSymbolCount Method (IView)

Gets the number of surface finish symbols on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSFSymbolCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetSFSymbolCount()
```

### C#

```csharp
System.int GetSFSymbolCount()
```

### C++/CLI

```cpp
System.int GetSFSymbolCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Total number of surface finish symbols on this drawing view

## VBA Syntax

See [View::GetSFSymbolCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetSFSymbolCount.html).

## Examples

[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)

## Remarks

Call this method before calling [IView::IGetSFSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetSFSymbols.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetSFSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetSFSymbols.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
