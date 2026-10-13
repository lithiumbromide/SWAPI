---
title: "EnergyForAssemblyProcess Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "EnergyForAssemblyProcess"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~EnergyForAssemblyProcess.html"
---

# EnergyForAssemblyProcess Property (ISustainabilityAssemblyProcess)

Gets or sets whether energy is required to create this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnergyForAssemblyProcess As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Boolean

instance.EnergyForAssemblyProcess = value

value = instance.EnergyForAssemblyProcess
```

### C#

```csharp
System.bool EnergyForAssemblyProcess {get; set;}
```

### C++/CLI

```cpp
property System.bool EnergyForAssemblyProcess {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if energy is required to create this assembly, false if not

## VBA Syntax

See [SustainabilityAssemblyProcess::EnergyForAssemblyProcess](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~EnergyForAssemblyProcess.html).

## Examples

See the examples in [ISustainabilityAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
