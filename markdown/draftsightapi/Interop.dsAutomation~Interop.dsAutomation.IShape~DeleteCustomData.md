---
title: "DeleteCustomData Method (IShape)"
project: ""
interface: "IShape"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~DeleteCustomData.html"
---

# DeleteCustomData Method (IShape)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the shape.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[IShape::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~GetCustomData.html)
[IShape::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~SetCustomData.html)
[IShape::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IShape~Handle.html)

## Availability

DraftSight V1R4.0
