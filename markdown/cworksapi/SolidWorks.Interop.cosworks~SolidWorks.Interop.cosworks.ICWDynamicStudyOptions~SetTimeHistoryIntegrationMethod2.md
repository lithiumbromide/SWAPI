---
title: "SetTimeHistoryIntegrationMethod2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetTimeHistoryIntegrationMethod2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html"
---

# SetTimeHistoryIntegrationMethod2 Method (ICWDynamicStudyOptions)

Sets the integration method of this modal time history dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeHistoryIntegrationMethod2( _
   ByVal NMethod As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim NMethod As System.Integer
Dim value As System.Integer

value = instance.SetTimeHistoryIntegrationMethod2(NMethod)
```

### C#

```csharp
System.int SetTimeHistoryIntegrationMethod2(
   System.int NMethod
)
```

### C++/CLI

```cpp
System.int SetTimeHistoryIntegrationMethod2(
   System.int NMethod
)
```

### Parameters

- `NMethod`: Integration method as defined in [swsTimeIntegrationMethod_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeIntegrationMethod_e.html)

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
