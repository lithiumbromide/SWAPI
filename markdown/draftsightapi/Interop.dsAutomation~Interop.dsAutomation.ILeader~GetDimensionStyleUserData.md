---
title: "GetDimensionStyleUserData Method (ILeader)"
project: ""
interface: "ILeader"
member: "GetDimensionStyleUserData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~GetDimensionStyleUserData.html"
---

# GetDimensionStyleUserData Method (ILeader)

Gets the DimensionStyle user data, including overrides, of the Leader.

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

## Examples

[Change DimensionStyle Options of Leader (C#)](Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm)
[Change DimensionStyle Options of Leader (VB.NET)](Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm)
[Change DimensionStyle Options of Leader (VBA)](Change_DimensionStyle_Options_of_Leader_Example_VBA.htm)

## Remarks

If you change a [DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html), then all entities using that DimensionStyle also change. However, if you get the IDimensionStyleUserData interface, then you can change the DimensionStyle of a specific Leader entity and not impact all other entities using that DimensionStyle.

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)

## Availability

DraftSight V1R4.0
