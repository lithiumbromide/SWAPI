---
title: "ChangeRenderActionHandler Delegate (SolidWorks.Visualize.Interfaces)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "ChangeRenderActionHandler"
member: ""
kind: "topic"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.ChangeRenderActionHandler.html"
---

# ChangeRenderActionHandler Delegate (SolidWorks.Visualize.Interfaces)

Obsolete. Handles render action changes.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Sub ChangeRenderActionHandler( _
   ByVal renderAction As RenderAction_e _
)
```

### Visual Basic (Usage)

```vb
Dim instance As New ChangeRenderActionHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate void ChangeRenderActionHandler(
   RenderAction_e renderAction
)
```

### C++/CLI

```cpp
public delegate void ChangeRenderActionHandler(
   RenderAction_e renderAction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndC++CLI.html).

### Parameters

- `renderAction`: Render action to handle as defined by [RenderAction_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.RenderAction_e.html)

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
