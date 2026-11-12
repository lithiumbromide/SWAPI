---
title: "CurrentProgress Property (IRendererPropertiesStatus)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus"
member: "CurrentProgress"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus~CurrentProgress.html"
---

# CurrentProgress Property (IRendererPropertiesStatus)

Gets the current progress.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CurrentProgress As System.Single
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus
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

[IRendererPropertiesStatus Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus.html)
[IRendererPropertiesStatus Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
