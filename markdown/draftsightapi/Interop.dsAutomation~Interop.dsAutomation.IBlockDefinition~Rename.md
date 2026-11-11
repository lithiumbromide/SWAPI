---
title: "Rename Method (IBlockDefinition)"
project: ""
interface: "IBlockDefinition"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~Rename.html"
---

# Rename Method (IBlockDefinition)

Renames this Block definition and all child Block instances.

## Syntax

### Visual Basic

```vb
Function Rename( _
   ByVal BlockName As System.String _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e Rename(
   System.string BlockName
)
```

### JScript

```
function Rename(
   BlockName : System.String
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e Rename(
   System.string* BlockName
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e Rename(
   System.String^ BlockName
)
```

### Parameters

- `BlockName`: New name for this Block definition

### Return Value

Status of renaming the Block definition as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[IBlockDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html)
[IBlockDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition_members.html)

## Availability

DraftSight 2018 SP0
