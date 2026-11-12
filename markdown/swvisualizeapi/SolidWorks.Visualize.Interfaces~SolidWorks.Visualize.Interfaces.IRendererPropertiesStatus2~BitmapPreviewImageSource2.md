---
title: "BitmapPreviewImageSource2 Property (IRendererPropertiesStatus2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRendererPropertiesStatus2"
member: "BitmapPreviewImageSource2"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2~BitmapPreviewImageSource2.html"
---

# BitmapPreviewImageSource2 Property (IRendererPropertiesStatus2)

Gets the bitmap preview image source.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BitmapPreviewImageSource2 As IBitmapImageSource
```

### Visual Basic (Usage)

```vb
Dim instance As IRendererPropertiesStatus2
Dim value As IBitmapImageSource

value = instance.BitmapPreviewImageSource2
```

### C#

```csharp
IBitmapImageSource BitmapPreviewImageSource2 {get;}
```

### C++/CLI

```cpp
property IBitmapImageSource^ BitmapPreviewImageSource2 {
   IBitmapImageSource^ get();
}
```

### Property Value

System.Windows.Media.Imaging.BitmapSource

## VBA Syntax

See [IRendererPropertiesStatus2::BitmapPreviewImageSource](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRendererPropertiesStatus2~BitmapPreviewImageSource.html).

## See Also

[IRendererPropertiesStatus2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2.html)
[IRendererPropertiesStatus2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRendererPropertiesStatus2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
