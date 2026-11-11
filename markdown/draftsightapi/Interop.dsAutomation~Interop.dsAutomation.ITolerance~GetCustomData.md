---
title: "GetCustomData Method (ITolerance)"
project: ""
interface: "ITolerance"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITolerance~GetCustomData.html"
---

# GetCustomData Method (ITolerance)

Gets the specified custom data for the geometric Tolerance.

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

[ITolerance Interface](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html)
[ITolerance Members](Interop.dsAutomation~Interop.dsAutomation.ITolerance_members.html)
[ITolerance::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~DeleteCustomData.html)
[ITolerance::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITolerance~SetCustomData.html)
[ITolerance::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITolerance~Handle.html)

## Availability

DraftSight V1R1.2
