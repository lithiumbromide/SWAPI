---
title: "_IEModelViewControlEvents_OnConfigChangeEventHandler Delegate (eDrawings.Interop.EModelViewControl)"
project: "eDrawings API Help"
interface: "_IEModelViewControlEvents_OnConfigChangeEventHandler"
member: ""
kind: "topic"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnConfigChangeEventHandler.html"
---

# _IEModelViewControlEvents_OnConfigChangeEventHandler Delegate (eDrawings.Interop.EModelViewControl)

Fired when the specified configuration changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub _IEModelViewControlEvents_OnConfigChangeEventHandler( _
   ByVal ConfigId As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New _IEModelViewControlEvents_OnConfigChangeEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void _IEModelViewControlEvents_OnConfigChangeEventHandler(
   System.int ConfigId
)
```

### C++/CLI

```cpp
public delegate void _IEModelViewControlEvents_OnConfigChangeEventHandler(
   System.int ConfigId
)
```

### Parameters

- `ConfigId`: Configuration ID

## VBA Syntax

See [OnConfigChange Event (EModelViewControl).](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl._IEModelViewControlEvents_OnConfigChangeEventHandler.html)

## Availability

eDrawings 2019 SP0
