---
title: "DeleteCustomData Method (IRay)"
project: ""
interface: "IRay"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRay~DeleteCustomData.html"
---

# DeleteCustomData Method (IRay)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Ray.

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

[IRay Interface](Interop.dsAutomation~Interop.dsAutomation.IRay.html)
[IRay Members](Interop.dsAutomation~Interop.dsAutomation.IRay_members.html)
[IRay::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~GetCustomData.html)
[IRay::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IRay~SetCustomData.html)
[IRay::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IRay~Handle.html)

## Availability

DraftSight V1R1.2
