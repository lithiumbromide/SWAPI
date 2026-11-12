---
title: "TimeHistorySecondIntegrationParameter Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "TimeHistorySecondIntegrationParameter"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistorySecondIntegrationParameter.html"
---

# TimeHistorySecondIntegrationParameter Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistorySecondIntegrationParameter2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistorySecondIntegrationParameter2.html) and [ICWDynamicStudyOptions::SetTimeHistorySecondIntegrationParameter2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistorySecondIntegrationParameter2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeHistorySecondIntegrationParameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.TimeHistorySecondIntegrationParameter = value

value = instance.TimeHistorySecondIntegrationParameter
```

### C#

```csharp
System.double TimeHistorySecondIntegrationParameter {get; set;}
```

### C++/CLI

```cpp
property System.double TimeHistorySecondIntegrationParameter {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Second integration parameter

## VBA Syntax

See [CWDynamicStudyOptions::TimeHistorySecondIntegrationParameter](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~TimeHistorySecondIntegrationParameter.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::TimeHistoryIntegrationMethod](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryIntegrationMethod.html) = 0 (Newmark).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::TimeHistoryFirstIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryFirstIntegrationParameter.html)
[ICWDynamicStudyOptions::TimeHistoryWilsonTheta Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryWilsonTheta.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
