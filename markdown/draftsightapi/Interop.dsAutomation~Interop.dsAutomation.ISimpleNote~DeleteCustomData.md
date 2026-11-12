---
title: "DeleteCustomData Method (ISimpleNote)"
project: ""
interface: "ISimpleNote"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~DeleteCustomData.html"
---

# DeleteCustomData Method (ISimpleNote)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the SimpleNote.

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

[ISimpleNote Interface](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote.html)
[ISimpleNote Members](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote_members.html)
[ISimpleNote::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~GetCustomData.html)
[ISimpleNote::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~SetCustomData.html)
[ISimpleNote::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ISimpleNote~Handle.html)

## Availability

DraftSight V1R1.2
