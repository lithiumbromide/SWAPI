---
title: "FrameLeft Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "FrameLeft"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html"
---

# FrameLeft Property (IModelView)

Gets or sets the left position of the frame of the document window that contains the model view in the SOLIDWORKS client area.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameLeft As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.FrameLeft = value

value = instance.FrameLeft
```

### C#

```csharp
System.int FrameLeft {get; set;}
```

### C++/CLI

```cpp
property System.int FrameLeft {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Left position of document window in client area in pixels

## VBA Syntax

See [ModelView::FrameLeft](ms-its:sldworksapivb6.chm::/sldworks~ModelView~FrameLeft.html).

## Examples

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html)
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html)
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html)
