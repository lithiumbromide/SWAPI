---
title: "DenoiserEnabled Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "DenoiserEnabled"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~DenoiserEnabled.html"
---

# DenoiserEnabled Property (IRenderOptions)

Gets or sets whether to enable the Denoiser for the render.

## Syntax

### Visual Basic (Declaration)

```vb
Property DenoiserEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Boolean

instance.DenoiserEnabled = value

value = instance.DenoiserEnabled
```

### C#

```csharp
System.bool DenoiserEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool DenoiserEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to enable denoiser, false (default) to not

## VBA Syntax

See [IRenderOptions::DenoiserEnabled](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~DenoiserEnabled.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

Setting this property to true:

- enables the usage of the AI-accelerated Denoiser to render an image.
- significantly reduces the number of frames and/or the time required to create a high-quality and noise-free render by about 1/10.
- may lead to unwanted artifacts.

For more information, see the **SOLIDWORKS Web Help > SOLIDWORKS Visualize Help > Working with 3D Models > Denoiser**.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::FrameCount Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~FrameCount.html)
[IRenderOptions::Milliseconds Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Milliseconds.html)
[IRenderOptions::TerminationMode Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~TerminationMode.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
