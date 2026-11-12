---
title: "GetPath Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "GetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetPath.html"
---

# GetPath Method (IDgnReference)

Gets the original path of this DGN reference.

## Syntax

### Visual Basic

```vb
Function GetPath() As System.String
```

### C#

```csharp
System.string GetPath()
```

### JScript

```
function GetPath() : System.String;
```

### Managed Extensions for C++

```
System.string* GetPath();
```

### C++/CLI

```cpp
System.String^ GetPath();
```

### Return Value

Saved path

## Remarks

This method returns the **Saved path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::GetFoundInPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetFoundInPath.html)
[IDgnReference::SetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetPath.html)

## Availability

DraftSight 2020 SP0
