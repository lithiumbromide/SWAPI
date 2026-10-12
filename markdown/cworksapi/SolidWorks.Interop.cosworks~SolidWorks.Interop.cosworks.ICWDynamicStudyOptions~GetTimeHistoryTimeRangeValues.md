---
title: "GetTimeHistoryTimeRangeValues Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetTimeHistoryTimeRangeValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues.html"
---

# GetTimeHistoryTimeRangeValues Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetTimeHistoryTimeRangeValues( _
   ByRef DStartTime As System.Double, _
   ByRef DEndTime As System.Double, _
   ByRef DTimeIncrement As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DStartTime As System.Double
Dim DEndTime As System.Double
Dim DTimeIncrement As System.Double

instance.GetTimeHistoryTimeRangeValues(DStartTime, DEndTime, DTimeIncrement)
```

### C#

```csharp
void GetTimeHistoryTimeRangeValues(
   out System.double DStartTime,
   out System.double DEndTime,
   out System.double DTimeIncrement
)
```

### C++/CLI

```cpp
void GetTimeHistoryTimeRangeValues(
   [Out] System.double DStartTime,
   [Out] System.double DEndTime,
   [Out] System.double DTimeIncrement
)
```

### Parameters

- `DStartTime`: Start time
- `DEndTime`: End time
- `DTimeIncrement`: Time increment

## VBA Syntax

See [CWDynamicStudyOptions::GetTimeHistoryTimeRangeValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetTimeHistoryTimeRangeValues.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
