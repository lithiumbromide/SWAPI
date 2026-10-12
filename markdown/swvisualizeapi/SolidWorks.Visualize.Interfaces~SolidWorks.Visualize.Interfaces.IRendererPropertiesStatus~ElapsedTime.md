---
title: "ElapsedTime Property (IRendererPropertiesStatus)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus"
member: "ElapsedTime"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus~ElapsedTime.html"
---

# ElapsedTime Property (IRendererPropertiesStatus)

Gets the elapsed render time.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ElapsedTime As System.TimeSpan
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus
Dim value As System.TimeSpan

value = instance.ElapsedTime
```

### C#

```csharp
System.TimeSpan ElapsedTime {get;}
```

### C++/CLI

```cpp
property System.TimeSpan ElapsedTime {
   System.TimeSpan get();
}
```

### Property Value

Elapsed render System.TimeSpan

## VBA Syntax

See [IRendererPropertiesStatus::ElapsedTime](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus~ElapsedTime.html).

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[IRendererPropertiesStatus Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus.html)
[IRendererPropertiesStatus Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
