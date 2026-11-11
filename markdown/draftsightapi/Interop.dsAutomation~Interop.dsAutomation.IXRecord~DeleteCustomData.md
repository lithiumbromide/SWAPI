---
title: "DeleteCustomData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~DeleteCustomData.html"
---

# DeleteCustomData Method (IXRecord)

Deletes the specified custom data from the XRecord.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetCustomData.html)
[IXRecord::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetCustomData.html)
[IXRecord::GetHandleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetHandleData.html)
[IXRecord::InsertHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertHandle.html)
[IXRecord::SetHandle Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetHandle.html)
[IXRecord::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Handle.html)

## Availability

V1R4.0
