---
title: "GetSize Method (ICustomPropertyControl)"
project: ""
interface: "ICustomPropertyControl"
member: "GetSize"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl~GetSize.html"
---

# GetSize Method (ICustomPropertyControl)

Gets the size of the custom tab.

## Syntax

### Visual Basic

```vb
Sub GetSize( _
   ByRef Width As System.Integer, _
   ByRef Height As System.Integer _
)
```

### C#

```csharp
void GetSize(
   out System.int Width,
   out System.int Height
)
```

### JScript

```
function GetSize(
   Width : System.int,
   Height : System.int
);
```

### Managed Extensions for C++

```
void GetSize(
   [PARAMFLAG::Out] System.int Width,
   [PARAMFLAG::Out] System.int Height
)
```

### C++/CLI

```cpp
void GetSize(
   [Out] System.int Width,
   [Out] System.int Height
)
```

### Parameters

- `Width`: Width of custom tab
- `Height`: Height of custom tab

## See Also

[ICustomPropertyControl Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl.html)
[ICustomPropertyControl Members](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl_members.html)

## Availability

DraftSight V1R1.3
