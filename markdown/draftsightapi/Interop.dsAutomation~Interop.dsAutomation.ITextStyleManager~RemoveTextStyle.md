---
title: "RemoveTextStyle Method (ITextStyleManager)"
project: ""
interface: "ITextStyleManager"
member: "RemoveTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~RemoveTextStyle.html"
---

# RemoveTextStyle Method (ITextStyleManager)

Removes the specified TextStyle.

## Syntax

### Visual Basic

```vb
Function RemoveTextStyle( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveTextStyle(
   System.string Name
)
```

### JScript

```
function RemoveTextStyle(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveTextStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveTextStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of TextStyle to remove

### Return Value

True if the specified TextStyle is removed, false if not

## See Also

[ITextStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager.html)
[ITextStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager_members.html)
[ITextStyleManager::CreateTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~CreateTextStyle.html)

## Availability

DraftSight V1R1.1
