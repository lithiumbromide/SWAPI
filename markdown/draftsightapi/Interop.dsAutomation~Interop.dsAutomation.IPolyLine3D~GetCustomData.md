---
title: "GetCustomData Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetCustomData.html"
---

# GetCustomData Method (IPolyLine3D)

Gets the specified custom data for the 3D PolyLine.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~DeleteCustomData.html)
[IPolyLine3D::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~SetCustomData.html)
[IPolyLine3D::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Handle.html)

## Availability

DraftSight V1R1.3
