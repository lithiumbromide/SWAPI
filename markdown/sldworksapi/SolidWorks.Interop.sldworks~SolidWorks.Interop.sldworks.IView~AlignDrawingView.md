---
title: "AlignDrawingView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "AlignDrawingView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignDrawingView.html"
---

# AlignDrawingView Method (IView)

Specifies the alignment of this auxiliary drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AlignDrawingView( _
   ByVal AlignViewType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim AlignViewType As System.Integer
Dim value As System.Boolean

value = instance.AlignDrawingView(AlignViewType)
```

### C#

```csharp
System.bool AlignDrawingView(
   System.int AlignViewType
)
```

### C++/CLI

```cpp
System.bool AlignDrawingView(
   System.int AlignViewType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AlignViewType`: Type of alignment as defined by [swAlignDrawingViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignDrawingViewTypes_e.html)

### Return Value

True if auxiliary drawing view alignment is set, false if not

## VBA Syntax

See [View::AlignDrawingView](ms-its:sldworksapivb6.chm::/sldworks~View~AlignDrawingView.html).

## Examples

[Align Auxiliary Drawing View (VBA)](Align_Auxiliary_Drawing_View_Example_VB.htm)
[Align Auxiliary Drawing View (VB.NET)](Align_Auxiliary_Drawing_View_Example_VBNET.htm)
[Align Auxiliary Drawing View (C#)](Align_Auxiliary_Drawing_View_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::AlignWithView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.html)
[IView::GetAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.html)
[IView::RemoveAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.html)
[IView::UseDefaultAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
