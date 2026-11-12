---
title: "_IEModelViewControlEvents_OnNamedViewEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnNamedViewEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnNamedViewEventHandler.html"
---

# _IEModelViewControlEvents_OnNamedViewEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when a named view has been selected.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnNamedViewEventHandler( _
   ByVal NamedViewId As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnNamedViewEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnNamedViewEventHandler(
   System.int NamedViewId
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnNamedViewEventHandler(
   System.int NamedViewId
)
```

### Parameters

- `NamedViewId`: Named views:

  - 0xDDDD = Front View
  - 0xDDDE = Back view
  - 0xDDDF = Left view
  - 0xDDED = Right view
  - 0xDDEE = Top view
  - 0xDDEF = Bottom view
  - 0xDDFD = Isometric view
  - 0xDDFE = Normal view

## VBA Syntax

See [OnNamedView Event (EModelViewControl)](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~OnNamedView_EV.html).

## Availability

eDrawings API 2014 SP1
