---
title: "GetCustomData Method (IViewport)"
project: ""
interface: "IViewport"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~GetCustomData.html"
---

# GetCustomData Method (IViewport)

Gets the specified custom data for the Viewport.

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

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)
[IViewport::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IViewport~DeleteCustomData.html)
[IViewport::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IViewport~SetCustomData.html)
[IViewport::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IViewport~Handle.html)

## Availability

DraftSight V1R3.0
