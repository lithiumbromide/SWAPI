---
title: "SetPath Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "SetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~SetPath.html"
---

# SetPath Method (IDgnDefinition)

Sets the saved path of the reference of this DGN definition.

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

- `DgnPath`: Path and file name of the saved DGN reference

## Remarks

This method sets the **Saved path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::GetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetPath.html)

## Availability

DraftSight 2020 SP0
