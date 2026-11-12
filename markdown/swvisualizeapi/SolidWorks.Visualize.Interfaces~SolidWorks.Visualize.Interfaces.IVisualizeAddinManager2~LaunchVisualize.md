---
title: "LaunchVisualize Method (IVisualizeAddinManager2)"
project: "SOLIDWORKS Visualize Add-in API Help"
interface: "IVisualizeAddinManager2"
member: "LaunchVisualize"
kind: "method"
source: "swvisualizeapi/SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2~LaunchVisualize.html"
---

# LaunchVisualize Method (IVisualizeAddinManager2)

Launches the latest installed version of SOLIDWORKS Visualize and optionally opens a project file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub LaunchVisualize( _
   ByVal filename As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IVisualizeAddinManager2
Dim filename As System.String

instance.LaunchVisualize(filename)
```

### C#

```csharp
void LaunchVisualize(
   System.string filename
)
```

### C++/CLI

```cpp
void LaunchVisualize(
   System.String^ filename
)
```

### Parameters

- `filename`: Full pathname to the .SVPJ file to open on launch; null or Nothing to open Visualize without loading a project (see **Remarks**)

## VBA Syntax

See [IVisualizeAddinManager2::LaunchVisualize](ms-its:swvisualizeapivb6.chm::/SolidWorks_Visualize_Interfaces~IVisualizeAddinManager2~LaunchVisualize.html).

## Remarks

If filename is an invalid path, an error message displays.

## See Also

[IVisualizeAddinManager2 Interface](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2.html)
[IVisualizeAddinManager2 Members](SolidWorks.Visualize.Interfaces~SolidWorks.Visualize.Interfaces.IVisualizeAddinManager2_members.html)

## Availability

SOLIDWORKS Visualize Add-in API 2026 FCS
