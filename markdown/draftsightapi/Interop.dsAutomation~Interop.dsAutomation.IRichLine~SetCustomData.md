---
title: "SetCustomData Method (IRichLine)"
project: ""
interface: "IRichLine"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLine~SetCustomData.html"
---

# SetCustomData Method (IRichLine)

Sets the custom data for the RichLine.

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

[IRichLine Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html)
[IRichLine Members](Interop.dsAutomation~Interop.dsAutomation.IRichLine_members.html)
[IRichLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~DeleteCustomData.html)
[IRichLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRichLine~GetCustomData.html)
[IRichLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRichLine~Handle.html)

## Availability

DraftSight V1R1.2
