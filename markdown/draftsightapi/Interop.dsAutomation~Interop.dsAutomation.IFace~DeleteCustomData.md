---
title: "DeleteCustomData Method (IFace)"
project: ""
interface: "IFace"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IFace~DeleteCustomData.html"
---

# DeleteCustomData Method (IFace)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Face.

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

[IFace Interface](Interop.dsAutomation~Interop.dsAutomation.IFace.html)
[IFace Members](Interop.dsAutomation~Interop.dsAutomation.IFace_members.html)
[IFace::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IFace~GetCustomData.html)
[IFace::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IFace~SetCustomData.html)
[IFace::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IFace~Handle.html)

## Availability

DraftSight V1R1.3
