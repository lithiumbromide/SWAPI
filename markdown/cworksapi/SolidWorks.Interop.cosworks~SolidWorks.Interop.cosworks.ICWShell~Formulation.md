---
title: "Formulation Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "Formulation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html"
---

# Formulation Property (ICWShell)

Gets or sets the formulation type for the shell.

## Syntax

### Visual Basic (Declaration)

```vb
Property Formulation As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim value As System.Integer

instance.Formulation = value

value = instance.Formulation
```

### C#

```csharp
System.int Formulation {get; set;}
```

### C++/CLI

```cpp
property System.int Formulation {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Formulation type as defined in [swsShellFormulation_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShellFormulation_e.html)

## VBA Syntax

See [CWShell::Formulation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~Formulation.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
