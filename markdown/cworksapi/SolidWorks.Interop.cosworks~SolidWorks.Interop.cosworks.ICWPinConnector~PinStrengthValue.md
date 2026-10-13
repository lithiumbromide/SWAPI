---
title: "PinStrengthValue Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "PinStrengthValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html"
---

# PinStrengthValue Property (ICWPinConnector)

Gets or sets the yield strength of this pin connector

## Syntax

### Visual Basic (Declaration)

```vb
Property PinStrengthValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.PinStrengthValue = value

value = instance.PinStrengthValue
```

### C#

```csharp
System.double PinStrengthValue {get; set;}
```

### C++/CLI

```cpp
property System.double PinStrengthValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Yield strength of this pin connector

## VBA Syntax

See [CWPinConnector::PinStrengthValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~PinStrengthValue.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PinStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html)
[ICWPinConnector::SafetyFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html)
[ICWPinConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html)
[ICWPinConnector::TensileStressAreaValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
