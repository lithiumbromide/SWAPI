---
title: "MassValue Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "MassValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html"
---

# MassValue Property (ICWPinConnector)

Gets or sets the mass for the pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property MassValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.MassValue = value

value = instance.MassValue
```

### C#

```csharp
System.double MassValue {get; set;}
```

### C++/CLI

```cpp
property System.double MassValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Mass of this pin connector

## VBA Syntax

See [CWPinConnector::MassValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~MassValue.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only if:

- [ICWPinConnector::IncludeMass](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeMass.html) is set to true

- or -

- [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true, and material is specified. To set the material of this pin connector, call [ICWPinConnector::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::Unit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~Unit.html)
[ICWPinConnector::MaterialUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)
[ICWPinConnector::PoissonsRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)
[ICWPinConnector::GetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
