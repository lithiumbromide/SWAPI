---
title: "RemoveDimensionStyle Method (IDimensionStyleManager)"
project: ""
interface: "IDimensionStyleManager"
member: "RemoveDimensionStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~RemoveDimensionStyle.html"
---

# RemoveDimensionStyle Method (IDimensionStyleManager)

Removes the specified DimensionStyle.

## Syntax

### Visual Basic

```vb
Function RemoveDimensionStyle( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveDimensionStyle(
   System.string Name
)
```

### JScript

```
function RemoveDimensionStyle(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveDimensionStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveDimensionStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of DimensionStyle to remove

### Return Value

True if the DimensionStyle is removed, false if not

## See Also

[IDimensionStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager.html)
[IDimensionStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager_members.html)
[IDimensionStyleManager::CreateDimensionStyle Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~CreateDimensionStyle.html)

## Availability

DraftSight V1R1.1
