---
title: "ShellThickness Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellThickness"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellThickness.html"
---

# ShellThickness Property (ICWShell)

Gets or sets the shell thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShellThickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Double

instance.ShellThickness = value

value = instance.ShellThickness
```

### C#

```csharp
System.double ShellThickness {get; set;}
```

### C++/CLI

```cpp
property System.double ShellThickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness of the shell

## VBA Syntax

See [CWShell::ShellThickness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellThickness.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

This method is not valid if [ICWShell::Formulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html) is set to [swsShellFormulation_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFormulation_e.html).swsShellFormulationComposite. To set the thickness of composite shell plies, you must:

1. Use [ICWShell::CompositeOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~CompositeOptions.html) to get an instance of [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html).
2. Call [ICWCompositeShellOptions::SetPlyParameters](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html) to set a ply's thickness.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::ShellUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellUnit.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
