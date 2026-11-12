---
title: "GetTimeHistorySecondIntegrationParameter2 Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetTimeHistorySecondIntegrationParameter2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html"
---

# GetTimeHistorySecondIntegrationParameter2 Method (ICWDynamicStudyOptions)

Gets the second integration parameter of the modal time history dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTimeHistorySecondIntegrationParameter2( _
   ByRef DSecondIntegration As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DSecondIntegration As System.Double
Dim value As System.Integer

value = instance.GetTimeHistorySecondIntegrationParameter2(DSecondIntegration)
```

### C#

```csharp
System.int GetTimeHistorySecondIntegrationParameter2(
   out System.double DSecondIntegration
)
```

### C++/CLI

```cpp
System.int GetTimeHistorySecondIntegrationParameter2(
   [Out] System.double DSecondIntegration
)
```

### Parameters

- `DSecondIntegration`: Second integration parameter

### Return Value

0 indicates success; a non-0 value indicates failure

## VBA Syntax

See [CWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html).

## Examples

[Create Linear Dynamic Time History Study (VBA)](Create_Dynamic_Time_History_Study_Example_VB.htm)
[Create Linear Dynamic Time History Study (VB.NET)](Create_Dynamic_Time_History_Study_Example_VBNET.htm)
[Create Linear Dynamic Time History Study (C#)](Create_Dynamic_Time_History_Study_Example_CSharp.htm)

## Remarks

This method is valid only if the time history integration method is Newmark. See [ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html) and [ICWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html)
[ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html)
[ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)
[ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html)
[ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2 Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)

## Availability

SOLIDWORKS Simulation API 2015 SP0
