---
title: "RenderOptions Property (IVisualizeAddinManager2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: "RenderOptions"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~RenderOptions.html"
---

# RenderOptions Property (IVisualizeAddinManager2)

Gets various render parameters that control aspects such as the location of the output, the image file type and size, and the quality of the render.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RenderOptions As IRenderOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
Dim value As IRenderOptions

value = instance.RenderOptions
```

### C#

```csharp
IRenderOptions RenderOptions {get;}
```

### C++/CLI

```cpp
property IRenderOptions^ RenderOptions {
   IRenderOptions^ get();
}
```

### Property Value

[IRenderOptions](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)

## VBA Syntax

See [IVisualizeAddinManager::RenderOptions](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager~RenderOptions.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## See Also

[IVisualizeAddinManager2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html)
[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
