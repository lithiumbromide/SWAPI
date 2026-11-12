---
title: "DurationType Property (ISustainabilityAssemblyUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyUse"
member: "DurationType"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~DurationType.html"
---

# DurationType Property (ISustainabilityAssemblyUse)

Gets or sets the per time units of energy usage.

## Syntax

### Visual Basic (Declaration)

```vb
Property DurationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyUse
Dim value As System.Integer

instance.DurationType = value

value = instance.DurationType
```

### C#

```csharp
System.int DurationType {get; set;}
```

### C++/CLI

```cpp
property System.int DurationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Per time units for [ISustainabilityAssemblyUse::AssemblyUseAmount](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse~AssemblyUseAmount.html) as defined in [swSustainabilityDurationType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityDurationType_e.html)

## VBA Syntax

See [SustainabilityAssemblyUse::DurationType](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyUse~DurationType.html).

## Examples

See the examples in [ISustainabilityAssemblyUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse.html).

## See Also

[ISustainabilityAssemblyUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse.html)
[ISustainabilityAssemblyUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
