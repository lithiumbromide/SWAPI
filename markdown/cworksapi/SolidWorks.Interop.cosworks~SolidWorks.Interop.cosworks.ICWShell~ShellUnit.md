---
title: "ShellUnit Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "ShellUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellUnit.html"
---

# ShellUnit Property (ICWShell)

Gets or sets the units for the shell thickness.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShellUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Integer

instance.ShellUnit = value

value = instance.ShellUnit
```

### C#

```csharp
System.int ShellUnit {get; set;}
```

### C++/CLI

```cpp
property System.int ShellUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Linear unit as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWShell::ShellUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~ShellUnit.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

This method is not valid if [ICWShell::Formulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html) is set to [swsShellFormulation_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFormulation_e.html).swsShellFormulationComposite. To set the length units of composite laminates, you must:

1. Use [ICWShell::CompositeOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~CompositeOptions.html) to get an instance of [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html).
2. Call [ICWCompositeShellOptions::LengthUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~LengthUnit.html) to set a composite laminate's units of length.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::ShellThickness Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~ShellThickness.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
