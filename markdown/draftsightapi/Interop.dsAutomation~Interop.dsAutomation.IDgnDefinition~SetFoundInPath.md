---
title: "SetFoundInPath Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "SetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~SetFoundInPath.html"
---

# SetFoundInPath Method (IDgnDefinition)

Sets the found in path for the reference of this DGN definition.

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

- `FoundInPath`: DGN reference copy location

## Remarks

This method sets the **Found in path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)

## Availability

DraftSight 2020 SP1
