---
title: "GetDimensionStyleFitOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleFitOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleFitOptions.html"
---

# GetDimensionStyleFitOptions Method (IDimensionStyleUserData)

Gets access to the fit options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleFitOptions() As DimensionStyleFitOptions
```

### C#

```csharp
DimensionStyleFitOptions GetDimensionStyleFitOptions()
```

### JScript

```
function GetDimensionStyleFitOptions() : DimensionStyleFitOptions;
```

### Managed Extensions for C++

```
DimensionStyleFitOptions* GetDimensionStyleFitOptions();
```

### C++/CLI

```cpp
DimensionStyleFitOptions^ GetDimensionStyleFitOptions();
```

### Return Value

[Fit options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions.html) for a Dimension, Leader, or geometric Tolerance

## Remarks

This method allows you to get or set the fit options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the fit options for all entities, use [IDimensionStyle::GetDimensionStyleFitOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleFitOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
