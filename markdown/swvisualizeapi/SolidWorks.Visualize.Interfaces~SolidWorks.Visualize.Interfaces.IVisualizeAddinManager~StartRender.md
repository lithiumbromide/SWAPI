---
title: "StartRender Method (IVisualizeAddinManager)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager"
member: "StartRender"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~StartRender.html"
---

# StartRender Method (IVisualizeAddinManager)

Obsolete. Superseded by [IVisualizeAddinManager2::StartRender2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function StartRender( _
   Optional ByVal renderNotificationHandler As IRenderNotificationHandler _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager
Dim renderNotificationHandler As IRenderNotificationHandler
Dim value As System.Boolean

value = instance.StartRender(renderNotificationHandler)
```

### C#

```csharp
System.bool StartRender(
   IRenderNotificationHandler renderNotificationHandler
)
```

### C++/CLI

```cpp
System.bool StartRender(
   IRenderNotificationHandler^ renderNotificationHandler
)
```

### Parameters

- `renderNotificationHandler`: [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html)

### Return Value

True if the render is successful, false if not

## VBA Syntax

See [IVisualizeAddinManager::StartRender](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager~StartRender.html).

## Remarks

This method starts a render and returns before the render is finished (asynchronous blocking).

Use [IVisualizeAddinManager::Render](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~Render.html) for synchronous blocking.

## See Also

[IVisualizeAddinManager Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html)
[IVisualizeAddinManager Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
