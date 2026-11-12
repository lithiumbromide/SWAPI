---
title: "Rename Method (ILayer)"
project: ""
interface: "ILayer"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Rename.html"
---

# Rename Method (ILayer)

Renames the Layer.

## Syntax

### Visual Basic

```vb
Function Rename( _
   ByVal Name As System.String _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e Rename(
   System.string Name
)
```

### JScript

```
function Rename(
   Name : System.String
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e Rename(
   System.string* Name
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e Rename(
   System.String^ Name
)
```

### Parameters

- `Name`: New name for the Layer

### Return Value

Status of renaming the Layer as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::Name Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Name.html)

## Availability

DraftSight V1R1.1
