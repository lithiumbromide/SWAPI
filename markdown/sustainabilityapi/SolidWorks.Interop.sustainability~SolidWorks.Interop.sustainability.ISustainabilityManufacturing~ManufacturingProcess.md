---
title: "ManufacturingProcess Property (ISustainabilityManufacturing)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityManufacturing"
member: "ManufacturingProcess"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing~ManufacturingProcess.html"
---

# ManufacturingProcess Property (ISustainabilityManufacturing)

Gets or sets the manufacturing process for the current part.

## Syntax

### Visual Basic (Declaration)

```vb
Property ManufacturingProcess As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityManufacturing
Dim value As System.String

instance.ManufacturingProcess = value

value = instance.ManufacturingProcess
```

### C#

```csharp
System.string ManufacturingProcess {get; set;}
```

### C++/CLI

```cpp
property System.String^ ManufacturingProcess {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Manufacturing process as defined in [swSustainabilityManufacturingProcessType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityManufacturingProcessType_e.html)

## VBA Syntax

See [SustainabilityManufacturing::ManufacturingProcess](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityManufacturing~ManufacturingProcess.html).

## Examples

See examples in [ISustainabilityManufacturing](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityManufacturing.html).

## Remarks

Availability of the manufacturing process types depends on the value of [ISustainabilityMaterial::MaterialClass](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityMaterial~MaterialClass.html). See the Sustainability Help for more information.

## See Also

[ISustainabilityManufacturing Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing.html)
[ISustainabilityManufacturing Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityManufacturing_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
