---
title: "GetDimensionStyleLineOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleLineOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleLineOptions.html"
---

# GetDimensionStyleLineOptions Method (IDimensionStyleUserData)

Gets access to the line options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleLineOptions() As DimensionStyleLineOptions
```

### C#

```csharp
DimensionStyleLineOptions GetDimensionStyleLineOptions()
```

### JScript

```
function GetDimensionStyleLineOptions() : DimensionStyleLineOptions;
```

### Managed Extensions for C++

```
DimensionStyleLineOptions* GetDimensionStyleLineOptions();
```

### C++/CLI

```cpp
DimensionStyleLineOptions^ GetDimensionStyleLineOptions();
```

### Return Value

[Line options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLineOptions.html) for a Dimension, Leader, or geometric Tolerance

## Remarks

This method allows you to get or set the line options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the line options for all entities, use [IDimensionStyle::GetDimensionStyleLineOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleLineOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
