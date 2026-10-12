---
title: "SetZeroStrainTemperature Method (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "SetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~SetZeroStrainTemperature.html"
---

# SetZeroStrainTemperature Method (ICWFrequencyStudyOptions)

Sets the temperature at zero strain and its units.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetZeroStrainTemperature( _
   ByVal DZeroStrainTemperature As System.Double, _
   ByVal NZeroStrainTemperatureUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim DZeroStrainTemperature As System.Double
Dim NZeroStrainTemperatureUnit As System.Integer

instance.SetZeroStrainTemperature(DZeroStrainTemperature, NZeroStrainTemperatureUnit)
```

### C#

```csharp
void SetZeroStrainTemperature(
   System.double DZeroStrainTemperature,
   System.int NZeroStrainTemperatureUnit
)
```

### C++/CLI

```cpp
void SetZeroStrainTemperature(
   System.double DZeroStrainTemperature,
   System.int NZeroStrainTemperatureUnit
)
```

### Parameters

- `DZeroStrainTemperature`: Reference temperature at zero strain
- `NZeroStrainTemperatureUnit`: Temperature units as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::SetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~SetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::GetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~GetZeroStrainTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
