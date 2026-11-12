---
title: "DeleteCustomData Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~DeleteCustomData.html"
---

# DeleteCustomData Method (IArcAlignedText)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the curved text.

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

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetCustomData.html)
[IArcAlignedText::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~SetCustomData.html)
[IArcAlignedText::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~Handle.html)

## Availability

DraftSight 2018 SP2
