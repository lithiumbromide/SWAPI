---
title: "GetTextStyle Method (ITextStyleManager)"
project: ""
interface: "ITextStyleManager"
member: "GetTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~GetTextStyle.html"
---

# GetTextStyle Method (ITextStyleManager)

Gets the specified TextStyle.

## Syntax

### Visual Basic

```vb
Function GetTextStyle( _
   ByVal Name As System.String _
) As TextStyle
```

### C#

```csharp
TextStyle GetTextStyle(
   System.string Name
)
```

### JScript

```
function GetTextStyle(
   Name : System.String
) : TextStyle;
```

### Managed Extensions for C++

```
TextStyle* GetTextStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
TextStyle^ GetTextStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of TextStyle

### Return Value

[TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)

## See Also

[ITextStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager.html)
[ITextStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager_members.html)
[ITextStyleManager::GetTextStyles Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~GetTextStyles.html)
[ITextStyleManager::GetActiveTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~GetActiveTextStyle.html)

## Availability

DraftSight V1R1.1
