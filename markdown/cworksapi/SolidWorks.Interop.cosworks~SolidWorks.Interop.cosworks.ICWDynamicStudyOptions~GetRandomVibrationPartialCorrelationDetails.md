---
title: "GetRandomVibrationPartialCorrelationDetails Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetRandomVibrationPartialCorrelationDetails"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails.html"
---

# GetRandomVibrationPartialCorrelationDetails Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetRandomVibrationPartialCorrelationDetails2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetRandomVibrationPartialCorrelationDetails( _
   ByRef NUnits As System.Integer, _
   ByRef DInRadius As System.Double, _
   ByRef DOutRadius As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NUnits As System.Integer
Dim DInRadius As System.Double
Dim DOutRadius As System.Double

instance.GetRandomVibrationPartialCorrelationDetails(NUnits, DInRadius, DOutRadius)
```

### C#

```csharp
void GetRandomVibrationPartialCorrelationDetails(
   out System.int NUnits,
   out System.double DInRadius,
   out System.double DOutRadius
)
```

### C++/CLI

```cpp
void GetRandomVibrationPartialCorrelationDetails(
   [Out] System.int NUnits,
   [Out] System.double DInRadius,
   [Out] System.double DOutRadius
)
```

### Parameters

- `NUnits`: Units as defined [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)
- `DInRadius`: Inside radius
- `DOutRadius`: Outside radius

## VBA Syntax

See [CWDynamicStudyOptions::GetRandomVibrationPartialCorrelationDetails](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetRandomVibrationPartialCorrelationDetails.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
