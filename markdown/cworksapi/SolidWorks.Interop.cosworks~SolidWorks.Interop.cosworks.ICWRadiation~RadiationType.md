---
title: "RadiationType Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "RadiationType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~RadiationType.html"
---

# RadiationType Property (ICWRadiation)

Gets or sets the type of radiation.

## Syntax

### Visual Basic (Declaration)

```vb
Property RadiationType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Integer

instance.RadiationType = value

value = instance.RadiationType
```

### C#

```csharp
System.int RadiationType {get; set;}
```

### C++/CLI

```cpp
property System.int RadiationType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Radiation type as defined in [swsRadiationType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRadiationType_e.html)

## VBA Syntax

See [CWRadiation::RadiationType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~RadiationType.html).

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
