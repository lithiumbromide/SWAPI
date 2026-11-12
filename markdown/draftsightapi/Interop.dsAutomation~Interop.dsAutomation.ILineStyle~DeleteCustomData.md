---
title: "DeleteCustomData Method (ILineStyle)"
project: ""
interface: "ILineStyle"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyle~DeleteCustomData.html"
---

# DeleteCustomData Method (ILineStyle)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the simple LineStyle.

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

[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyle Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyle_members.html)
[ILineStyle::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~GetCustomData.html)
[ILineStyle::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~SetCustomData.html)
[ILineStyle::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Handle.html)

## Availability

DraftSight V1R4.0
