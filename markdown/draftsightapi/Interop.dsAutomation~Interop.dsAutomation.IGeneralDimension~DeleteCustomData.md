---
title: "DeleteCustomData Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~DeleteCustomData.html"
---

# DeleteCustomData Method (IGeneralDimension)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Dimension.

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

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetCustomData.html)
[IGeneralDimension::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~SetCustomData.html)
[IGeneralDimension::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Handle.html)

## Availability

DraftSight V1R1.2
