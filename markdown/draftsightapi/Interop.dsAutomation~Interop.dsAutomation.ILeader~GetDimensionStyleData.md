---
title: "GetDimensionStyleData Method (ILeader)"
project: ""
interface: "ILeader"
member: "GetDimensionStyleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~GetDimensionStyleData.html"
---

# GetDimensionStyleData Method (ILeader)

Gets the DimensionStyle for the Leader.

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

If you change a DimensionStyle, then all entities using that DimensionStyle also change. However, if you use the [IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html) interface, then you can change the DimensionStyle of a specific Leader entity and not change all other entities using that DimensionStyle.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)
[ILeader::DimensionStyle Method](Interop.dsAutomation~Interop.dsAutomation.ILeader~DimensionStyle.html)

## Availability

DraftSight V1R1.2
