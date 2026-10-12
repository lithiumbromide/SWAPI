---
title: "Plane Property (ISustainabilityTransportation)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityTransportation"
member: "Plane"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation~Plane.html"
---

# Plane Property (ISustainabilityTransportation)

Gets or sets the distance traveled by plane from the region of manufacture to the region of use.

## Syntax

### Visual Basic (Declaration)

```vb
Property Plane As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityTransportation
Dim value As System.Double

instance.Plane = value

value = instance.Plane
```

### C#

```csharp
System.double Plane {get; set;}
```

### C++/CLI

```cpp
property System.double Plane {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Distance in kilometers or miles traveled by plane <= 100,000,000.0

## VBA Syntax

See [SustainabilityTransportation::Plane](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityTransportation~Plane.html).

## Examples

See the examples in [ISustainabilityTransportation](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityTransportation.html).

## See Also

[ISustainabilityTransportation Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation.html)
[ISustainabilityTransportation Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
