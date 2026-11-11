---
title: "SetCustomData Method (IPolyLine3D)"
project: ""
interface: "IPolyLine3D"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~SetCustomData.html"
---

# SetCustomData Method (IPolyLine3D)

Sets the custom data for the 3D PolyLine.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IPolyLine3D Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D.html)
[IPolyLine3D Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D_members.html)
[IPolyLine3D::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~DeleteCustomData.html)
[IPolyLine3D::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~GetCustomData.html)
[IPolyLine3D::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine3D~Handle.html)

## Availability

DraftSight V1R1.3
