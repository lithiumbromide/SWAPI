---
title: "BitmapPreviewImageSource Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "BitmapPreviewImageSource"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~BitmapPreviewImageSource.html"
---

# BitmapPreviewImageSource Property (IRendererPropertiesStatus2)

Obsolete. Superseded by [IRendererPropertiesStatus2::BitmapPreviewImageSource2](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~BitmapPreviewImageSource2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BitmapPreviewImageSource As System.Windows.Media.Imaging.BitmapSource
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
Dim value As System.Windows.Media.Imaging.BitmapSource

value = instance.BitmapPreviewImageSource
```

### C#

```csharp
System.Windows.Media.Imaging.BitmapSource BitmapPreviewImageSource {get;}
```

### C++/CLI

```cpp
property System.Windows.Media.Imaging.BitmapSource^ BitmapPreviewImageSource {
   System.Windows.Media.Imaging.BitmapSource^ get();
}
```

### Property Value

System.Windows.Media.Imaging.BitmapSource

## VBA Syntax

See [IRendererPropertiesStatus::BitmapPreviewImageSource](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus~BitmapPreviewImageSource.html).

## Examples

See the [IRenderNotificationHandler](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderNotificationHandler.html) example.

## See Also

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
