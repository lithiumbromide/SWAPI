---
title: "SetCustomData Method (IRevolve)"
project: ""
interface: "IRevolve"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolve~SetCustomData.html"
---

# SetCustomData Method (IRevolve)

Sets the custom data for this Revolve.

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

[IRevolve Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolve.html)
[IRevolve Members](Interop.dsAutomation~Interop.dsAutomation.IRevolve_members.html)
[IRevolve::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~DeleteCustomData.html)
[IRevolve::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~GetCustomData.html)

## Availability

DraftSight 2020 SP0
