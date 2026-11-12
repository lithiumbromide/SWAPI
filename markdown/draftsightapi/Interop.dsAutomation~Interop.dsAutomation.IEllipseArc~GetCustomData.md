---
title: "GetCustomData Method (IEllipseArc)"
project: ""
interface: "IEllipseArc"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~GetCustomData.html"
---

# GetCustomData Method (IEllipseArc)

Gets the specified custom data for the Ellipse or an elliptical Arc.

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

[IEllipseArc Interface](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc.html)
[IEllipseArc Members](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc_members.html)
[IEllipseArc::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~DeleteCustomData.html)
[IEllipseArc::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~SetCustomData.html)
[IEllipseArc::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IEllipseArc~Handle.html)

## Availability

DraftSight V1R1.2
