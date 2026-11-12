---
title: "Rename Method (INamedView)"
project: ""
interface: "INamedView"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.INamedView~Rename.html"
---

# Rename Method (INamedView)

Renames this named view with the specified new name.

## Syntax

### Visual Basic

```vb
Function Rename( _
   ByVal NewName As System.String _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e Rename(
   System.string NewName
)
```

### JScript

```
function Rename(
   NewName : System.String
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e Rename(
   System.string* NewName
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e Rename(
   System.String^ NewName
)
```

### Parameters

- `NewName`: New name of this named view

### Return Value

Result status as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[INamedView Interface](Interop.dsAutomation~Interop.dsAutomation.INamedView.html)
[INamedView Members](Interop.dsAutomation~Interop.dsAutomation.INamedView_members.html)

## Availability

DraftSight V1R1.4
