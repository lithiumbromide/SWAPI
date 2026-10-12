---
title: "YoungModulus Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "YoungModulus"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html"
---

# YoungModulus Property (ICWPinConnector)

Gets or sets Young's Modulus for the material of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property YoungModulus As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

Young's Modulus (see **Remarks**)

## VBA Syntax

See [CWPinConnector::YoungModulus](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~YoungModulus.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only if:

- [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true.
- Material is specified. Call [ICWPinConnector::SetLibraryMaterial](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html) to set the material of this pin connector.

  | If ICWPinConnector::MaterialType is... | Then use this property to... | Young's Modulus for the specified... |
  | --- | --- | --- |
  | 0 | Get and set | Custom material |
  | 1 | Only get | Library material |

See the **Material Properties in Simulation** topic in the Simulation Help for more information about Elastic Modulus.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::MassValue Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html)
[ICWPinConnector::MaterialUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)
[ICWPinConnector::PoissonsRatio Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::GetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
