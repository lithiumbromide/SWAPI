---
title: "SetCustomData Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~SetCustomData.html"
---

# SetCustomData Method (IEllipseArc)

Sets the custom data for the Ellipse or an elliptical Arc.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~DeleteCustomData.html)
[IEllipseArc::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetCustomData.html)
[IEllipseArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Handle.html)

## Availability

DraftSight V1R1.2
