---
title: "_IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler.html"
---

# _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Obsolete. Superseded by [IEModelViewControlEvents::OnComponentMouseOverNotify2](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler.html)

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler( _
   ByVal ComponentName As System.String, _
   ByVal XCoordinate As System.Integer, _
   ByVal YCoordinate As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler(
   System.string ComponentName,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnComponentMouseOverNotifyEventHandler(
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

See [OnComoponentMouseOverNotify Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnComponentMouseOverNotify_EV.html).

## Availability

eDrawings API 2005 SP0
