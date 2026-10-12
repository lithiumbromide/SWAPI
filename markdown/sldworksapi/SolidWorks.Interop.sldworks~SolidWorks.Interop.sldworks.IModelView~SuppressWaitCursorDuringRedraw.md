---
title: "SuppressWaitCursorDuringRedraw Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "SuppressWaitCursorDuringRedraw"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SuppressWaitCursorDuringRedraw.html"
---

# SuppressWaitCursorDuringRedraw Property (IModelView)

Gets or sets the state of the wait cursor (also called the hourglass) while this model view is being redrawn.

## Syntax

### Visual Basic (Declaration)

```vb
Property SuppressWaitCursorDuringRedraw As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.SuppressWaitCursorDuringRedraw = value

value = instance.SuppressWaitCursorDuringRedraw
```

### C#

```csharp
System.bool SuppressWaitCursorDuringRedraw {get; set;}
```

### C++/CLI

```cpp
property System.bool SuppressWaitCursorDuringRedraw {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable the wait cursor, false to disable it

## VBA Syntax

See [ModelView::SuppressWaitCursorDuringRedraw](ms-its:sldworksapivb6.chm::/sldworks~ModelView~SuppressWaitCursorDuringRedraw.html).

## Examples

[Disable Wait Cursor When Model View Redrawn (VBA)](Disable_Wait_Cursor_While_Model_View_Redrawn_VB.htm)

## Remarks

When a model view is being redrawn, the wait cursor is normally displayed. This property allows you to suppress the wait cursor.

An add-in might find this property useful in situations where it is running a series of APIs, and one or more of those APIs cause the model view to redraw. By default, redrawing the model causes the wait cursor to flash on and off, which the end user may find disconcerting. By setting this property to false, the flashing wait cursor is suppressed. [IModelDoc::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html) is the most common API that causes a model view to redraw.

If your program disables this property, then it should re-enable it when the operation for which it was disabled completes. Otherwise, SOLIDWORKS will continue to not display the wait cursor. In other words, the expected use of this property is that you should disable it for a specific operation (or set of operations) in your code, and then immediately restore its previous behavior when that operation is completed.

Use of this property does not affect SOLIDWORKS performance.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::GraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html)
[IModelView::IGraphicsRedraw Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGraphicsRedraw.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
