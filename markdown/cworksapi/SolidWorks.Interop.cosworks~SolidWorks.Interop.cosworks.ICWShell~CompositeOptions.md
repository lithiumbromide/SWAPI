---
title: "CompositeOptions Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "CompositeOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~CompositeOptions.html"
---

# CompositeOptions Property (ICWShell)

Gets the options for this composite shell.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CompositeOptions As CWCompositeShellOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As CWCompositeShellOptions

value = instance.CompositeOptions
```

### C#

```csharp
CWCompositeShellOptions CompositeOptions {get;}
```

### C++/CLI

```cpp
property CWCompositeShellOptions^ CompositeOptions {
   CWCompositeShellOptions^ get();
}
```

### Property Value

[ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)

## VBA Syntax

See [CWShell::CompositeOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~CompositeOptions.html).

## Examples

[Set Composite Shell Options (VBA)](Set_Composite_Shell_Options_Example_VB.htm)
[Set Composite Shell Options (VB.NET)](Set_Composite_Shell_Options_Example_VBNET.htm)
[Set Composite Shell Options (C#)](Set_Composite_Shell_Options_Example_CSharp.htm)

## Remarks

This property is valid only if [ICWShell::Formulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html) is set to [swsShellFormulation_e.](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFormulation_e.html)swsShellFormulationComposite.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
