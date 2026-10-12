---
title: "GetZeroStrainTemperature Method (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "GetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~GetZeroStrainTemperature.html"
---

# GetZeroStrainTemperature Method (ICWFrequencyStudyOptions)

Gets the temperature at zero strain and its units.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetZeroStrainTemperature( _
   ByRef DZeroStrainTemperature As System.Double, _
   ByRef NZeroStrainTemperatureUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim DZeroStrainTemperature As System.Double
Dim NZeroStrainTemperatureUnit As System.Integer

instance.GetZeroStrainTemperature(DZeroStrainTemperature, NZeroStrainTemperatureUnit)
```

### C#

```csharp
void GetZeroStrainTemperature(
   out System.double DZeroStrainTemperature,
   out System.int NZeroStrainTemperatureUnit
)
```

### C++/CLI

```cpp
void GetZeroStrainTemperature(
   [Out] System.double DZeroStrainTemperature,
   [Out] System.int NZeroStrainTemperatureUnit
)
```

### Parameters

- `DZeroStrainTemperature`: Reference temperature at zero strain
- `NZeroStrainTemperatureUnit`: Temperature units as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)

## VBA Syntax

See [CWFrequencyStudyOptions::GetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~GetZeroStrainTemperature.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)
[ICWFrequencyStudyOptions::SetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~SetZeroStrainTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
