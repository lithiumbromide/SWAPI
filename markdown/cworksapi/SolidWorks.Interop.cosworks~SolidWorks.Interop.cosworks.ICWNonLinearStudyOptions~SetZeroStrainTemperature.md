---
title: "SetZeroStrainTemperature Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetZeroStrainTemperature.html"
---

# SetZeroStrainTemperature Method (ICWNonLinearStudyOptions)

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
Dim instance As ICWNonLinearStudyOptions
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
- `NZeroStrainTemperatureUnit`: Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)

## VBA Syntax

See [CWNonLinearStudyOptions::SetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetZeroStrainTemperature.html)
[ICWNonLinearStudyOptions::UseLargeStrain Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~UseLargeStrain.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
