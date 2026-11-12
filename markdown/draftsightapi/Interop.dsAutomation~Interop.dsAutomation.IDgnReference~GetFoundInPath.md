---
title: "GetFoundInPath Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "GetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetFoundInPath.html"
---

# GetFoundInPath Method (IDgnReference)

Gets the found in path for this DGN reference.

## Syntax

### Visual Basic

```vb
Function GetFoundInPath() As System.String
```

### C#

```csharp
System.string GetFoundInPath()
```

### JScript

```
function GetFoundInPath() : System.String;
```

### Managed Extensions for C++

```
System.string* GetFoundInPath();
```

### C++/CLI

```cpp
System.String^ GetFoundInPath();
```

### Return Value

Found in path

## Remarks

This method returns the **Found in path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetPath.html)

## Availability

DraftSight 2020 SP0
