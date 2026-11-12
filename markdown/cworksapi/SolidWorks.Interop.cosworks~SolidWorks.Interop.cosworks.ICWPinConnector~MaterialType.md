---
title: "MaterialType Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "MaterialType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialType.html"
---

# MaterialType Property (ICWPinConnector)

Gets or sets the type of material for this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

instance.MaterialType = value

value = instance.MaterialType
```

### C#

```csharp
System.int MaterialType {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = From material library
- 0 = Custom defined

## VBA Syntax

See [CWPinConnector::MaterialType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~MaterialType.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only if [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)
[ICWPinConnector::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html)
[ICWPinConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
