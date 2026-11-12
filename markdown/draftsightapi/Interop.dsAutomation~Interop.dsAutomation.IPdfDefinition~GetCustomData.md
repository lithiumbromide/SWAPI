---
title: "GetCustomData Method (IPdfDefinition)"
project: ""
interface: "IPdfDefinition"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition~GetCustomData.html"
---

# GetCustomData Method (IPdfDefinition)

Gets the specified custom data for the PDF definition.

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

[IPdfDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition.html)
[IPdfDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IPdfDefinition_members.html)

## Availability

DraftSight 2020 SP0
