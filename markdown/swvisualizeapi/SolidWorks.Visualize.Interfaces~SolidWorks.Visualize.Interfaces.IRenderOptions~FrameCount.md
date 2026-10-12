---
title: "FrameCount Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "FrameCount"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~FrameCount.html"
---

# FrameCount Property (IRenderOptions)

Gets or sets the maximum frame count at which to terminate the render.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrameCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Integer

instance.FrameCount = value

value = instance.FrameCount
```

### C#

```csharp
System.int FrameCount {get; set;}
```

### C++/CLI

```cpp
property System.int FrameCount {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Maximum frame count; default value is 100

## VBA Syntax

See [IRenderOptions::FrameCount](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~FrameCount.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

This property is valid only if [IRenderOptions::TerminationMode](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~TerminationMode.html) is set to [TerminationMode](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.TerminationMode.html).QualityLevel

The frame count has a significant influence on the overall render time.

Please note that renders with SOLIDWORKS Visualize continuously refine results by a small amount until a maximum frame count has been reached. The appropriate setting depends on several factors such as the complexity of the model, the lighting, the appearances, the image size, whether [IRenderOptions::DenoiserEnabled](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~DenoiserEnabled.html) is true, and the desired level of final quality.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::Milliseconds Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Milliseconds.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
