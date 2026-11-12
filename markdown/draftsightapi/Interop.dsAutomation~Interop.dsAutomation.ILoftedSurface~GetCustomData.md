---
title: "GetCustomData Method (ILoftedSurface)"
project: ""
interface: "ILoftedSurface"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~GetCustomData.html"
---

# GetCustomData Method (ILoftedSurface)

Gets the specified custom data for this lofted surface.

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

[ILoftedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface.html)
[ILoftedSurface Members](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface_members.html)
[ILoftedSurface::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~DeleteCustomData.html)
[ILoftedSurface::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILoftedSurface~SetCustomData.html)

## Availability

DraftSight 2020 SP0
