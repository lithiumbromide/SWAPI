---
title: "MaterialUnit Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "MaterialUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html"
---

# MaterialUnit Property (ICWPinConnector)

Gets or sets the unit system for the material properties of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

instance.MaterialUnit = value

value = instance.MaterialUnit
```

### C#

```csharp
System.int MaterialUnit {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Unit system as defined in [swsUnitSystem_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWPinConnector::MaterialUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~MaterialUnit.html).

## Remarks

This property is valid only if [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true, and material is specified. Call [ICWPinConnector::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html) to set the material of this pin connector.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PoissonsRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)
[ICWPinConnector::MassValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html)
[ICWPinConnector::GetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
