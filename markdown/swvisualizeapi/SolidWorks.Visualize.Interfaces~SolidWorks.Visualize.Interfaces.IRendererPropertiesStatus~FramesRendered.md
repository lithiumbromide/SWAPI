---
title: "FramesRendered Property (IRendererPropertiesStatus)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus"
member: "FramesRendered"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus~FramesRendered.html"
---

# FramesRendered Property (IRendererPropertiesStatus)

Gets the number of rendered frames.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FramesRendered As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus
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

[IRendererPropertiesStatus Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus.html)
[IRendererPropertiesStatus Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
