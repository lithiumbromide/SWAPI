---
title: "TensileStressAreaValue Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "TensileStressAreaValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html"
---

# TensileStressAreaValue Property (ICWPinConnector)

Gets or sets the tensile stress area for this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property TensileStressAreaValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.TensileStressAreaValue = value

value = instance.TensileStressAreaValue
```

### C#

```csharp
System.double TensileStressAreaValue {get; set;}
```

### C++/CLI

```cpp
property System.double TensileStressAreaValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Tensile stress area

## VBA Syntax

See [CWPinConnector::TensileStressAreaValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~TensileStressAreaValue.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html)
[ICWPinConnector::SafetyFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html)
[ICWPinConnector::PinStrengthValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html)
[ICWPinConnector::PinStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
