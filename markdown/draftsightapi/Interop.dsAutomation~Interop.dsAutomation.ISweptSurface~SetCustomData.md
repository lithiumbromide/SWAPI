---
title: "SetCustomData Method (ISweptSurface)"
project: ""
interface: "ISweptSurface"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~SetCustomData.html"
---

# SetCustomData Method (ISweptSurface)

Sets the custom data for this swept surface.

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

[ISweptSurface Interface](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface.html)
[ISweptSurface Members](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface_members.html)
[ISweptSurface::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~DeleteCustomData.html)
[ISweptSurface::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ISweptSurface~GetCustomData.html)

## Availability

DraftSight 2020 SP0
