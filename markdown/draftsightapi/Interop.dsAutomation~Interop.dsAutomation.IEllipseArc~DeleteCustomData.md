---
title: "DeleteCustomData Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~DeleteCustomData.html"
---

# DeleteCustomData Method (IEllipseArc)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Ellipse or an elliptical Arc.

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

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetCustomData.html)
[IEllipseArc::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~SetCustomData.html)
[IEllipseArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Handle.html)

## Availability

DraftSight V1R1.2
