---
title: "GetDimensionStyleAngularDimensionOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleAngularDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleAngularDimensionOptions.html"
---

# GetDimensionStyleAngularDimensionOptions Method (IDimensionStyleUserData)

Gets access to the angular Dimension options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleAngularDimensionOptions() As DimensionStyleAngularDimensionOptions
```

### C#

```csharp
DimensionStyleAngularDimensionOptions GetDimensionStyleAngularDimensionOptions()
```

### JScript

```
function GetDimensionStyleAngularDimensionOptions() : DimensionStyleAngularDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleAngularDimensionOptions* GetDimensionStyleAngularDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleAngularDimensionOptions^ GetDimensionStyleAngularDimensionOptions();
```

### Return Value

[Angular Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleAngularDimensionOptions.html) of a Dimension, Leader, or geometric Tolerance entity

## Remarks

This method allows you to get or set the angular Dimension options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the angular Dimension options for all entities, use [IDimensionStyle::GetDimensionStyleAngularDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleAngularDimensionOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
