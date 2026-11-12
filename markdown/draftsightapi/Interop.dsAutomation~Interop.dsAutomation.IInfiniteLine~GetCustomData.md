---
title: "GetCustomData Method (IInfiniteLine)"
project: ""
interface: "IInfiniteLine"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~GetCustomData.html"
---

# GetCustomData Method (IInfiniteLine)

Gets the specified custom data for the InfiniteLine.

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

[IInfiniteLine Interface](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine.html)
[IInfiniteLine Members](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine_members.html)
[IInfiniteLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~DeleteCustomData.html)
[IInfiniteLine::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~SetCustomData.html)
[IInfiniteLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IInfiniteLine~Handle.html)

## Availability

DraftSight V1R1.2
