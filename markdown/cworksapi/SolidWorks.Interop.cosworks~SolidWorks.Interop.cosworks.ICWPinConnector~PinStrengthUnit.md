---
title: "PinStrengthUnit Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "PinStrengthUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html"
---

# PinStrengthUnit Property (ICWPinConnector)

Gets or sets the units of yield strength of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property PinStrengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

instance.PinStrengthUnit = value

value = instance.PinStrengthUnit
```

### C#

```csharp
System.int PinStrengthUnit {get; set;}
```

### C++/CLI

```cpp
property System.int PinStrengthUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Strength units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)

## VBA Syntax

See [CWPinConnector::PinStrengthUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~PinStrengthUnit.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PinStrengthValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html)
[ICWPinConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html)
[ICWPinConnector::TensileStressAreaValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html)
[ICWPinConnector::SafetyFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
