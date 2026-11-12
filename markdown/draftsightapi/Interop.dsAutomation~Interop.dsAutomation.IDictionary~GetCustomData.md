---
title: "GetCustomData Method (IDictionary)"
project: ""
interface: "IDictionary"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~GetCustomData.html"
---

# GetCustomData Method (IDictionary)

Gets the specified custom data for the dictionary.

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

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)
[IDictionary::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~DeleteCustomData.html)
[IDictionary::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~SetCustomData.html)
[IDictionary::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IDictionary~Handle.html)

## Availability

DraftSight V1R4.0
