---
title: "GetCustomData Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetCustomData.html"
---

# GetCustomData Method (ISimpleNote)

Gets the specified custom data for the SimpleNote.

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

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~DeleteCustomData.html)
[ISimpleNote::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetCustomData.html)
[ISimpleNote::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Handle.html)

## Availability

DraftSight V1R1.2
