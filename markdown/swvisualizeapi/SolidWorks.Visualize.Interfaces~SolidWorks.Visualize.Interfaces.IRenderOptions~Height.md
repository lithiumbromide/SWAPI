---
title: "Height Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "Height"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Height.html"
---

# Height Property (IRenderOptions)

Gets or sets the reference height of the render output.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Integer

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.int Height {get; set;}
```

### C++/CLI

```cpp
property System.int Height {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Height in pixels; default is 1080

## VBA Syntax

See [IRenderOptions::Height](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~Height.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

The total number of pixels has a significant influence on the overall render complexity and time needed to complete the render.

The actual width depends on the aspect ratio (width/height) of the camera in SOLIDWORKS or 11/8.5 for SOLIDWORKS views that do not define an aspect ratio.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::Width Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Width.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
