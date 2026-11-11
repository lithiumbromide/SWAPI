---
title: "GetCustomData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html"
---

# GetCustomData Method (IXRecord)

Gets the specified custom data for the XRecord.

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

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html)
[IXRecord::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html)
[IXRecord::GetHandleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html)
[IXRecord::InsertHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html)
[IXRecord::SetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)

## Availability

DraftSight V1R4.0
