---
title: "PerformAdvanceValidations Method (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "PerformAdvanceValidations"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~PerformAdvanceValidations.html"
---

# PerformAdvanceValidations Method (ICWBearingConnector)

Calculates (shaft length)/(shaft diameter) and (shaft length)/(bearing length).

## Syntax

### Visual Basic (Declaration)

```vb
Function PerformAdvanceValidations() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector
Dim value As System.Integer

value = instance.PerformAdvanceValidations()
```

### C#

```csharp
System.int PerformAdvanceValidations()
```

### C++/CLI

```cpp
System.int PerformAdvanceValidations();
```

### Return Value

Error code as defined by [swsBearingConnectorErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectorErrors_e.html)

## VBA Syntax

See [CWBearingConnector::PerformAdvanceValidations](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~PerformAdvanceValidations.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)
[ICWBearingConnector::AllowLenByDiamRatioGreaterThan2ForShaft Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowLenByDiamRatioGreaterThan2ForShaft.html)
[ICWBearingConnector::AllowShaftByBearingRatioGreaterThan2 Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~AllowShaftByBearingRatioGreaterThan2.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
