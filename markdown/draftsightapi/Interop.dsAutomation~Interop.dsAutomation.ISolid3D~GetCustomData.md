---
title: "GetCustomData Method (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~GetCustomData.html"
---

# GetCustomData Method (ISolid3D)

Gets the specified custom data for this 3D solid.

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

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)
[ISolid3D::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~DeleteCustomData.html)
[ISolid3D::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISolid3D~SetCustomData.html)

## Availability

DraftSight 2020 SP0
