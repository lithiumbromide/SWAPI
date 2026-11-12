---
title: "GetFoundInPath Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "GetFoundInPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetFoundInPath.html"
---

# GetFoundInPath Method (IDgnDefinition)

Gets the found in path for the reference of this DGN definition.

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

DGN reference copy location

## Remarks

This method returns the **Found in path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)

## Availability

DraftSight 2020 SP0
