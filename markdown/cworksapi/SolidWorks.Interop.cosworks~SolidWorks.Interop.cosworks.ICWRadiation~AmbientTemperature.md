---
title: "AmbientTemperature Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "AmbientTemperature"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~AmbientTemperature.html"
---

# AmbientTemperature Property (ICWRadiation)

Gets or sets the value of ambient temperature for this radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Property AmbientTemperature As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Double

instance.AmbientTemperature = value

value = instance.AmbientTemperature
```

### C#

```csharp
System.double AmbientTemperature {get; set;}
```

### C++/CLI

```cpp
property System.double AmbientTemperature {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Ambient temperature

## VBA Syntax

See [CWRadiation::AmbientTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~AmbientTemperature.html).

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiation::OpenSystem Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~OpenSystem.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
