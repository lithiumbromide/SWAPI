---
title: "GetSensorDetailsForGraphsAndPlots Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "GetSensorDetailsForGraphsAndPlots"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~GetSensorDetailsForGraphsAndPlots.html"
---

# GetSensorDetailsForGraphsAndPlots Method (ICWStudyResultOptions)

Gets how plot data for response graphs is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetSensorDetailsForGraphsAndPlots( _
   ByRef NSensorOption As System.Integer, _
   ByRef SSensorName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim NSensorOption As System.Integer
Dim SSensorName As System.String

instance.GetSensorDetailsForGraphsAndPlots(NSensorOption, SSensorName)
```

### C#

```csharp
void GetSensorDetailsForGraphsAndPlots(
   out System.int NSensorOption,
   out System.string SSensorName
)
```

### C++/CLI

```cpp
void GetSensorDetailsForGraphsAndPlots(
   [Out] System.int NSensorOption,
   [Out] System.String^ SSensorName
)
```

### Parameters

- `NSensorOption`: Sensor option as defined in [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html)
- `SSensorName`: Sensor name; valid only if NSensorOption = swsResultOptionsSensorOption_e.swsResultOptionsSensorOption_SpecificSensor

## VBA Syntax

See [CWStudyResultOptions::GetSensorDetailsForGraphsAndPlots](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~GetSensorDetailsForGraphsAndPlots.html).

## Remarks

This method is valid only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = swsSaveResultsOption_e.swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
