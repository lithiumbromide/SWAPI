---
title: "GetCustomData Method (IHatch)"
project: ""
interface: "IHatch"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~GetCustomData.html"
---

# GetCustomData Method (IHatch)

Gets the specified custom data for the Hatch.

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

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~SetCustomData.html)
[IHatch::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~DeleteCustomData.html)
[IHatch::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IHatch~Handle.html)

## Availability

DraftSight V1R1.3
