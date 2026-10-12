---
title: "StartRender2 Method (IVisualizeAddinManager2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: "StartRender2"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~StartRender2.html"
---

# StartRender2 Method (IVisualizeAddinManager2)

Renders asynchronously.

## Syntax

### Visual Basic (Declaration)

```vb
Function StartRender2( _
   ByVal renderNotificationHandler As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
Dim renderNotificationHandler As System.Object
Dim value As System.Boolean

value = instance.StartRender2(renderNotificationHandler)
```

### C#

```csharp
System.bool StartRender2(
   System.object renderNotificationHandler
)
```

### C++/CLI

```cpp
System.bool StartRender2(
   System.Object^ renderNotificationHandler
)
```

### Parameters

- `renderNotificationHandler`: [IRenderNotificationHandler2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler2.html) object (see **Remarks**)

### Return Value

True if the render is successful, false if not

## VBA Syntax

See [IVisualizeAddinManager2::StartRender2](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager2~StartRender2.html).

## Remarks

This method starts a render and returns before the render is complete.

## See Also

[IVisualizeAddinManager2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html)
[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
