---
title: "FramesRendered Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "FramesRendered"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~FramesRendered.html"
---

# FramesRendered Property (IRendererPropertiesStatus2)

Gets the number of rendered frames.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FramesRendered As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
Dim value As System.Integer

value = instance.FramesRendered
```

### C#

```csharp
System.int FramesRendered {get;}
```

### C++/CLI

```cpp
property System.int FramesRendered {
   System.int get();
}
```

### Property Value

Number of rendered frames

## VBA Syntax

See [IRendererPropertiesStatus::FramesRendered](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus~FramesRendered.html).

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
