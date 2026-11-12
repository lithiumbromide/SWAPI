---
title: "DeleteCustomData Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~DeleteCustomData.html"
---

# DeleteCustomData Method (IDimensionStyle)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the DimensionStyle.

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

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetCustomData.html)
[IDimensionStyle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~SetCustomData.html)
[IDimensionStyle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~Handle.html)

## Availability

DraftSight V1R1.2
