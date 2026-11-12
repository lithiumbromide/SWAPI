---
title: "SetCustomData Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~SetCustomData.html"
---

# SetCustomData Method (IArcAlignedText)

Sets the custom data for this curved text.

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

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~DeleteCustomData.html)
[IArcAlignedText::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetCustomData.html)
[IArcAlignedText::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~Handle.html)

## Availability

DraftSight 2018 SP2
