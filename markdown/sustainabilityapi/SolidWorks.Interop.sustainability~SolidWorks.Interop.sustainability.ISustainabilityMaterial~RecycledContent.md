---
title: "RecycledContent Property (ISustainabilityMaterial)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityMaterial"
member: "RecycledContent"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial~RecycledContent.html"
---

# RecycledContent Property (ISustainabilityMaterial)

Gets or sets the percentage of material that can be recycled.

## Syntax

### Visual Basic (Declaration)

```vb
Property RecycledContent As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityMaterial
Dim value As System.Double

instance.RecycledContent = value

value = instance.RecycledContent
```

### C#

```csharp
System.double RecycledContent {get; set;}
```

### C++/CLI

```cpp
property System.double RecycledContent {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Percentage of material that can be recycled (see **Remarks**)

## VBA Syntax

See [SustainabilityMaterial::RecycledContent](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityMaterial~RecycledContent.html).

## Examples

[Calculate Environmental Impact of Part (VBA)](Calculate_Environmental_Impact_of_Part_Example_VB.htm)

## Remarks

This property is read-only for assembly components. For parts, you can set the recycled content of the following materials:

| ISustainabilityMaterial::MaterialClass | ISustainabilityMaterial::MaterialName |
| --- | --- |
| Aluminum Alloys | 356.0-T6 Permanent Mold cast |
| Aluminum Alloys | AA356.0-F |

## See Also

[ISustainabilityMaterial Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial.html)
[ISustainabilityMaterial Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityMaterial_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
