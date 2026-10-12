---
title: "FrameTop Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "FrameTop"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html"
---

# FrameTop Property (IModelView)

Gets or sets the top position of the frame of the document window that contains the model view in the SOLIDWORKS client area.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameTop As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.FrameTop = value

value = instance.FrameTop
```

### C#

```csharp
System.int FrameTop {get; set;}
```

### C++/CLI

```cpp
property System.int FrameTop {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Top position of document window in client area in pixels

## VBA Syntax

See [ModelView::FrameTop](ms-its:sldworksapivb6.chm::/sldworks~ModelView~FrameTop.html).

## Examples

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html)
[IModelView::FrameState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html)
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html)
