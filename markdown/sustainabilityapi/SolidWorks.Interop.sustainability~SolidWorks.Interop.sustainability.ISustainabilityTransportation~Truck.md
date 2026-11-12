---
title: "Truck Property (ISustainabilityTransportation)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityTransportation"
member: "Truck"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation~Truck.html"
---

# Truck Property (ISustainabilityTransportation)

Gets or sets the distance traveled by truck from the region of manufacture to the region of use.

## Syntax

### Visual Basic (Declaration)

```vb
Property Truck As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityTransportation
Dim value As System.Double

instance.Truck = value

value = instance.Truck
```

### C#

```csharp
System.double Truck {get; set;}
```

### C++/CLI

```cpp
property System.double Truck {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Distance in kilometers or miles traveled by truck <= 100,000,000.0

## VBA Syntax

See [SustainabilityTransportation::Truck](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityTransportation~Truck.html).

## Examples

See the examples in [ISustainabilityTransportation](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityTransportation.html).

## See Also

[ISustainabilityTransportation Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation.html)
[ISustainabilityTransportation Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
