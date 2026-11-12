---
title: "RemoveRichLineStyle Method (IRichLineStyleManager)"
project: ""
interface: "IRichLineStyleManager"
member: "RemoveRichLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager~RemoveRichLineStyle.html"
---

# RemoveRichLineStyle Method (IRichLineStyleManager)

Removes the specified RichLineStyle from the document.

## Syntax

### Visual Basic

```vb
Function RemoveRichLineStyle( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveRichLineStyle(
   System.string Name
)
```

### JScript

```
function RemoveRichLineStyle(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveRichLineStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveRichLineStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of RichLineStyle to remove

### Return Value

True if the specified RichLineStyle is removed, false if not

## See Also

[IRichLineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager.html)
[IRichLineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyleManager_members.html)

## Availability

DraftSight V1R1.1
