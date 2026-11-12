---
title: "SetTimeHistoryDeadLoadOptions2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetTimeHistoryDeadLoadOptions2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html"
---

# SetTimeHistoryDeadLoadOptions2 Method (ICWDynamicStudyOptions)

Sets the dead load effects of the modal time history dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTimeHistoryDeadLoadOptions2( _
   ByVal BChecked As System.Boolean, _
   ByVal SStudyName As System.String, _
   ByVal DMultiplicationFactor As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Boolean
Dim SStudyName As System.String
Dim DMultiplicationFactor As System.Double
Dim value As System.Integer

value = instance.SetTimeHistoryDeadLoadOptions2(BChecked, SStudyName, DMultiplicationFactor)
```

### C#

```csharp
System.int SetTimeHistoryDeadLoadOptions2(
   System.bool BChecked,
   System.string SStudyName,
   System.double DMultiplicationFactor
)
```

### C++/CLI

```cpp
System.int SetTimeHistoryDeadLoadOptions2(
   System.bool BChecked,
   System.String^ SStudyName,
   System.double DMultiplicationFactor
)
```

### Parameters

- `BChecked`: True to set dead loads for a static study, false to not
- `SStudyName`: Name of the study
- `DMultiplicationFactor`: Multiplication factor

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)
[ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html)
[ICWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
