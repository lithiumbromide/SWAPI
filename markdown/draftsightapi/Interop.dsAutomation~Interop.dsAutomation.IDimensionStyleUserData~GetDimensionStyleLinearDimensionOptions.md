---
title: "GetDimensionStyleLinearDimensionOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleLinearDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleLinearDimensionOptions.html"
---

# GetDimensionStyleLinearDimensionOptions Method (IDimensionStyleUserData)

Gets access to the linear Dimension options of the DimensionStyle for a [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleLinearDimensionOptions() As DimensionStyleLinearDimensionOptions
```

### C#

```csharp
DimensionStyleLinearDimensionOptions GetDimensionStyleLinearDimensionOptions()
```

### JScript

```
function GetDimensionStyleLinearDimensionOptions() : DimensionStyleLinearDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleLinearDimensionOptions* GetDimensionStyleLinearDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleLinearDimensionOptions^ GetDimensionStyleLinearDimensionOptions();
```

### Return Value

[Linear Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions.html) for a Dimension, Leader, or geometric Tolerance

## Remarks

This method allows you to get or set the linear Dimension options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the linear Dimension options for all entities, use [IDimensionStyle::GetDimensionStyleLinearDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleLinearDimensionOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
