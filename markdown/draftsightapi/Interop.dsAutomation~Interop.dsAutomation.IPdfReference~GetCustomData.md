---
title: "GetCustomData Method (IPdfReference)"
project: ""
interface: "IPdfReference"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfReference~GetCustomData.html"
---

# GetCustomData Method (IPdfReference)

Gets the specified custom data for the PDF reference.

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

[IPdfReference Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)
[IPdfReference Members](Interop.dsAutomation~Interop.dsAutomation.IPdfReference_members.html)
[IPdfReference::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~DeleteCustomData.html)
[IPdfReference::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~SetCustomData.html)
[IPdfReference::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IPdfReference~Handle.html)

## Availability

DraftSight 2020 SP0
