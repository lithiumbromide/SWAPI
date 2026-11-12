---
title: "YoungModulus Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "YoungModulus"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~YoungModulus.html"
---

# YoungModulus Property (ICWBoltConnector)

Gets or sets the Young modulus for the custom material.

## Syntax

### Visual Basic (Declaration)

```vb
Property YoungModulus As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.YoungModulus = value

value = instance.YoungModulus
```

### C#

```csharp
System.double YoungModulus {get; set;}
```

### C++/CLI

```cpp
property System.double YoungModulus {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Young modulus

## VBA Syntax

See [CWBoltConnector::YoungModulus](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~YoungModulus.html).

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
