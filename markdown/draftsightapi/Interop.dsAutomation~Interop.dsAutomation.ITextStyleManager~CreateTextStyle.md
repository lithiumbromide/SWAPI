---
title: "CreateTextStyle Method (ITextStyleManager)"
project: ""
interface: "ITextStyleManager"
member: "CreateTextStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~CreateTextStyle.html"
---

# CreateTextStyle Method (ITextStyleManager)

Creates the specified TextStyle.

## Syntax

### Visual Basic

```vb
Sub CreateTextStyle( _
   ByVal Name As System.String, _
   ByRef TextStyle As TextStyle, _
   ByRef Result As dsCreateObjectResult_e _
)
```

### C#

```csharp
void CreateTextStyle(
   System.string Name,
   out TextStyle TextStyle,
   out dsCreateObjectResult_e Result
)
```

### JScript

```
function CreateTextStyle(
   Name : System.String,
   TextStyle : TextStyle,
   Result : dsCreateObjectResult_e
);
```

### Managed Extensions for C++

```
void CreateTextStyle(
   System.string* Name,
   [PARAMFLAG::Out] TextStyle* TextStyle,
   [PARAMFLAG::Out] dsCreateObjectResult_e Result
)
```

### C++/CLI

```cpp
void CreateTextStyle(
   System.String^ Name,
   [Out] TextStyle^ TextStyle,
   [Out] dsCreateObjectResult_e Result
)
```

### Parameters

- `Name`: Name
- `TextStyle`: [TextStyle](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
- `Result`: Status of creating the TextStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[ITextStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager.html)
[ITextStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager_members.html)
[ITextStyleManager::RemoveTextStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyleManager~RemoveTextStyle.html)

## Availability

DraftSight V1R1.1
