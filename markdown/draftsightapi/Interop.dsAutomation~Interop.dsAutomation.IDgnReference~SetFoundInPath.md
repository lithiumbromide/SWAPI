---
title: "SetFoundInPath Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "SetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetFoundInPath.html"
---

# SetFoundInPath Method (IDgnReference)

Sets the found in path for this DGN reference.

## Syntax

### Visual Basic

```vb
Sub SetFoundInPath( _
   ByVal FoundInPath As System.String _
)
```

### C#

```csharp
void SetFoundInPath(
   System.string FoundInPath
)
```

### JScript

```
function SetFoundInPath(
   FoundInPath : System.String
);
```

### Managed Extensions for C++

```
void SetFoundInPath(
   System.string* FoundInPath
)
```

### C++/CLI

```cpp
void SetFoundInPath(
   System.String^ FoundInPath
)
```

### Parameters

- `FoundInPath`: Found in path

## Remarks

This method sets the **Found in path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)

## Availability

DraftSight 2020 SP1
