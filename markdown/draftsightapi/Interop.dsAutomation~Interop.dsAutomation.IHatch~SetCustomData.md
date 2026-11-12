---
title: "SetCustomData Method (IHatch)"
project: ""
interface: "IHatch"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~SetCustomData.html"
---

# SetCustomData Method (IHatch)

Sets the custom data for the Hatch.

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

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~DeleteCustomData.html)
[IHatch::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetCustomData.html)
[IHatch::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IHatch~Handle.html)

## Availability

DraftSight V1R1.3
