---
title: "CreateRichLineStyle Method (IRichLineStyleManager)"
project: ""
interface: "IRichLineStyleManager"
member: "CreateRichLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager~CreateRichLineStyle.html"
---

# CreateRichLineStyle Method (IRichLineStyleManager)

Creates a RichLineStyle for the document.

## Syntax

### Visual Basic

```vb
Sub CreateRichLineStyle( _
   ByVal Name As System.String, _
   ByRef RichLineStyle As RichLineStyle, _
   ByRef Result As dsCreateObjectResult_e _
)
```

### C#

```csharp
void CreateRichLineStyle(
   System.string Name,
   out RichLineStyle RichLineStyle,
   out dsCreateObjectResult_e Result
)
```

### JScript

```
function CreateRichLineStyle(
   Name : System.String,
   RichLineStyle : RichLineStyle,
   Result : dsCreateObjectResult_e
);
```

### Managed Extensions for C++

```
void CreateRichLineStyle(
   System.string* Name,
   [PARAMFLAG::Out] RichLineStyle* RichLineStyle,
   [PARAMFLAG::Out] dsCreateObjectResult_e Result
)
```

### C++/CLI

```cpp
void CreateRichLineStyle(
   System.String^ Name,
   [Out] RichLineStyle^ RichLineStyle,
   [Out] dsCreateObjectResult_e Result
)
```

### Parameters

- `Name`: Name
- `RichLineStyle`: [RichLineStyle](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
- `Result`: Status of creating a RichLineStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[IRichLineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager.html)
[IRichLineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager_members.html)

## Availability

DraftSight V1R1.1
