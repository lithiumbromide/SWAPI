---
title: "SetRandomVibrationPartialCorrelationDetails Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetRandomVibrationPartialCorrelationDetails"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails.html"
---

# SetRandomVibrationPartialCorrelationDetails Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetRandomVibrationPartialCorrelationDetails2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetRandomVibrationPartialCorrelationDetails( _
   ByVal NUnits As System.Integer, _
   ByVal DInRadius As System.Double, _
   ByVal DOutRadius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NUnits As System.Integer
Dim DInRadius As System.Double
Dim DOutRadius As System.Double

instance.SetRandomVibrationPartialCorrelationDetails(NUnits, DInRadius, DOutRadius)
```

### C#

```csharp
void SetRandomVibrationPartialCorrelationDetails(
   System.int NUnits,
   System.double DInRadius,
   System.double DOutRadius
)
```

### C++/CLI

```cpp
void SetRandomVibrationPartialCorrelationDetails(
   System.int NUnits,
   System.double DInRadius,
   System.double DOutRadius
)
```

### Parameters

- `NUnits`: Units as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DInRadius`: Inside radius
- `DOutRadius`: Outside radius

## VBA Syntax

See [CWDynamicStudyOptions::SetRandomVibrationPartialCorrelationDetails](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetRandomVibrationPartialCorrelationDetails.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
