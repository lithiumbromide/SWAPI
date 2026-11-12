---
title: "ReplaceViewWithSketch Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ReplaceViewWithSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithSketch.html"
---

# ReplaceViewWithSketch Method (IView)

Converts this view into a sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceViewWithSketch() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.ReplaceViewWithSketch()
```

### C#

```csharp
System.bool ReplaceViewWithSketch()
```

### C++/CLI

```cpp
System.bool ReplaceViewWithSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the view is successfully replaced with a [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html), false if not

## VBA Syntax

See [View::ReplaceViewWithSketch](ms-its:sldworksapivb6.chm::/sldworks~View~ReplaceViewWithSketch.html).

## Examples

[Convert Drawing Views to Sketch Blocks (VBA)](Convert_Drawing_Views_to_Sketches_Example_VB.htm)
[Convert Drawing Views to Sketch Blocks (VB.NET)](Convert_Drawing_Views_to_Sketches_Example_VBNET.htm)
[Convert Drawing Views to Sketch Blocks (C#)](Convert_Drawing_Views_to_Sketches_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ReplaceViewWithBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ReplaceViewWithBlock.html)
[IView::InsertViewAsBlock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertViewAsBlock.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
