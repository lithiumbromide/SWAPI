---
title: "SetElementAt Method (IMathTransform)"
project: ""
interface: "IMathTransform"
member: "SetElementAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathTransform~SetElementAt.html"
---

# SetElementAt Method (IMathTransform)

Sets the specified value of the element at the specified row and column of this transformation matrix.

## Syntax

### Visual Basic

```vb
Sub SetElementAt( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal NewVal As System.Double _
)
```

### C#

```csharp
void SetElementAt(
   System.int Row,
   System.int Column,
   System.double NewVal
)
```

### JScript

```
function SetElementAt(
   Row : System.int,
   Column : System.int,
   NewVal : System.double
);
```

### Managed Extensions for C++

```
void SetElementAt(
   System.int Row,
   System.int Column,
   System.double NewVal
)
```

### C++/CLI

```cpp
void SetElementAt(
   System.int Row,
   System.int Column,
   System.double NewVal
)
```

### Parameters

- `Row`: Row position of transform matrix
- `Column`: Column position of transform matrix
- `NewVal`: Value of element at Row and Column position

## See Also

[IMathTransform Interface](Interop.dsAutomation~Interop.dsAutomation.IMathTransform.html)
[IMathTransform Members](Interop.dsAutomation~Interop.dsAutomation.IMathTransform_members.html)
[IMathTransform::GetElementAt Method](Interop.dsAutomation~Interop.dsAutomation.IMathTransform~GetElementAt.html)

## Availability

DraftSight V1R1.4
