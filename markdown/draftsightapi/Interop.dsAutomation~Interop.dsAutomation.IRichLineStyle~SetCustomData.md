---
title: "SetCustomData Method (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~SetCustomData.html"
---

# SetCustomData Method (IRichLineStyle)

Sets the custom data for the RichLineStyle.

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

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~DeleteCustomData.html)
[IRichLineStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~GetCustomData.html)
[IRichLineStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~Handle.html)

## Availability

DraftSight V1R1.2
