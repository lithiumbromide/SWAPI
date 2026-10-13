---
title: "SetViewPosition Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetViewPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetViewPosition.html"
---

# SetViewPosition Method (IView)

Moves this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetViewPosition( _
   ByVal Position As System.Object, _
   ByVal MoveChildViews As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Position As System.Object
Dim MoveChildViews As System.Boolean
Dim value As System.Boolean

value = instance.SetViewPosition(Position, MoveChildViews)
```

### C#

```csharp
System.bool SetViewPosition(
   System.object Position,
   System.bool MoveChildViews
)
```

### C++/CLI

```cpp
System.bool SetViewPosition(
   System.Object^ Position,
   System.bool MoveChildViews
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Position`: Array of two doubles giving the new x,y position of this drawing view relative to the sheet origin (see **Remarks**)
- `MoveChildViews`: True to also move child views, false to not

### Return Value

True if view position successfully set, false if not

## VBA Syntax

See [View::SetViewPosition](ms-its:sldworksapivb6.chm::/sldworks~View~SetViewPosition.html).

## Remarks

Take careful note of view alignments when specifying Position. Any view alignments that might affect this view are handled the same way as if you were using the SOLIDWORKS Design user interface to draw the view to move it. If this view is aligned with another view, it will only be allowed to move along the alignment vector.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[DDrawingDocEvents_ViewPositionChangeNotifyEventHandler Delegate (IView)](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_ViewPositionChangeNotifyEventHandler.html)
[IView::Position Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Position.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
