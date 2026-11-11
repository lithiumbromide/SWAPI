---
title: "GetElementAt Method (IMathTransform)"
project: ""
interface: "IMathTransform"
member: "GetElementAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathTransform~GetElementAt.html"
---

# GetElementAt Method (IMathTransform)

Gets the value in the specified row and column of this transformation matrix.

## Syntax

### Visual Basic

```vb
Function GetElementAt( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetElementAt(
   System.int Row,
   System.int Column
)
```

### JScript

```
function GetElementAt(
   Row : System.int,
   Column : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetElementAt(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.double GetElementAt(
   System.int Row,
   System.int Column
)
```

### Parameters

- `Row`: Row position of transformation matrix
- `Column`: Column position of transformation matrix

### Return Value

Value of element in Row and Column

## Examples

[Rotate, Scale, Project, and Mirror a Line Entity (JavaScript)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_JS.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VB.NET)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (C#)](Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_CSharp.htm)
[Rotate, Scale, Project, and Mirror a Line Entity (VBA)](Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm)

## See Also

[IMathTransform Interface](Interop.dsAutomation~Interop.dsAutomation.IMathTransform.html)
[IMathTransform Members](Interop.dsAutomation~Interop.dsAutomation.IMathTransform_members.html)
[IMathTransform::SetElementAt Method](Interop.dsAutomation~Interop.dsAutomation.IMathTransform~SetElementAt.html)

## Availability

DraftSight V1R1.4
