---
title: "SetCustomData Method (ILineStyle)"
project: ""
interface: "ILineStyle"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyle~SetCustomData.html"
---

# SetCustomData Method (ILineStyle)

Sets the custom data for the simple LineStyle.

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

[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyle Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyle_members.html)
[ILineStyle::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~DeleteCustomData.html)
[ILineStyle::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~GetCustomData.html)
[ILineStyle::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Handle.html)

## Availability

DraftSight V1R4.0
