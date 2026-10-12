---
title: "ImageFormat Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "ImageFormat"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~ImageFormat.html"
---

# ImageFormat Property (IRenderOptions)

Gets or sets the image format of the rendered output.

## Syntax

### Visual Basic (Declaration)

```vb
Property ImageFormat As ImageFormat_e
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As ImageFormat_e

instance.ImageFormat = value

value = instance.ImageFormat
```

### C#

```csharp
ImageFormat_e ImageFormat {get; set;}
```

### C++/CLI

```cpp
property ImageFormat_e ImageFormat {
   ImageFormat_e get();
   void set (    ImageFormat_e value);
}
```

### Property Value

Image format as defined by [ImageFormat_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.ImageFormat_e.html); default is ImageFormat_e.PNG

## VBA Syntax

See [IRenderOptions::ImageFormat](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~ImageFormat.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

If this property is set to ImageFormat_e.JPEG, then [IRenderOptions::IncludeAlpha](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~IncludeAlpha.html) is not valid.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
