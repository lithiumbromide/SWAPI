---
title: "TerminationMode Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "TerminationMode"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~TerminationMode.html"
---

# TerminationMode Property (IRenderOptions)

Gets or sets the criteria used to decide when a render is terminated.

## Syntax

### Visual Basic (Declaration)

```vb
Property TerminationMode As TerminationMode_e
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As TerminationMode_e

instance.TerminationMode = value

value = instance.TerminationMode
```

### C#

```csharp
TerminationMode_e TerminationMode {get; set;}
```

### C++/CLI

```cpp
property TerminationMode_e TerminationMode {
   TerminationMode_e get();
   void set (    TerminationMode_e value);
}
```

### Property Value

Termination mode as defined by [TerminationMode_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.TerminationMode_e.html)

## VBA Syntax

See [IRenderOptions::TerminationMode](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~TerminationMode.html).

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)
[IRenderOptions::FrameCount Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~FrameCount.html)
[IRenderOptions::Milliseconds Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~Milliseconds.html)
[IRenderOptions::DenoiserEnabled Property ()](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~DenoiserEnabled.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
