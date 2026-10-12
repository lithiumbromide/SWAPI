---
title: "FrameWidth Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "FrameWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html"
---

# FrameWidth Property (IModelView)

Gets or sets the width of the frame of the document window that contains the model view in the SOLIDWORKS client area.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameWidth As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.FrameWidth = value

value = instance.FrameWidth
```

### C#

```csharp
System.int FrameWidth {get; set;}
```

### C++/CLI

```cpp
property System.int FrameWidth {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of document window in client area in pixels

## VBA Syntax

See [ModelView::FrameWidth](ms-its:sldworksapivb6.chm::/sldworks~ModelView~FrameWidth.html).

## Examples

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html)
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html)
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html)
