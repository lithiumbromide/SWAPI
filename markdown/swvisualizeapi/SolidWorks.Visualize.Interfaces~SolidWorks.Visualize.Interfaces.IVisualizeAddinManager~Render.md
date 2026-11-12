---
title: "Render Method (IVisualizeAddinManager)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager"
member: "Render"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~Render.html"
---

# Render Method (IVisualizeAddinManager)

Renders synchronously.

## Syntax

### Visual Basic (Declaration)

```vb
Function Render() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager
Dim value As System.Boolean

value = instance.Render()
```

### C#

```csharp
System.bool Render()
```

### C++/CLI

```cpp
System.bool Render();
```

### Return Value

True if the render is successful, false if not

## VBA Syntax

See [IVisualizeAddinManager::Render](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager~Render.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

This method blocks until the render is finished. Use [IVisualizeAddinManager::StartRender](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~StartRender.html) for asynchronous blocking.

Depending on the choice of [IVisualizeAddinManager::RenderOptions](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager~RenderOptions.html) and the available hardware, a render can take a long time to finish.

## See Also

[IVisualizeAddinManager Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html)
[IVisualizeAddinManager Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
