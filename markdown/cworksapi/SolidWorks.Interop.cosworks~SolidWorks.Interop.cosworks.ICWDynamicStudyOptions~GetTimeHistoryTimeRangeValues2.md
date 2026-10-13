---
title: "GetTimeHistoryTimeRangeValues2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetTimeHistoryTimeRangeValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html"
---

# GetTimeHistoryTimeRangeValues2 Method (ICWDynamicStudyOptions)

Gets the time range of the modal time history dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeHistoryTimeRangeValues2( _
   ByRef DStartTime As System.Double, _
   ByRef DEndTime As System.Double, _
   ByRef DTimeIncrement As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DStartTime As System.Double
Dim DEndTime As System.Double
Dim DTimeIncrement As System.Double
Dim value As System.Integer

value = instance.GetTimeHistoryTimeRangeValues2(DStartTime, DEndTime, DTimeIncrement)
```

### C#

```csharp
System.int GetTimeHistoryTimeRangeValues2(
   out System.double DStartTime,
   out System.double DEndTime,
   out System.double DTimeIncrement
)
```

### C++/CLI

```cpp
System.int GetTimeHistoryTimeRangeValues2(
   [Out] System.double DStartTime,
   [Out] System.double DEndTime,
   [Out] System.double DTimeIncrement
)
```

### Parameters

- `DStartTime`: Start time
- `DEndTime`: End time
- `DTimeIncrement`: Time increment

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html).

## Examples

[Create Linear Dynamic Time History Study (VBA)](Create_Dynamic_Time_History_Study_Example_VB.htm)
[Create Linear Dynamic Time History Study (VB.NET)](Create_Dynamic_Time_History_Study_Example_VBNET.htm)
[Create Linear Dynamic Time History Study (C#)](Create_Dynamic_Time_History_Study_Example_CSharp.htm)

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html)
[ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
