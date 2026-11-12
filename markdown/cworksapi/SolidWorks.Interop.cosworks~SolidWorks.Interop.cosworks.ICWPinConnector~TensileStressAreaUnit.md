---
title: "TensileStressAreaUnit Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "TensileStressAreaUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html"
---

# TensileStressAreaUnit Property (ICWPinConnector)

Gets or sets the units of tensile stress area for this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property TensileStressAreaUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Integer

instance.TensileStressAreaUnit = value

value = instance.TensileStressAreaUnit
```

### C#

```csharp
System.int TensileStressAreaUnit {get; set;}
```

### C++/CLI

```cpp
property System.int TensileStressAreaUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Tensile stress area unit as defined in [swsTensileStressAreaUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTensileStressAreaUnit_e.html)

## VBA Syntax

See [CWPinConnector::TensileStressAreaUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~TensileStressAreaUnit.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::TensileStressAreaValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html)
[ICWPinConnector::PinStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html)
[ICWPinConnector::PinStrengthValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html)
[ICWPinConnector::SafetyFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
