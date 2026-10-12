---
title: "Milliseconds Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "Milliseconds"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Milliseconds.html"
---

# Milliseconds Property (IRenderOptions)

Gets or sets the number of milliseconds to wait before terminating the render.

## Syntax

### Visual Basic (Declaration)

```vb
Property Milliseconds As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.Long

instance.Milliseconds = value

value = instance.Milliseconds
```

### C#

```csharp
System.long Milliseconds {get; set;}
```

### C++/CLI

```cpp
property System.int64 Milliseconds {
   System.int64 get();
   void set (    System.int64 value);
}
```

### Property Value

Time limit in milliseconds; default value is 60000

## VBA Syntax

See [IRenderOptions::Milliseconds](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~Milliseconds.html).

## Remarks

This property is valid only if [IRenderOptions::TerminationMode](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~TerminationMode.html) is set to [TerminationMode_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.TerminationMode_e.html).TimeLimit.

Please note that renders with SOLIDWORKS Visualize continuously refine results by a small amount until a time limit has been reached. The appropriate setting depends on several factors such as the complexity of the model, the lighting, the appearances, the image size, whether [IRenderOptions::DenoiserEnabled](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~DenoiserEnabled.html) is true, and the desired level of final quality

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::FrameCount Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~FrameCount.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
