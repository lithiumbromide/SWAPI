---
title: "GetParents Method (IExternalReference)"
project: ""
interface: "IExternalReference"
member: "GetParents"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetParents.html"
---

# GetParents Method (IExternalReference)

Gets the parent external references for the external reference.

## Syntax

### Visual Basic

```vb
Function GetParents() As System.Object
```

### C#

```csharp
System.object GetParents()
```

### JScript

```
function GetParents() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetParents();
```

### C++/CLI

```cpp
System.Object^ GetParents();
```

### Return Value

Array of [parent external references](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)

## Remarks

IExternalReference::GetParents gets all parent external references as an array of external references. However, a parent external reference might not be a top-level external reference (e.g., an external reference might have more than one parent). Use [IExternalReference::IsTopLevel](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~IsTopLevel.html) to determine if a parent external reference is a top-level reference.

## See Also

[IExternalReference Interface](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html)
[IExternalReference Members](Interop.dsAutomation~Interop.dsAutomation.IExternalReference_members.html)
[IExternalReference::GetChildren Method](Interop.dsAutomation~Interop.dsAutomation.IExternalReference~GetChildren.html)

## Availability

DraftSight V1R1
