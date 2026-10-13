---
title: "SetTimeHistoryTimeRangeValues Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetTimeHistoryTimeRangeValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues.html"
---

# SetTimeHistoryTimeRangeValues Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetTimeHistoryTimeRangeValues2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryTimeRangeValues2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTimeHistoryTimeRangeValues( _
   ByVal DStartTime As System.Double, _
   ByVal DEndTime As System.Double, _
   ByVal DTimeIncrement As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim DStartTime As System.Double
Dim DEndTime As System.Double
Dim DTimeIncrement As System.Double

instance.SetTimeHistoryTimeRangeValues(DStartTime, DEndTime, DTimeIncrement)
```

### C#

```csharp
void SetTimeHistoryTimeRangeValues(
   System.double DStartTime,
   System.double DEndTime,
   System.double DTimeIncrement
)
```

### C++/CLI

```cpp
void SetTimeHistoryTimeRangeValues(
   System.double DStartTime,
   System.double DEndTime,
   System.double DTimeIncrement
)
```

### Parameters

- `DStartTime`: Start time
- `DEndTime`: End time
- `DTimeIncrement`: Time increment

## VBA Syntax

See [CWDynamicStudyOptions::SetTimeHistoryTimeRangeValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetTimeHistoryTimeRangeValues.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetTimeHistoryTimeRangeValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryTimeRangeValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
