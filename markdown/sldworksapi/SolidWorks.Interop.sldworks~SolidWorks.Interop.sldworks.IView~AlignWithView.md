---
title: "AlignWithView Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "AlignWithView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.html"
---

# AlignWithView Method (IView)

Sets view alignment.

## Syntax

### Visual Basic (Declaration)

```vb
Function AlignWithView( _
   ByVal AlignType As System.Integer, _
   ByVal BaseView As View _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim AlignType As System.Integer
Dim BaseView As View
Dim value As System.Boolean

value = instance.AlignWithView(AlignType, BaseView)
```

### C#

```csharp
System.bool AlignWithView(
   System.int AlignType,
   View BaseView
)
```

### C++/CLI

```cpp
System.bool AlignWithView(
   System.int AlignType,
   View^ BaseView
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AlignType`: Type of alignment to set as defined by [swAlignViewTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAlignViewTypes_e.html)
- `BaseView`: [View](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html) with which to align, if aligning with another view

### Return Value

True if view alignment is set, false if not

## VBA Syntax

See [View::AlignWithView](ms-its:sldworksapivb6.chm::/sldworks~View~AlignWithView.html).

## Examples

[Align Drawing Views (C#)](Align_Drawing_Views_Example_CSharp.htm)
[Align Drawing Views (VB.NET)](Align_Drawing_Views_Example_VBNET.htm)
[Align Drawing Views (VBA)](Align_Drawing_Views_Example_VB.htm)

## Remarks

AlignType tells how to align this view.

| If AlignType is set to... | Then BaseView... |
| --- | --- |
| swAlignViewHorizontalCenter | must be specified as the view with which to align. |
| swAlignViewVerticalCenter | must be specified as the view with which to align. |
| swAlignViewHorizontalOrigin | must be specified as the view with which to align. |
| swAlignViewVerticalOrigin | must be specified as the view with which to align. |
| swNoViewAlignment | is ignored. |
| swDefaultViewAlignment | is ignored. |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.html)
[IView::RemoveAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.html)
[IView::UseDefaultAlignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.html)
[IView::AlignDrawingView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignDrawingView.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
