---
title: "GetCustomData Method (IRevolve)"
project: ""
interface: "IRevolve"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRevolve~GetCustomData.html"
---

# GetCustomData Method (IRevolve)

Gets the specified custom data for this Revolve.

## Syntax

### Visual Basic

```vb
Function GetCustomData( _
   ByVal ApplicationName As System.String _
) As CustomData
```

### C#

```csharp
CustomData GetCustomData(
   System.string ApplicationName
)
```

### JScript

```
function GetCustomData(
   ApplicationName : System.String
) : CustomData;
```

### Managed Extensions for C++

```
CustomData* GetCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
CustomData^ GetCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

### Return Value

[Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IRevolve Interface](Interop.dsAutomation~Interop.dsAutomation.IRevolve.html)
[IRevolve Members](Interop.dsAutomation~Interop.dsAutomation.IRevolve_members.html)
[IRevolve::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~DeleteCustomData.html)
[IRevolve::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IRevolve~SetCustomData.html)

## Availability

DraftSight 2020 SP0
