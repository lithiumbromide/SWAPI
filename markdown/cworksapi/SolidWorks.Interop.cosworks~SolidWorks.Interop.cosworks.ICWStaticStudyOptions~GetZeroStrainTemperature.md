---
title: "GetZeroStrainTemperature Method (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "GetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~GetZeroStrainTemperature.html"
---

# GetZeroStrainTemperature Method (ICWStaticStudyOptions)

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
Dim instance As ICWStaticStudyOptions
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
- `NZeroStrainTemperatureUnit`: Temperature unit as defined [swsTemperatureUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTemperatureUnit_e.html)

## VBA Syntax

See [CWStaticStudyOptions::GetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~GetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::SetZeroStrainTemperature Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~SetZeroStrainTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
