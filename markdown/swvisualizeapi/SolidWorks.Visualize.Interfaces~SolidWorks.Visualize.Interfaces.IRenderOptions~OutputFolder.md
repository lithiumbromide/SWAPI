---
title: "OutputFolder Property (IRenderOptions)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IRenderOptions"
member: "OutputFolder"
kind: "property"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~OutputFolder.html"
---

# OutputFolder Property (IRenderOptions)

Gets or sets the path to the folder to which the rendered output should be saved.

## Syntax

### Visual Basic (Declaration)

```vb
Property OutputFolder As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderOptions
Dim value As System.String

instance.OutputFolder = value

value = instance.OutputFolder
```

### C#

```csharp
System.string OutputFolder {get; set;}
```

### C++/CLI

```cpp
property System.String^ OutputFolder {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Render output folder (see **Remarks**)

## VBA Syntax

See [IRenderOptions::OutputFolder](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IRenderOptions~OutputFolder.html).

## Examples

See the [IVisualizeAddinManager](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager.html) examples.

## Remarks

The full path name of the output is:

`render_output_folder`\`job_name`\`job_name.extension`

where:

`render_output_folder` = Typically **USERPROFILE**\Documents\SOLIDWORKS Visualize Content\Images

`job_name` = Use [IRenderOptions::JobName](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions~JobName.html) to specify this; by default it is the SOLIDWORKS model name

extension = Image format as defined by [ImageFormat_e](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.ImageFormat_e.html)

## See Also

[IRenderOptions Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions.html)
[IRenderOptions Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IRenderOptions_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2025 FCS
