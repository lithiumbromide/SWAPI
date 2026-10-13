---
title: "SetCallbackHandler Method (IRenderNotificationHandler2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderNotificationHandler2"
member: "SetCallbackHandler"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2~SetCallbackHandler.html"
---

# SetCallbackHandler Method (IRenderNotificationHandler2)

Provides the handler implementation with a callback interface that can be used during asynchronous rendering to request preview images or to cancel an ongoing render.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCallbackHandler( _
   ByVal callbackHandler As IRenderCallbackHandler _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderNotificationHandler2
Dim callbackHandler As IRenderCallbackHandler

instance.SetCallbackHandler(callbackHandler)
```

### C#

```csharp
void SetCallbackHandler(
   IRenderCallbackHandler callbackHandler
)
```

### C++/CLI

```cpp
void SetCallbackHandler(
   IRenderCallbackHandler^ callbackHandler
)
```

### Parameters

- `callbackHandler`: [IRenderCallbackHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderCallbackHandler.html)

## VBA Syntax

See [IRenderNotificationHandler2::SetCallbackHandler](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderNotificationHandler2~SetCallbackHandler.html).

## Remarks

This method gets called once during the setup phase of [IVisualizeAddinManager2::StartRender2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.html). If no preview or cancellation features are needed, this method may be implemented as a no op.

## See Also

[IRenderNotificationHandler2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2.html)
[IRenderNotificationHandler2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
