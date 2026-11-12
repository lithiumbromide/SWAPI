---
title: "RemoveLineStyle Method (ILineStyleManager)"
project: ""
interface: "ILineStyleManager"
member: "RemoveLineStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager~RemoveLineStyle.html"
---

# RemoveLineStyle Method (ILineStyleManager)

Removes the specified simple [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) from the document.

## Syntax

### Visual Basic

```vb
Function RemoveLineStyle( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveLineStyle(
   System.string Name
)
```

### JScript

```
function RemoveLineStyle(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveLineStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveLineStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the simple LineStyle to remove from the document

### Return Value

True if the simple LineStyle is removed from the document, false if not

## See Also

[ILineStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager.html)
[ILineStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyleManager_members.html)
[ILineStyle::Name Property ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Name.html)

## Availability

DraftSight V1R4.0
