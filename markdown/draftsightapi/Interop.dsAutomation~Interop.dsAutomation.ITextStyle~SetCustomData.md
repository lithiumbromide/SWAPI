---
title: "SetCustomData Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~SetCustomData.html"
---

# SetCustomData Method (ITextStyle)

Sets the custom data for the TextStyle.

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

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~DeleteCustomData.html)
[ITextStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~GetCustomData.html)
[ITextStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Handle.html)

## Availability

DraftSight V1R1.2
