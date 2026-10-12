---
title: "IncludeAlpha Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "IncludeAlpha"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~IncludeAlpha.html"
---

# IncludeAlpha Property (IRenderOptions)

Gets or sets whether to export transparency information in the alpha channel of the rendered image(s).

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeAlpha As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Boolean

instance.IncludeAlpha = value

value = instance.IncludeAlpha
```

### C#

```csharp
System.bool IncludeAlpha {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeAlpha {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include alpha channel, false (default) to not

## VBA Syntax

See [IRenderOptions::IncludeAlpha](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~IncludeAlpha.html).

## Remarks

This property is valid only if If [IRenderOptions::ImageFormat](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~ImageFormat.html) is not set to [ImageFormat_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.ImageFormat_e.html).JPEG.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
