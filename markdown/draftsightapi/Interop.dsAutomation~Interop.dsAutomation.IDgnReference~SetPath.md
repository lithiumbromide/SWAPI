---
title: "SetPath Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "SetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetPath.html"
---

# SetPath Method (IDgnReference)

Gets the original path of this DGN reference.

## Syntax

### Visual Basic

```vb
Sub SetPath( _
   ByVal DgnPath As System.String _
)
```

### C#

```csharp
void SetPath(
   System.string DgnPath
)
```

### JScript

```
function SetPath(
   DgnPath : System.String
);
```

### Managed Extensions for C++

```
void SetPath(
   System.string* DgnPath
)
```

### C++/CLI

```cpp
void SetPath(
   System.String^ DgnPath
)
```

### Parameters

- `DgnPath`: Saved path

## Remarks

This method sets the **Saved path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetPath.html)

## Availability

DraftSight 2020 SP0
