---
title: "SetCustomData Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetCustomData.html"
---

# SetCustomData Method (IPdfReference)

Sets the custom data for this PDF reference.

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

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~DeleteCustomData.html)
[IPdfReference::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetCustomData.html)
[IPdfReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Handle.html)

## Availability

DraftSight 2020 SP0
