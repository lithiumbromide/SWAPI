---
title: "GetCustomData Method (IExtrusion)"
project: ""
interface: "IExtrusion"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExtrusion~GetCustomData.html"
---

# GetCustomData Method (IExtrusion)

Gets the specified custom data for this extrusion.

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

[IExtrusion Interface](Interop.dsAutomation~Interop.dsAutomation.IExtrusion.html)
[IExtrusion Members](Interop.dsAutomation~Interop.dsAutomation.IExtrusion_members.html)
[IExtrusion::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~DeleteCustomData.html)
[IExtrusion::SetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IExtrusion~SetCustomData.html)

## Availability

DraftSight 2020 SP0
