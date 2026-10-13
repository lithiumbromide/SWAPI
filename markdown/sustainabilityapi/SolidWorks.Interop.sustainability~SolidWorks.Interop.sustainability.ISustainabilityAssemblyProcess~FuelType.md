---
title: "FuelType Property (ISustainabilityAssemblyProcess)"
project: "SOLIDWORKS Sustainability API Help"
interface: "ISustainabilityAssemblyProcess"
member: "FuelType"
kind: "property"
source: "sustainabilityapi/SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess~FuelType.html"
---

# FuelType Property (ISustainabilityAssemblyProcess)

Type of fuel required by this assembly process.

## Syntax

### Visual Basic (Declaration)

```vb
Property FuelType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISustainabilityAssemblyProcess
Dim value As System.Integer

instance.FuelType = value

value = instance.FuelType
```

### C#

```csharp
System.int FuelType {get; set;}
```

### C++/CLI

```cpp
property System.int FuelType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of fuel as defined in [swSustainabilityFuelType_e](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.swSustainabilityFuelType_e.html); valid only if [ISustainabilityAssemblyProcess::EnergyForAssemblyProcess](SOLIDWORKS.Interop.sustainability~SOLIDWORKS.Interop.sustainability.ISustainabilityAssemblyProcess~EnergyForAssemblyProcess.html) is true

## VBA Syntax

See [SustainabilityAssemblyProcess::FuelType](ms-its:sustainabilityapivb6.chm::/sustainabilityLib~SustainabilityAssemblyProcess~FuelType.html).

## See Also

[ISustainabilityAssemblyProcess Interface](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess.html)
[ISustainabilityAssemblyProcess Members](SolidWorks.Interop.sustainability~SolidWorks.Interop.sustainability.ISustainabilityAssemblyProcess_members.html)

## Availability

SOLIDWORKS Sustainability API 2013 SP0
