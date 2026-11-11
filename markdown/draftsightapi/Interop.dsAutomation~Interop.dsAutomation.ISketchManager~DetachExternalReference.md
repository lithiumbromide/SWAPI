---
title: "DetachExternalReference Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "DetachExternalReference"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~DetachExternalReference.html"
---

# DetachExternalReference Method (ISketchManager)

Detaches the specified external reference from the drawing.

## Syntax

### Visual Basic

```vb
Function DetachExternalReference( _
   ByVal ExternalReference As ExternalReference _
) As System.Boolean
```

### C#

```csharp
System.bool DetachExternalReference(
   ExternalReference ExternalReference
)
```

### JScript

```
function DetachExternalReference(
   ExternalReference : ExternalReference
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DetachExternalReference(
   ExternalReference* ExternalReference
)
```

### C++/CLI

```cpp
System.bool DetachExternalReference(
   ExternalReference^ ExternalReference
)
```

### Parameters

- `ExternalReference`: [External reference](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html) to detach from the drawing

### Return Value

True if the external reference is detached from the drawing, false if not

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)
[ISketchManager::InsertExternalReference Method ()](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertExternalReference.html)

## Availability

DraftSight V1R4.0
