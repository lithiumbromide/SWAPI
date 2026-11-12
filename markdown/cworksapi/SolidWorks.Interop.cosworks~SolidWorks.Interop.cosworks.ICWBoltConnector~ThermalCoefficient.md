---
title: "ThermalCoefficient Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "ThermalCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThermalCoefficient.html"
---

# ThermalCoefficient Property (ICWBoltConnector)

Gets or sets the thermal expansion coefficient for the custom material.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.ThermalCoefficient = value

value = instance.ThermalCoefficient
```

### C#

```csharp
System.double ThermalCoefficient {get; set;}
```

### C++/CLI

```cpp
property System.double ThermalCoefficient {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thermal expansion coefficient

## VBA Syntax

See [CWBoltConnector::ThermalCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~ThermalCoefficient.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetLibraryMaterial.html)
[ICWBoltConnector::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetLibraryMaterial.html)
[ICWBoltConnector::IncludeMass Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeMass.html)
[ICWBoltConnector::MassValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MassValue.html)
[ICWBoltConnector::MaterialSource Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialSource.html)
[ICWBoltConnector::MaterialType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialType.html)
[ICWBoltConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialUnit.html)
[ICWBoltConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PoissonsRatio.html)
[ICWBoltConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThermalCoefficient.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
