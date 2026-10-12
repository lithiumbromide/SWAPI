---
title: "ElapsedTime Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "ElapsedTime"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~ElapsedTime.html"
---

# ElapsedTime Property (IRendererPropertiesStatus2)

Gets the elapsed render time.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ElapsedTime As System.TimeSpan
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
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

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
