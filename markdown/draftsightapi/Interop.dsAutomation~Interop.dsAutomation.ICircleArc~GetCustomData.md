---
title: "GetCustomData Method (ICircleArc)"
project: ""
interface: "ICircleArc"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircleArc~GetCustomData.html"
---

# GetCustomData Method (ICircleArc)

Gets the specified custom data for the Arc.

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

[ICircleArc Interface](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html)
[ICircleArc Members](Interop.dsAutomation~Interop.dsAutomation.ICircleArc_members.html)
[ICircleArc::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~DeleteCustomData.html)
[ICircleArc::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~SetCustomData.html)
[ICircleArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ICircleArc~Handle.html)

## Availability

DraftSight V1R1.2
