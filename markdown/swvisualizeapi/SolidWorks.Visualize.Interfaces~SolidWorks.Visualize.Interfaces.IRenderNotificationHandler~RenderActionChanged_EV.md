---
title: "RenderActionChanged Event (IRenderNotificationHandler)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler"
member: "RenderActionChanged"
kind: "event"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler~RenderActionChanged_EV.html"
---

# RenderActionChanged Event (IRenderNotificationHandler)

Obsolete. Fire this event to cancel (or cancel and save) an on-going render.

## Syntax

### Visual Basic (Declaration)

```vb
Event RenderActionChanged As ChangeRenderActionHandler
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler
Dim handler As ChangeRenderActionHandler

AddHandler instance.RenderActionChanged, handler
```

### C#

```csharp
event ChangeRenderActionHandler RenderActionChanged
```

### C++/CLI

```cpp
event ChangeRenderActionHandler^ RenderActionChanged
```
