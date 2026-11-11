---
title: "DeleteCustomData Method (IViewport)"
project: ""
interface: "IViewport"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~DeleteCustomData.html"
---

# DeleteCustomData Method (IViewport)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Viewport.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)
[IViewport::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetCustomData.html)
[IViewport::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IViewport~SetCustomData.html)
[IViewport::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IViewport~Handle.html)

## Availability

DraftSight V1R3.0
