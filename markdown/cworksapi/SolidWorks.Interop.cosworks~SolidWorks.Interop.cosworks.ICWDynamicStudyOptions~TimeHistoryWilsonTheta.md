---
title: "TimeHistoryWilsonTheta Property (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "TimeHistoryWilsonTheta"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryWilsonTheta.html"
---

# TimeHistoryWilsonTheta Property (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistoryWilsonTheta2](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryWilsonTheta2.html) and [ICWDynamicStudyOptions::SetTimeHistoryWilsonTheta2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryWilsonTheta2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Property TimeHistoryWilsonTheta As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim value As System.Double

instance.TimeHistoryWilsonTheta = value

value = instance.TimeHistoryWilsonTheta
```

### C#

```csharp
System.double TimeHistoryWilsonTheta {get; set;}
```

### C++/CLI

```cpp
property System.double TimeHistoryWilsonTheta {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Theta value (see **Remarks**)

## VBA Syntax

See [CWDynamicStudyOptions::TimeHistoryWilsonTheta](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~TimeHistoryWilsonTheta.html).

## Remarks

This property is valid only if [ICWDynamicStudyOptions::TimeHistoryIntegrationMethod](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryIntegrationMethod.html) = 1 (Wilson Theta).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::TimeHistoryFirstIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistoryFirstIntegrationParameter.html)
[ICWDynamicStudyOptions::TimeHistorySecondIntegrationParameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~TimeHistorySecondIntegrationParameter.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
