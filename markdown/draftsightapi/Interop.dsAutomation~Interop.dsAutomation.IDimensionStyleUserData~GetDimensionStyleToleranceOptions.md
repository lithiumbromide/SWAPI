---
title: "GetDimensionStyleToleranceOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleToleranceOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleToleranceOptions.html"
---

# GetDimensionStyleToleranceOptions Method (IDimensionStyleUserData)

Gets access to the tolerance options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleToleranceOptions() As DimensionStyleToleranceOptions
```

### C#

```csharp
DimensionStyleToleranceOptions GetDimensionStyleToleranceOptions()
```

### JScript

```
function GetDimensionStyleToleranceOptions() : DimensionStyleToleranceOptions;
```

### Managed Extensions for C++

```
DimensionStyleToleranceOptions* GetDimensionStyleToleranceOptions();
```

### C++/CLI

```cpp
DimensionStyleToleranceOptions^ GetDimensionStyleToleranceOptions();
```

### Return Value

[Tolerance options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html) for a Dimension, Leader, or geometric Tolerance entity

## Remarks

This method allows you to get or set the tolerance options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the tolerance options for all entities, use [IDimensionStyle::GetDimensionStyleToleranceOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleToleranceOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
