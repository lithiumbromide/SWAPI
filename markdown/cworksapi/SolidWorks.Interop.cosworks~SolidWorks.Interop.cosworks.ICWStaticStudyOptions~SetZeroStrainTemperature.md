---
title: "SetZeroStrainTemperature Method (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "SetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SetZeroStrainTemperature.html"
---

# SetZeroStrainTemperature Method (ICWStaticStudyOptions)

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
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::SetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~SetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::GetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~GetZeroStrainTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
