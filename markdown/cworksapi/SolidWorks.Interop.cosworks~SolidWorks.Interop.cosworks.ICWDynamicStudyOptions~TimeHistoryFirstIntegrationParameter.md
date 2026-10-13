---
title: "TimeHistoryFirstIntegrationParameter Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "TimeHistoryFirstIntegrationParameter"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryFirstIntegrationParameter.html"
---

# TimeHistoryFirstIntegrationParameter Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistoryFirstIntegrationParameter2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryFirstIntegrationParameter2.html) and [ICWDynamicStudyOptions::SetTimeHistoryFirstIntegrationParameter2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryFirstIntegrationParameter2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeHistoryFirstIntegrationParameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.TimeHistoryFirstIntegrationParameter = value

value = instance.TimeHistoryFirstIntegrationParameter
```

### C#

```csharp
System.double TimeHistoryFirstIntegrationParameter {get; set;}
```

### C++/CLI

```cpp
property System.double TimeHistoryFirstIntegrationParameter {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

First integration parameter

## VBA Syntax

See [CWDynamicStudyOptions::TimeHistoryFirstIntegrationParameter](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~TimeHistoryFirstIntegrationParameter.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::TimeHistoryIntegrationMethod](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryIntegrationMethod.html) = 0 (Newmark).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::TimeHistorySecondIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistorySecondIntegrationParameter.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
