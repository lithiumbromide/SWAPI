---
title: "SetAutomaticTimeIncrement Method (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "SetAutomaticTimeIncrement"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~SetAutomaticTimeIncrement.html"
---

# SetAutomaticTimeIncrement Method (ICWNonLinearStudyOptions)

Sets the parameters for automatic stepping.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAutomaticTimeIncrement( _
   ByVal DInitialTimeIncrement As System.Double, _
   ByVal DMiNVal As System.Double, _
   ByVal DMaxVal As System.Double, _
   ByVal NNoOfAdjustments As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim DInitialTimeIncrement As System.Double
Dim DMiNVal As System.Double
Dim DMaxVal As System.Double
Dim NNoOfAdjustments As System.Integer

instance.SetAutomaticTimeIncrement(DInitialTimeIncrement, DMiNVal, DMaxVal, NNoOfAdjustments)
```

### C#

```csharp
void SetAutomaticTimeIncrement(
   System.double DInitialTimeIncrement,
   System.double DMiNVal,
   System.double DMaxVal,
   System.int NNoOfAdjustments
)
```

### C++/CLI

```cpp
void SetAutomaticTimeIncrement(
   System.double DInitialTimeIncrement,
   System.double DMiNVal,
   System.double DMaxVal,
   System.int NNoOfAdjustments
)
```

### Parameters

- `DInitialTimeIncrement`: Initial time increment
- `DMiNVal`: Minimum value
- `DMaxVal`: Maximum value
- `NNoOfAdjustments`: Maximum allowed number of adjustments

## VBA Syntax

See [CWNonLinearStudyOptions::SetAutomaticTimeIncrement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~SetAutomaticTimeIncrement.html).

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::GetAutomaticTimeIncrement Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~GetAutomaticTimeIncrement.html)
[ICWNonLinearStudyOptions::EndTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~EndTime.html)
[ICWNonLinearStudyOptions::FixedTimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FixedTimeIncrement.html)
[ICWNonLinearStudyOptions::StartTime Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~StartTime.html)
[ICWNonLinearStudyOptions::TimeIncrement Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~TimeIncrement.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
