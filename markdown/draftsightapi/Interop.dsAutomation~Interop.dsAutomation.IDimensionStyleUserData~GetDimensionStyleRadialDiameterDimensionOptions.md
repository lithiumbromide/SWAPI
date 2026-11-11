---
title: "GetDimensionStyleRadialDiameterDimensionOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleRadialDiameterDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleRadialDiameterDimensionOptions.html"
---

# GetDimensionStyleRadialDiameterDimensionOptions Method (IDimensionStyleUserData)

Gets access to radius or diameter Dimension options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleRadialDiameterDimensionOptions() As DimensionStyleRadialDiameterDimensionOptions
```

### C#

```csharp
DimensionStyleRadialDiameterDimensionOptions GetDimensionStyleRadialDiameterDimensionOptions()
```

### JScript

```
function GetDimensionStyleRadialDiameterDimensionOptions() : DimensionStyleRadialDiameterDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleRadialDiameterDimensionOptions* GetDimensionStyleRadialDiameterDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleRadialDiameterDimensionOptions^ GetDimensionStyleRadialDiameterDimensionOptions();
```

### Return Value

[Radius or diameter Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions.html) for a Dimension, Leader, or geometric Tolerance entity

## Remarks

This method allows you to get or set the radius or diameter Dimension options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the radius or diameter Dimension options for all entities, use [IDimensionStyle::GetDimensionStyleRadialDiameterDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleRadialDiameterDimensionOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
