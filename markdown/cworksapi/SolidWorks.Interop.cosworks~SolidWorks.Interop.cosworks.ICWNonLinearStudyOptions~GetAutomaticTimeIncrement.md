---
title: "GetAutomaticTimeIncrement Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "GetAutomaticTimeIncrement"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html"
---

# GetAutomaticTimeIncrement Method (ICWNonLinearStudyOptions)

Gets the parameters for automatic stepping.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetAutomaticTimeIncrement( _
   ByRef DInitialTimeIncrement As System.Double, _
   ByRef DMiNVal As System.Double, _
   ByRef DMaxVal As System.Double, _
   ByRef NNoOfAdjustments As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim DInitialTimeIncrement As System.Double
Dim DMiNVal As System.Double
Dim DMaxVal As System.Double
Dim NNoOfAdjustments As System.Integer

instance.GetAutomaticTimeIncrement(DInitialTimeIncrement, DMiNVal, DMaxVal, NNoOfAdjustments)
```

### C#

```csharp
void GetAutomaticTimeIncrement(
   out System.double DInitialTimeIncrement,
   out System.double DMiNVal,
   out System.double DMaxVal,
   out System.int NNoOfAdjustments
)
```

### C++/CLI

```cpp
void GetAutomaticTimeIncrement(
   [Out] System.double DInitialTimeIncrement,
   [Out] System.double DMiNVal,
   [Out] System.double DMaxVal,
   [Out] System.int NNoOfAdjustments
)
```

### Parameters

- `DInitialTimeIncrement`: Initial time increment
- `DMiNVal`: Minimum value
- `DMaxVal`: Maximum value
- `NNoOfAdjustments`: Maximum allowed number of adjustments

## VBA Syntax

See [CWNonLinearStudyOptions::GetAutomaticTimeIncrement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~GetAutomaticTimeIncrement.html).

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::SetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::EndTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html)
[ICWNonLinearStudyOptions::FixedTimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html)
[ICWNonLinearStudyOptions::StartTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html)
[ICWNonLinearStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
