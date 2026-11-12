---
title: "SetCustomData Method (IRegion)"
project: ""
interface: "IRegion"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRegion~SetCustomData.html"
---

# SetCustomData Method (IRegion)

Sets the custom data for the Region.

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

[IRegion Interface](Interop.dsAutomation~Interop.dsAutomation.IRegion.html)
[IRegion Members](Interop.dsAutomation~Interop.dsAutomation.IRegion_members.html)
[IRegion::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~DeleteCustomData.html)
[IRegion::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRegion~GetCustomData.html)
[IRegion::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRegion~Handle.html)

## Availability

DraftSight V1R2.0
