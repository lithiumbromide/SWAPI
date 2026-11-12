---
title: "SetTimeHistoryDeadLoadOptions Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "SetTimeHistoryDeadLoadOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions.html"
---

# SetTimeHistoryDeadLoadOptions Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTimeHistoryDeadLoadOptions( _
   ByVal BChecked As System.Integer, _
   ByVal SStudyName As System.String, _
   ByVal DMultiplicationFactor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Integer
Dim SStudyName As System.String
Dim DMultiplicationFactor As System.Double

instance.SetTimeHistoryDeadLoadOptions(BChecked, SStudyName, DMultiplicationFactor)
```

### C#

```csharp
void SetTimeHistoryDeadLoadOptions(
   System.int BChecked,
   System.string SStudyName,
   System.double DMultiplicationFactor
)
```

### C++/CLI

```cpp
void SetTimeHistoryDeadLoadOptions(
   System.int BChecked,
   System.String^ SStudyName,
   System.double DMultiplicationFactor
)
```

### Parameters

- `BChecked`: 1 to set dead loads for a static study, 0 to not
- `SStudyName`: Name of the study
- `DMultiplicationFactor`: Multiplication factor

## VBA Syntax

See [CWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
