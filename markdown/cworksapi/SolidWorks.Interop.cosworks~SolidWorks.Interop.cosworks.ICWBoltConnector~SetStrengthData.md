---
title: "SetStrengthData Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "SetStrengthData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetStrengthData.html"
---

# SetStrengthData Method (ICWBoltConnector)

Sets the strength data for this bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetStrengthData( _
   ByVal DTensileStressArea As System.Double, _
   ByVal DPinBoltStrength As System.Double, _
   ByVal DSafetyFactor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DTensileStressArea As System.Double
Dim DPinBoltStrength As System.Double
Dim DSafetyFactor As System.Double

instance.SetStrengthData(DTensileStressArea, DPinBoltStrength, DSafetyFactor)
```

### C#

```csharp
void SetStrengthData(
   System.double DTensileStressArea,
   System.double DPinBoltStrength,
   System.double DSafetyFactor
)
```

### C++/CLI

```cpp
void SetStrengthData(
   System.double DTensileStressArea,
   System.double DPinBoltStrength,
   System.double DSafetyFactor
)
```

### Parameters

- `DTensileStressArea`: Tensile stress area
- `DPinBoltStrength`: Bolt strength
- `DSafetyFactor`: Safety factor

## VBA Syntax

See [CWBoltConnector::SetStrengthData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~SetStrengthData.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::IncludeStrengthData Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeStrengthData.html)
[ICWBoltConnector::GetStrengthData Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetStrengthData.html)
[ICWBoltConnector::TensileStressAreaUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~TensileStressAreaUnit.html)
[ICWBoltConnector::PinBoltStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PinBoltStrengthUnit.html)
[ICWBoltConnector::IncludeKnownTensileStressArea Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeKnownTensileStressArea.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::ThreadsPerLengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThreadsPerLengthUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
