---
title: "_IEModelViewControlEvents_OnModifySceneEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnModifySceneEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnModifySceneEventHandler.html"
---

# _IEModelViewControlEvents_OnModifySceneEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when a scene is modified.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnModifySceneEventHandler( _
   ByVal ModifyEvent As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnModifySceneEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnModifySceneEventHandler(
   System.int ModifyEvent
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnModifySceneEventHandler(
   System.int ModifyEvent
)
```

### Parameters

- `ModifyEvent`: Modification event bitmask:

  - 1 or 0x001 = Hide/Show
  - 2 or 0x002 = Rotate
  - 4 or 0x004 = Pan
  - 8 or 0x008 = Zoom
  - 16 or 0x010 = MakeTransparent
  - 32 or 0x020 = Next
  - 64 or 0x040 = Projection
  - 128 or 0x080 = LayerChange
  - 256 or 0x100 = DisplayStateChange

## VBA Syntax

See [OnModifyScene Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnModifyScene_EV.html).

## Availability

eDrawings API 2015 SP0
