---
title: "SetCustomData Method (IRay)"
project: ""
interface: "IRay"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~SetCustomData.html"
---

# SetCustomData Method (IRay)

Sets the custom data for the Ray.

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

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~DeleteCustomData.html)
[IRay::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetCustomData.html)
[IRay::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRay~Handle.html)

## Availability

DraftSight V1R1.2
