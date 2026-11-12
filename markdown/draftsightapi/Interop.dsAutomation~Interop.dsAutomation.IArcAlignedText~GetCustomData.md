---
title: "GetCustomData Method (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~GetCustomData.html"
---

# GetCustomData Method (IArcAlignedText)

Gets the specified custom data for this curved text.

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

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)
[IArcAlignedText::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~DeleteCustomData.html)
[IArcAlignedText::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~SetCustomData.html)
[IArcAlignedText::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~Handle.html)

## Availability

DraftSight 2018 SP2
