---
title: "AssemblyUseAmount Property (ISustainabilityAssemblyUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyUse"
member: "AssemblyUseAmount"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~AssemblyUseAmount.html"
---

# AssemblyUseAmount Property (ISustainabilityAssemblyUse)

Gets or sets the amount of energy used over the life span of this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyUseAmount As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyUse
Dim value As System.Object

instance.AssemblyUseAmount = value

value = instance.AssemblyUseAmount
```

### C#

```csharp
System.object AssemblyUseAmount {get; set;}
```

### C++/CLI

```cpp
property System.Object^ AssemblyUseAmount {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array containing the amounts of electricity, natural gas, diesel, gasoline, and light fuel oil used over the life span of the assembly; valid only if [ISustainabilityAssemblyUse::EnergyOverLifeSpan](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse~EnergyOverLifeSpan.html) is true

## VBA Syntax

See [SustainabilityAssemblyUse::AssemblyUseAmount](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyUse~AssemblyUseAmount.html).

## Examples

See the examples in [ISustainabilityAssemblyUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse.html).

## See Also

[ISustainabilityAssemblyUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse.html)
[ISustainabilityAssemblyUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
