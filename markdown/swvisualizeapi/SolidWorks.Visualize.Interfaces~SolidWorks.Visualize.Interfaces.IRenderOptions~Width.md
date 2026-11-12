---
title: "Width Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "Width"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Width.html"
---

# Width Property (IRenderOptions)

Gets or sets the reference width of the render output.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Integer

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.int Width {get; set;}
```

### C++/CLI

```cpp
property System.int Width {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Width in pixels; default is 1920

## VBA Syntax

See [IRenderOptions::Width](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~Width.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

The total number of pixels has a significant influence on the overall render complexity and time needed to complete the render.

The actual width depends on the aspect ratio (width/height) of the camera in SOLIDWORKS or 11/8.5 for SOLIDWORKS views that do not define an aspect ratio.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::Height Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Height.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
