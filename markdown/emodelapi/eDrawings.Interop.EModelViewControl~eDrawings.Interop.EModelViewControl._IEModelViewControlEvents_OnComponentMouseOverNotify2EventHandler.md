---
title: "_IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler.html"
---

# _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when the cursor is over a component.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler( _
   ByVal ComponentName As System.String, _
   ByVal ComponentConfigName As System.String, _
   ByVal XCoordinate As System.Integer, _
   ByVal YCoordinate As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler(
   System.string ComponentName,
   System.string ComponentConfigName,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnComponentMouseOverNotify2EventHandler(
   System.String^ ComponentName,
   System.String^ ComponentConfigName,
   System.int XCoordinate,
   System.int YCoordinate
)
```

### Parameters

- `ComponentName`: Component name
- `ComponentConfigName`: Component configuration name
- `XCoordinate`: x coordinate of cursor
- `YCoordinate`: y coordinate of cursor

## VBA Syntax

See [OnComponentMouseOverNotify2 Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnComponentMouseOverNotify2_EV.html).

## Availability

eDrawings API 2013 SP0
