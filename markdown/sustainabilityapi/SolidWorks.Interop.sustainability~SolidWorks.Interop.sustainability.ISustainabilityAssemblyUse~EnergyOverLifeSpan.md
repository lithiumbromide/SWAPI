---
title: "EnergyOverLifeSpan Property (ISustainabilityAssemblyUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyUse"
member: "EnergyOverLifeSpan"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~EnergyOverLifeSpan.html"
---

# EnergyOverLifeSpan Property (ISustainabilityAssemblyUse)

Gets or sets whether energy is required over the life span of the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnergyOverLifeSpan As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyUse
Dim value As System.Boolean

instance.EnergyOverLifeSpan = value

value = instance.EnergyOverLifeSpan
```

### C#

```csharp
System.bool EnergyOverLifeSpan {get; set;}
```

### C++/CLI

```cpp
property System.bool EnergyOverLifeSpan {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if energy is required over the life span of the assembly, false if not

## VBA Syntax

See [SustainabilityAssemblyUse::EnergyOverLifeSpan](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyUse~EnergyOverLifeSpan.html).

## Examples

See the examples in [ISustainabilityAssemblyUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse.html).

## See Also

[ISustainabilityAssemblyUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse.html)
[ISustainabilityAssemblyUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse_members.html)
[ISustainabilityAssemblyUse::AssemblyUseAmount Property](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~AssemblyUseAmount.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
