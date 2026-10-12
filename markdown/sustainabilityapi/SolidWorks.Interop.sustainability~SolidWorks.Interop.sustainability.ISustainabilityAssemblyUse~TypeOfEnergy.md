---
title: "TypeOfEnergy Property (ISustainabilityAssemblyUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyUse"
member: "TypeOfEnergy"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~TypeOfEnergy.html"
---

# TypeOfEnergy Property (ISustainabilityAssemblyUse)

Gets or sets the type of energy used over the life span of the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property TypeOfEnergy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyUse
Dim value As System.Integer

instance.TypeOfEnergy = value

value = instance.TypeOfEnergy
```

### C#

```csharp
System.int TypeOfEnergy {get; set;}
```

### C++/CLI

```cpp
property System.int TypeOfEnergy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of energy as defined in [swSustainabilityEnergyType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityEnergyType_e.html); valid only if [ISustainabilityAssemblyUse::EnergyOverLifeSpan](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse~EnergyOverLifeSpan.html) is true

## VBA Syntax

See [SustainabilityAssemblyUse::TypeOfEnergy](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyUse~TypeOfEnergy.html).

## See Also

[ISustainabilityAssemblyUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse.html)
[ISustainabilityAssemblyUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
