---
title: "SetZeroStrainTemperature Method (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "SetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~SetZeroStrainTemperature.html"
---

# SetZeroStrainTemperature Method (ICWBucklingStudyOptions)

Sets the reference temperature and its units at zero strain.

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
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::SetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~SetZeroStrainTemperature.html).

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
