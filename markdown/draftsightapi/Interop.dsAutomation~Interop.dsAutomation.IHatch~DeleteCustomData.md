---
title: "DeleteCustomData Method (IHatch)"
project: ""
interface: "IHatch"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHatch~DeleteCustomData.html"
---

# DeleteCustomData Method (IHatch)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Hatch.

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

[IHatch Interface](Interop.dsAutomation~Interop.dsAutomation.IHatch.html)
[IHatch Members](Interop.dsAutomation~Interop.dsAutomation.IHatch_members.html)
[IHatch::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~GetCustomData.html)
[IHatch::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IHatch~SetCustomData.html)
[IHatch::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IHatch~Handle.html)

## Availability

DraftSight V1R1.3
