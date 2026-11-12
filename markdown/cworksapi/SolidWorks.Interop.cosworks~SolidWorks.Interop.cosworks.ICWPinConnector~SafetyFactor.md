---
title: "SafetyFactor Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "SafetyFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html"
---

# SafetyFactor Property (ICWPinConnector)

Gets or sets the safety factor for the design check of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property SafetyFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Double

instance.SafetyFactor = value

value = instance.SafetyFactor
```

### C#

```csharp
System.double SafetyFactor {get; set;}
```

### C++/CLI

```cpp
property System.double SafetyFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Safety factor

## VBA Syntax

See [CWPinConnector::SafetyFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~SafetyFactor.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PinStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html)
[ICWPinConnector::PinStrengthValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html)
[ICWPinConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html)
[ICWPinConnector::TensileStressAreaValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html)
[ICWPinConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
