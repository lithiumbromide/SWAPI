---
title: "Paint Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "Paint"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~Paint.html"
---

# Paint Property (ISustainabilityManufacturing)

Gets or sets the paint type used to manufacture the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property Paint As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.Integer

instance.Paint = value

value = instance.Paint
```

### C#

```csharp
System.int Paint {get; set;}
```

### C++/CLI

```cpp
property System.int Paint {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Paint type as defined in [swSustainabilityManufacturingPaintType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityManufacturingPaintType_e.html)

## VBA Syntax

See [SustainabilityManufacturing::Paint](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~Paint.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
