---
title: "Region Property (ISustainabilityUse)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityUse"
member: "Region"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityUse~Region.html"
---

# Region Property (ISustainabilityUse)

Gets or sets the geographical region where the part is transported and used.

## Syntax

### Visual Basic (Declaration)

```vb
Property Region As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityUse
Dim value As System.Integer

instance.Region = value

value = instance.Region
```

### C#

```csharp
System.int Region {get; set;}
```

### C++/CLI

```cpp
property System.int Region {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Geographical region where the part is transported and used as defined in [swSustainabilityRegionName_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityRegionName_e.html)

## VBA Syntax

See [SustainabilityUse::Region](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityPartUse~Region.html).

## Examples

See examples in [ISustainabilityUse](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityUse.html).

## See Also

[ISustainabilityUse Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityUse.html)
[ISustainabilityUse Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityUse_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
