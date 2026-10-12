---
title: "AssemblyRegion Property (ISustainabilityAssemblyUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyUse"
member: "AssemblyRegion"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse~AssemblyRegion.html"
---

# AssemblyRegion Property (ISustainabilityAssemblyUse)

Gets or sets the geographical region where the assembly is used.

## Syntax

### Visual Basic (Declaration)

```vb
Property AssemblyRegion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyUse
Dim value As System.Integer

instance.AssemblyRegion = value

value = instance.AssemblyRegion
```

### C#

```csharp
System.int AssemblyRegion {get; set;}
```

### C++/CLI

```cpp
property System.int AssemblyRegion {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Geographical region where the assembly is used as defined in [swSustainabilityRegionName_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityRegionName_e.html)

## VBA Syntax

See [SustainabilityAssemblyUse::AssemblyRegion](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyUse~AssemblyRegion.html).

## Examples

See the examples in [ISustainabilityAssemblyUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyUse.html).

## See Also

[ISustainabilityAssemblyUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse.html)
[ISustainabilityAssemblyUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyUse_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
