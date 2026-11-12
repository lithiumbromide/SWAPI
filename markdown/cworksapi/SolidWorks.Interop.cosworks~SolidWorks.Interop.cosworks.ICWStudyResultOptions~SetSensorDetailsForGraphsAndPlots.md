---
title: "SetSensorDetailsForGraphsAndPlots Method (ICWStudyResultOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudyResultOptions"
member: "SetSensorDetailsForGraphsAndPlots"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions~SetSensorDetailsForGraphsAndPlots.html"
---

# SetSensorDetailsForGraphsAndPlots Method (ICWStudyResultOptions)

Sets how plot data for response graphs is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetSensorDetailsForGraphsAndPlots( _
   ByVal NSensorOption As System.Integer, _
   ByVal SSensorName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudyResultOptions
Dim NSensorOption As System.Integer
Dim SSensorName As System.String

instance.SetSensorDetailsForGraphsAndPlots(NSensorOption, SSensorName)
```

### C#

```csharp
void SetSensorDetailsForGraphsAndPlots(
   System.int NSensorOption,
   System.string SSensorName
)
```

### C++/CLI

```cpp
void SetSensorDetailsForGraphsAndPlots(
   System.int NSensorOption,
   System.String^ SSensorName
)
```

### Parameters

- `NSensorOption`: Sensor option as defined in [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html)
- `SSensorName`: Sensor name; valid only if NSensorOption = [swsResultOptionsSensorOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsResultOptionsSensorOption_e.html).swsResultOptionsSensorOption_SpecificSensor

## VBA Syntax

See [CWStudyResultOptions::SetSensorDetailsForGraphsAndPlots](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudyResultOptions~SetSensorDetailsForGraphsAndPlots.html).

## Remarks

This method is valid only if [ICWStudyResultOptions::SaveResultsForSolutionStepsOption](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions~SaveResultsForSolutionStepsOption.html) = swsSaveResultsOption_e.swsSaveResultsOption_ForSpecifiedSolutionSteps.

## See Also

[ICWStudyResultOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions.html)
[ICWStudyResultOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudyResultOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
