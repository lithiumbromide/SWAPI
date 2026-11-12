---
title: "SetTimeHistoryTimeRangeValues2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetTimeHistoryTimeRangeValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html"
---

# SetTimeHistoryTimeRangeValues2 Method (ICWDynamicStudyOptions)

Sets the time range of the modal time history dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeHistoryTimeRangeValues2( _
   ByVal DStartTime As System.Double, _
   ByVal DEndTime As System.Double, _
   ByVal DTimeIncrement As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DStartTime As System.Double
Dim DEndTime As System.Double
Dim DTimeIncrement As System.Double
Dim value As System.Integer

value = instance.SetTimeHistoryTimeRangeValues2(DStartTime, DEndTime, DTimeIncrement)
```

### C#

```csharp
System.int SetTimeHistoryTimeRangeValues2(
   System.double DStartTime,
   System.double DEndTime,
   System.double DTimeIncrement
)
```

### C++/CLI

```cpp
System.int SetTimeHistoryTimeRangeValues2(
   System.double DStartTime,
   System.double DEndTime,
   System.double DTimeIncrement
)
```

### Parameters

- `DStartTime`: Start time
- `DEndTime`: End time
- `DTimeIncrement`: Time increment

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
