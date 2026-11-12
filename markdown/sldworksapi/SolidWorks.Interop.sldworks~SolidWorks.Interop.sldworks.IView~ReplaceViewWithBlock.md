---
title: "ReplaceViewWithBlock Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ReplaceViewWithBlock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithBlock.html"
---

# ReplaceViewWithBlock Method (IView)

Converts this view into a sketch block with the specified manipulator location.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceViewWithBlock( _
   ByVal InsertionPoint As MathPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim InsertionPoint As MathPoint
Dim value As System.Boolean

value = instance.ReplaceViewWithBlock(InsertionPoint)
```

### C#

```csharp
System.bool ReplaceViewWithBlock(
   MathPoint InsertionPoint
)
```

### C++/CLI

```cpp
System.bool ReplaceViewWithBlock(
   MathPoint^ InsertionPoint
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertionPoint`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) in this view where the manipulator of the new [sketch block](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockInstance.html) is located

### Return Value

True if the view is successfully replaced with a sketch block, false if not

## VBA Syntax

See [View::ReplaceViewWithBlock](ms-its:sldworksapivb6.chm::/sldworks~View~ReplaceViewWithBlock.html).

## Examples

[Convert Drawing Views to Sketch Blocks (VBA)](Convert_Drawing_Views_to_Sketches_Example_VB.htm)
[Convert Drawing Views to Sketch Blocks (VB.NET)](Convert_Drawing_Views_to_Sketches_Example_VBNET.htm)
[Convert Drawing Views to Sketch Blocks (C#)](Convert_Drawing_Views_to_Sketches_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::InsertViewAsBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock.html)
[IView::ReplaceViewWithSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
