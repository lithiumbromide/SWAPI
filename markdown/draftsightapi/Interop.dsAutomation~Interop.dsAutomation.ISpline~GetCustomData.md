---
title: "GetCustomData Method (ISpline)"
project: ""
interface: "ISpline"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISpline~GetCustomData.html"
---

# GetCustomData Method (ISpline)

Gets the specified custom data for the Spline

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

[ISpline Interface](Interop.dsAutomation~Interop.dsAutomation.ISpline.html)
[ISpline Members](Interop.dsAutomation~Interop.dsAutomation.ISpline_members.html)
[ISpline::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~DeleteCustomData.html)
[ISpline::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISpline~SetCustomData.html)
[ISpline::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISpline~Handle.html)

## Availability

DraftSight V1R1.3
