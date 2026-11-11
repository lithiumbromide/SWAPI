---
title: "GetDimensionStyleDualDimensionOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleDualDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleDualDimensionOptions.html"
---

# GetDimensionStyleDualDimensionOptions Method (IDimensionStyleUserData)

Gets access to the dual Dimension options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleDualDimensionOptions() As DimensionStyleDualDimensionOptions
```

### C#

```csharp
DimensionStyleDualDimensionOptions GetDimensionStyleDualDimensionOptions()
```

### JScript

```
function GetDimensionStyleDualDimensionOptions() : DimensionStyleDualDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleDualDimensionOptions* GetDimensionStyleDualDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleDualDimensionOptions^ GetDimensionStyleDualDimensionOptions();
```

### Return Value

[Dual Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions.html) of a Dimension, Leader, or geometric Tolerance entity

## Remarks

This method allows you to get or set the dual Dimension options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the dual Dimension options for all entities, use [IDimensionStyle::GetDimensionStyleDualDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleDualDimensionOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
