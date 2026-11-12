---
title: "GetCustomData Method (IExtrudedSurface)"
project: ""
interface: "IExtrudedSurface"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~GetCustomData.html"
---

# GetCustomData Method (IExtrudedSurface)

Gets the specified custom data for this extruded surface.

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

[IExtrudedSurface Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface.html)
[IExtrudedSurface Members](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface_members.html)
[IExtrudedSurface::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~DeleteCustomData.html)
[IExtrudedSurface::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrudedSurface~SetCustomData.html)

## Availability

DraftSight 2020 SP0
