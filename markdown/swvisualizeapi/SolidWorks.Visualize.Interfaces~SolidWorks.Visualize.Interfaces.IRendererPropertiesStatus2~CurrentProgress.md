---
title: "CurrentProgress Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "CurrentProgress"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~CurrentProgress.html"
---

# CurrentProgress Property (IRendererPropertiesStatus2)

Gets the current progress.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProgress As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
Dim value As System.Single

value = instance.CurrentProgress
```

### C#

```csharp
System.float CurrentProgress {get;}
```

### C++/CLI

```cpp
property System.float CurrentProgress {
   System.float get();
}
```

### Property Value

Current progress

## VBA Syntax

See [IRendererPropertiesStatus::CurrentProgress](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus~CurrentProgress.html).

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
