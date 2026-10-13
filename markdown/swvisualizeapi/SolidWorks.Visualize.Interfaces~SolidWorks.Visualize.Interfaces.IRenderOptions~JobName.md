---
title: "JobName Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "JobName"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~JobName.html"
---

# JobName Property (IRenderOptions)

Gets or sets the subfolder and filename of the rendered output.

## Syntax

### Visual Basic (Declaration)

```vb
Property JobName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.String

instance.JobName = value

value = instance.JobName
```

### C#

```csharp
System.string JobName {get; set;}
```

### C++/CLI

```cpp
property System.String^ JobName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Render job name; default is the name of the SOLIDWORKS model

## VBA Syntax

See [IRenderOptions::JobName](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~JobName.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

[IRenderOptions::OutputFolder](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~OutputFolder.html) specifies the path to the folder where the rendered output should be saved to.

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
