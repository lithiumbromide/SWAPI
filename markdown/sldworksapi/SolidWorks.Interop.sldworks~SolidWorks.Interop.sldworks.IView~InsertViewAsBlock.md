---
title: "InsertViewAsBlock Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertViewAsBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock.html"
---

# InsertViewAsBlock Method (IView)

Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertViewAsBlock( _
   ByVal InsertionPoint As MathPoint, _
   ByVal Position As MathPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim InsertionPoint As MathPoint
Dim Position As MathPoint
Dim value As System.Boolean

value = instance.InsertViewAsBlock(InsertionPoint, Position)
```

### C#

```csharp
System.bool InsertViewAsBlock(
   MathPoint InsertionPoint,
   MathPoint Position
)
```

### C++/CLI

```cpp
System.bool InsertViewAsBlock(
   MathPoint^ InsertionPoint,
   MathPoint^ Position
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertionPoint`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) in this view where the manipulator of the new [sketch block](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) is located
- `Position`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) on the drawing sheet where the new sketch block manipulator is positioned

### Return Value

True if the view is successfully converted to a sketch block, false if not

## VBA Syntax

See [View::InsertViewAsBlock](ms-its:sldworksapivb6.chm::/sldworks~View~InsertViewAsBlock.html).

## Examples

[Convert Drawing Views to Sketch Blocks (VBA)](Convert_Drawing_Views_to_Sketches_Example_VB.htm)
[Convert Drawing Views to Sketch Blocks (VB.NET)](Convert_Drawing_Views_to_Sketches_Example_VBNET.htm)
[Convert Drawing Views to Sketch Blocks (C#)](Convert_Drawing_Views_to_Sketches_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ReplaceViewWithBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithBlock.html)
[IView::ReplaceViewWithSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
