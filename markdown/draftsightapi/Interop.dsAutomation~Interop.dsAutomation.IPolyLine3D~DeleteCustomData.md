---
title: "DeleteCustomData Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~DeleteCustomData.html"
---

# DeleteCustomData Method (IPolyLine3D)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the 3D PolyLine.

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

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetCustomData.html)
[IPolyLine3D::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~SetCustomData.html)
[IPolyLine3D::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Handle.html)

## Availability

DraftSight V1R1.3
