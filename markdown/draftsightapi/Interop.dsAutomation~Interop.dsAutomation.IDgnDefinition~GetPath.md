---
title: "GetPath Method (IDgnDefinition)"
project: ""
interface: "IDgnDefinition"
member: "GetPath"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~GetPath.html"
---

# GetPath Method (IDgnDefinition)

Gets the saved path of the reference of this DGN definition.

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

Path and file name of the saved DGN reference

## Remarks

This method returns the **Saved path** that is displayed in the File information section of the Attach Reference: DGN dialog that appears after you run the ATTACHDGN command in DraftSight.

## See Also

[IDgnDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition.html)
[IDgnDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition_members.html)
[IDgnDefinition::SetPath Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnDefinition~SetPath.html)

## Availability

DraftSight 2020 SP0
