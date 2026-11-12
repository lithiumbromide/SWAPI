---
title: "GetStrengthData Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "GetStrengthData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html"
---

# GetStrengthData Method (ICWBoltConnector)

Gets the strength data for this bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetStrengthData( _
   ByRef DTensileStressArea As System.Double, _
   ByRef DPinBoltStrength As System.Double, _
   ByRef DSafetyFactor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DTensileStressArea As System.Double
Dim DPinBoltStrength As System.Double
Dim DSafetyFactor As System.Double

instance.GetStrengthData(DTensileStressArea, DPinBoltStrength, DSafetyFactor)
```

### C#

```csharp
void GetStrengthData(
   out System.double DTensileStressArea,
   out System.double DPinBoltStrength,
   out System.double DSafetyFactor
)
```

### C++/CLI

```cpp
void GetStrengthData(
   [Out] System.double DTensileStressArea,
   [Out] System.double DPinBoltStrength,
   [Out] System.double DSafetyFactor
)
```

### Parameters

- `DTensileStressArea`: Tensile stress area
- `DPinBoltStrength`: Bolt strength
- `DSafetyFactor`: Safety factor

## VBA Syntax

See [CWBoltConnector::GetStrengthData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~GetStrengthData.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::SetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::IncludeKnownTensileStressArea Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html)
[ICWBoltConnector::PinBoltStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PinBoltStrengthUnit.html)
[ICWBoltConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::ThreadsPerLengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThreadsPerLengthUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
