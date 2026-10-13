---
title: "Train Property (ISustainabilityTransportation)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityTransportation"
member: "Train"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation~Train.html"
---

# Train Property (ISustainabilityTransportation)

Gets or sets the distance traveled by train from the region of manufacture to the region of use.

## Syntax

### Visual Basic (Declaration)

```vb
Property Train As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityTransportation
Dim value As System.Double

instance.Train = value

value = instance.Train
```

### C#

```csharp
System.double Train {get; set;}
```

### C++/CLI

```cpp
property System.double Train {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Distance in kilometers or miles traveled by train <= 100,000,000.0

## VBA Syntax

See [SustainabilityTransportation::Train](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityTransportation~Train.html).

## Examples

See the examples in [ISustainabilityTransportation](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityTransportation.html).

## See Also

[ISustainabilityTransportation Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation.html)
[ISustainabilityTransportation Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityTransportation_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
