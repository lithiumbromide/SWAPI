---
title: "GetCustomData Method (ITrace)"
project: ""
interface: "ITrace"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~GetCustomData.html"
---

# GetCustomData Method (ITrace)

Gets the specified custom data for this Trace.

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

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~DeleteCustomData.html)
[ITrace::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetCustomData.html)
[ITrace::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~Handle.html)

## Availability

DraftSight V1R5.0
