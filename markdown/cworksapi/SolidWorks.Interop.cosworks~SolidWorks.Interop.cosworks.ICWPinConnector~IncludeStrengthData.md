---
title: "IncludeStrengthData Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "IncludeStrengthData"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html"
---

# IncludeStrengthData Property (ICWPinConnector)

Gets or sets whether to include strength data in the analysis of this pin connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeStrengthData As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
Dim value As System.Boolean

instance.IncludeStrengthData = value

value = instance.IncludeStrengthData
```

### C#

```csharp
System.bool IncludeStrengthData {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeStrengthData {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include strength data, false to not

## VBA Syntax

See [CWPinConnector::IncludeStrengthData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~IncludeStrengthData.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This property is valid only for static and nonlinear studies.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::PinStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthUnit.html)
[ICWPinConnector::PinStrengthValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PinStrengthValue.html)
[ICWPinConnector::SafetyFactor Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SafetyFactor.html)
[ICWPinConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaUnit.html)
[ICWPinConnector::TensileStressAreaValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~TensileStressAreaValue.html)
[ICWPinConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)
[ICWPinConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 API
