---
title: "GetTimeHistoryDeadLoadOptions Method (ICWDynamicStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicStudyOptions"
member: "GetTimeHistoryDeadLoadOptions"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions.html"
---

# GetTimeHistoryDeadLoadOptions Method (ICWDynamicStudyOptions)

Obsolete. Superseded by [ICWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions2.](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetTimeHistoryDeadLoadOptions( _
   ByRef BChecked As System.Integer, _
   ByRef SStudyName As System.String, _
   ByRef DMultiplicationFactor As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicStudyOptions
Dim BChecked As System.Integer
Dim SStudyName As System.String
Dim DMultiplicationFactor As System.Double

instance.GetTimeHistoryDeadLoadOptions(BChecked, SStudyName, DMultiplicationFactor)
```

### C#

```csharp
void GetTimeHistoryDeadLoadOptions(
   out System.int BChecked,
   out System.string SStudyName,
   out System.double DMultiplicationFactor
)
```

### C++/CLI

```cpp
void GetTimeHistoryDeadLoadOptions(
   [Out] System.int BChecked,
   [Out] System.String^ SStudyName,
   [Out] System.double DMultiplicationFactor
)
```

### Parameters

- `BChecked`: 1 to get dead loads from a static study, 0 to not
- `SStudyName`: Name of the static study
- `DMultiplicationFactor`: Multiplication factor

## VBA Syntax

See [CWDynamicStudyOptions::GetTimeHistoryDeadLoadOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicStudyOptions~GetTimeHistoryDeadLoadOptions.html).

## See Also

[ICWDynamicStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions.html)
[ICWDynamicStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions_members.html)
[ICWDynamicStudyOptions::SetTimeHistoryDeadLoadOptions Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicStudyOptions~SetTimeHistoryDeadLoadOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
