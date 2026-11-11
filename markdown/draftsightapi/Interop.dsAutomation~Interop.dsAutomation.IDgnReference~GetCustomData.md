---
title: "GetCustomData Method (IDgnReference)"
project: ""
interface: "IDgnReference"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDgnReference~GetCustomData.html"
---

# GetCustomData Method (IDgnReference)

Gets the specified custom data for the DGN reference.

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

[IDgnReference Interface](Interop.dsAutomation~Interop.dsAutomation.IDgnReference.html)
[IDgnReference Members](Interop.dsAutomation~Interop.dsAutomation.IDgnReference_members.html)
[IDgnReference::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~DeleteCustomData.html)
[IDgnReference::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~SetCustomData.html)
[IDgnReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDgnReference~Handle.html)

## Availability

DraftSight 2020 SP0
