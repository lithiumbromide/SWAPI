---
title: "GetZeroStrainTemperature Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetZeroStrainTemperature.html"
---

# GetZeroStrainTemperature Method (ICWNonLinearStudyOptions)

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
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::GetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::SetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetZeroStrainTemperature.html)
[ICWNonLinearStudyOptions::UseLargeStrain Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeStrain.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
