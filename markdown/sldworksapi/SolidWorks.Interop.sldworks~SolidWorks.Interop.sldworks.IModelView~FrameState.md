---
title: "FrameState Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "FrameState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameState.html"
---

# FrameState Property (IModelView)

Gets or sets the window state (minimum, maximum, or normal) for the frame of the document window that contains the model view in the SOLIDWORKS client area.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameState As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Integer

instance.FrameState = value

value = instance.FrameState
```

### C#

```csharp
System.int FrameState {get; set;}
```

### C++/CLI

```cpp
property System.int FrameState {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Window state as defined in [swWindowState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWindowState_e.html)

## VBA Syntax

See [ModelView::FrameState](ms-its:sldworksapivb6.chm::/sldworks~ModelView~FrameState.html).

## Examples

[Position Document Window (VBA)](Position_a_Document_Window_Example_VB.htm)
[Create Hidden Undo Object (VBA)](Create_Multiple_Undo_Command_Example_VB.htm)
[Create Hidden Undo Object (VB.NET)](Create_Multiple_Undo_Command_Example_VBNET.htm)
[Create Hidden Undo Object (C#)](Create_Multiple_Undo_Command_Example_CSharp.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::FrameHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameHeight.html)
[IModelView::FrameLeft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameLeft.html)
[IModelView::FrameTop Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameTop.html)
[IModelView::FrameWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~FrameWidth.html)
