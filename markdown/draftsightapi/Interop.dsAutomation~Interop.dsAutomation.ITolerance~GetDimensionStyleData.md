---
title: "GetDimensionStyleData Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "GetDimensionStyleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetDimensionStyleData.html"
---

# GetDimensionStyleData Method (ITolerance)

Gets the DimensionStyle of the geometric Tolerance.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleData() As DimensionStyle
```

### C#

```csharp
DimensionStyle GetDimensionStyleData()
```

### JScript

```
function GetDimensionStyleData() : DimensionStyle;
```

### Managed Extensions for C++

```
DimensionStyle* GetDimensionStyleData();
```

### C++/CLI

```cpp
DimensionStyle^ GetDimensionStyleData();
```

### Return Value

[DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)

## Remarks

If you change a DimensionStyle, then all entities using that DimensionStyle also change. However, if you use the [IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html) interface, then you can change the DimensionStyle of a specific geometric Tolerance entity and not change all other entities using that DimensionStyle.

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::DimensionStyle Property](Interop.dsAutomation~Interop.dsAutomation.ITolerance~DimensionStyle.html)

## Availability

DraftSight V1R1.2
