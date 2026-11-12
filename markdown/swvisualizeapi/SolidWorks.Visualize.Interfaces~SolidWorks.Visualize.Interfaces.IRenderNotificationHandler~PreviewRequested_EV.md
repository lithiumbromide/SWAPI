---
title: "PreviewRequested Event (IRenderNotificationHandler)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler"
member: "PreviewRequested"
kind: "event"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler~PreviewRequested_EV.html"
---

# PreviewRequested Event (IRenderNotificationHandler)

Obsolete. Fire this event to request a preview image during an on-going render.

## Syntax

### Visual Basic (Declaration)

```vb
Event PreviewRequested As PreviewRequestHandler
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler
Dim handler As PreviewRequestHandler

AddHandler instance.PreviewRequested, handler
```

### C#

```csharp
event PreviewRequestHandler PreviewRequested
```

### C++/CLI

```cpp
event PreviewRequestHandler^ PreviewRequested
```
