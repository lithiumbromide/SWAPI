---
title: "Weight Property (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "Weight"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~Weight.html"
---

# Weight Property (ISustainabilityMaterial)

Gets the weight of the material.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Weight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim value As System.Double

value = instance.Weight
```

### C#

```csharp
System.double Weight {get;}
```

### C++/CLI

```cpp
property System.double Weight {
   System.double get();
}
```

### Property Value

Weight of the material

## VBA Syntax

See [SustainabilityMaterial::Weight](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~Weight.html).

## Examples

[Calculate Environmental Impact of Part (VBA)](Calculate_Environmental_Impact_of_Part_Example_VB.htm)

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
