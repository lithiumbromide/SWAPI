---
title: "AssemblyProcessAmount Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "AssemblyProcessAmount"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~AssemblyProcessAmount.html"
---

# AssemblyProcessAmount Property (ISustainabilityAssemblyProcess)

Gets or sets the amount of fuel required to assemble this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyProcessAmount As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Object

instance.AssemblyProcessAmount = value

value = instance.AssemblyProcessAmount
```

### C#

```csharp
System.object AssemblyProcessAmount {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AssemblyProcessAmount {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array containing the amounts of electricity and natural gas required to assemble this assembly; valid only if [ISustainabilityAssemblyProcess::EnergyForAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess~EnergyForAssemblyProcess.html) is true

## VBA Syntax

See [SustainabilityAssemblyProcess::AssemblyProcessAmount](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~AssemblyProcessAmount.html).

## Examples

See the examples in [ISustainabilityAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
