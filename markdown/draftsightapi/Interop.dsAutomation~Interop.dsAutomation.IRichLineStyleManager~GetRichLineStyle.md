---
title: "GetRichLineStyle Method (IRichLineStyleManager)"
project: ""
interface: "IRichLineStyleManager"
member: "GetRichLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager~GetRichLineStyle.html"
---

# GetRichLineStyle Method (IRichLineStyleManager)

Gets the specified RichLineStyle for the document.

## Syntax

### Visual Basic

```vb
Function GetRichLineStyle( _
   ByVal Name As System.String _
) As RichLineStyle
```

### C#

```csharp
RichLineStyle GetRichLineStyle(
   System.string Name
)
```

### JScript

```
function GetRichLineStyle(
   Name : System.String
) : RichLineStyle;
```

### Managed Extensions for C++

```
RichLineStyle* GetRichLineStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
RichLineStyle^ GetRichLineStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of RichLineStyle

### Return Value

[RichLineStyle](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)

## See Also

[IRichLineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager.html)
[IRichLineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager_members.html)
[IRichLineStyleManager::GetRichLineStyles Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager~GetRichLineStyles.html)
[IRichLineStyleManager::GetActiveRichLineStyle Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager~GetActiveRichLineStyle.html)

## Availability

DraftSight V1R1.1
