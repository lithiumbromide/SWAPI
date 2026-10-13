---
title: "ThermalCoefficient Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "ThermalCoefficient"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html"
---

# ThermalCoefficient Property (ICWPinConnector)

Gets or sets the coefficient of thermal expansion for the material of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThermalCoefficient As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

Coefficient of thermal expansion (see **Remarks**)

## VBA Syntax

See [CWPinConnector::ThermalCoefficient](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~ThermalCoefficient.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only if:

- [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true.
- Material is specified. Call [ICWPinConnector::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html) to set the material of this pin connector.

  | If ICWPinConnector::MaterialType is... | Then use this property to... | The coefficient of thermal expansion for the specified... |
  | --- | --- | --- |
  | 0 | Get and set | Custom material |
  | 1 | Only get | Library material |

See the **Material Properties in Simulation** topic in the Simulation Help for more information about the coefficient of thermal expansion.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PoissonsRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::YoungModulus Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)
[ICWPinConnector::MassValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html)
[ICWPinConnector::MaterialUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)
[ICWPinConnector::GetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
