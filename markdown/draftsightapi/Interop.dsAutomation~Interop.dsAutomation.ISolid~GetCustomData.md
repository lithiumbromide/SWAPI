---
title: "GetCustomData Method (ISolid)"
project: ""
interface: "ISolid"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid~GetCustomData.html"
---

# GetCustomData Method (ISolid)

Gets the specified custom data for the 2D Solid.

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

[ISolid Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid.html)
[ISolid Members](Interop.dsAutomation~Interop.dsAutomation.ISolid_members.html)
[ISolid::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~DeleteCustomData.html)
[ISolid::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISolid~SetCustomData.html)
[ISolid::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISolid~Handle.html)

## Availability

DraftSight V1R1.3
