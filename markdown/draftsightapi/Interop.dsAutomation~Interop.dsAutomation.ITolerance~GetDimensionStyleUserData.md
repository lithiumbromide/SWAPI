---
title: "GetDimensionStyleUserData Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "GetDimensionStyleUserData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetDimensionStyleUserData.html"
---

# GetDimensionStyleUserData Method (ITolerance)

Gets the DimensionStyle user data, including overrides, of the geometric Tolerance.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleUserData() As DimensionStyleUserData
```

### C#

```csharp
DimensionStyleUserData GetDimensionStyleUserData()
```

### JScript

```
function GetDimensionStyleUserData() : DimensionStyleUserData;
```

### Managed Extensions for C++

```
DimensionStyleUserData* GetDimensionStyleUserData();
```

### C++/CLI

```cpp
DimensionStyleUserData^ GetDimensionStyleUserData();
```

### Return Value

[IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)

## Remarks

If you change a [DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html), then all entities using that DimensionStyle also change. However, if you use the IDimensionStyleUserData interface, then you can change the DimensionStyle of a specific geometric Tolerance entity and not change all other entities using that DimensionStyle.

## See Also

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)

## Availability

DraftSight V1R4.0
