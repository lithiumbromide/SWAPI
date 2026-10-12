---
title: "TimeHistoryIntegrationMethod Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "TimeHistoryIntegrationMethod"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryIntegrationMethod.html"
---

# TimeHistoryIntegrationMethod Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistoryIntegrationMethod2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryIntegrationMethod2.html) and [ICWDynamicStudyOptions::SetTimeHistoryIntegrationMethod2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryIntegrationMethod2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeHistoryIntegrationMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Integer

instance.TimeHistoryIntegrationMethod = value

value = instance.TimeHistoryIntegrationMethod
```

### C#

```csharp
System.int TimeHistoryIntegrationMethod {get; set;}
```

### C++/CLI

```cpp
property System.int TimeHistoryIntegrationMethod {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Integration method as defined in [swsTimeIntegrationMethod_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsTimeIntegrationMethod_e.html)

## VBA Syntax

See [CWDynamicStudyOptions::TimeHistoryIntegrationMethod](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~TimeHistoryIntegrationMethod.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::TimeHistoryFirstIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryFirstIntegrationParameter.html)
[ICWDynamicStudyOptions::TimeHistorySecondIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistorySecondIntegrationParameter.html)
[ICWDynamicStudyOptions::TimeHistoryWilsonTheta Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryWilsonTheta.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
