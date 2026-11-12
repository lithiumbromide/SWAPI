---
title: "_IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler.html"
---

# _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Obsolete. Superseded by [IEModelViewControlEvent OnComponentSelectionNotify2](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnComponentSelectionNotify2EventHandler.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler( _
   ByVal ComponentName As System.String, _
   ByVal XCoordinate As System.Integer, _
   ByVal YCoordinate As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler(
   System.string ComponentName,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnComponentSelectionNotifyEventHandler(
   System.String^ ComponentName,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### Parameters

- `ComponentName`: Component name
- `XCoordinate`: x coordinate of cursor
- `YCoordinate`: y coordinate of cursor

## VBA Syntax

See [OnComponentSelectionNotify Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnComponentSelectionNotify_EV.html).

## Examples

##### VB.NET example:

```vb
Private Sub AxEModelViewControl1_OnComponentSelectionNotify(ByVal sender As System.Object, ByVal e As AxEModelView._IEModelViewControlEvents_OnComponentSelectionNotifyEvent) Handles AxEModelViewControl1.OnComponentSelectionNotify
'' Access the event arguments
e.ComponentName
e.XCoordinate
e.YCoordinate
End Sub
```

## Availability

eDrawings API 2005 SP0
