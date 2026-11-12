---
title: "GetCustomData Method (IPoint)"
project: ""
interface: "IPoint"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPoint~GetCustomData.html"
---

# GetCustomData Method (IPoint)

Gets the specified custom data for the point.

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

[IPoint Interface](Interop.dsAutomation~Interop.dsAutomation.IPoint.html)
[IPoint Members](Interop.dsAutomation~Interop.dsAutomation.IPoint_members.html)
[IPoint::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPoint~DeleteCustomData.html)
[IPoint::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPoint~SetCustomData.html)
[IPoint::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPoint~Handle.html)

## Availability

DraftSight V1R1.2
