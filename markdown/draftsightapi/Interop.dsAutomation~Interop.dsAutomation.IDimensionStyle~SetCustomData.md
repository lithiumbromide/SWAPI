---
title: "SetCustomData Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~SetCustomData.html"
---

# SetCustomData Method (IDimensionStyle)

Sets the custom data for the DimensionStyle.

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

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~DeleteCustomData.html)
[IDimensionStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetCustomData.html)
[IDimensionStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~Handle.html)

## Availability

DraftSight V1R1.2
