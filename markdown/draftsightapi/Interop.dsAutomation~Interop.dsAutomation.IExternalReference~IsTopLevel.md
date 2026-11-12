---
title: "IsTopLevel Method (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "IsTopLevel"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~IsTopLevel.html"
---

# IsTopLevel Method (IExternalReference)

Gets whether this external reference is a top-level reference.

## Syntax

### Visual Basic

```vb
Function IsTopLevel() As System.Boolean
```

### C#

```csharp
System.bool IsTopLevel()
```

### JScript

```
function IsTopLevel() : System.boolean;
```

### Managed Extensions for C++

```
System.bool IsTopLevel();
```

### C++/CLI

```cpp
System.bool IsTopLevel();
```

### Return Value

True if this external reference is a top-level reference, false if it is not

## Remarks

[IExternalReference::GetParents](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetParents.html) gets all parent external references as an array of external references. However, a parent external reference might not be a top-level external reference (e.g., an external reference might have more than one parent). Use IExternalReference::IsTopLevel to determine if a parent external reference is a top-level reference.

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)

## Availability

DraftSight V1R5
