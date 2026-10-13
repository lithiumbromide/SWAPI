---
title: "GetZeroStrainTemperature Method (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "GetZeroStrainTemperature"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~GetZeroStrainTemperature.html"
---

# GetZeroStrainTemperature Method (ICWBucklingStudyOptions)

Gets the reference temperature and its units at zero strain.

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
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::GetZeroStrainTemperature](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~GetZeroStrainTemperature.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

The default temperature at zero strain is 298 Kelvin.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
