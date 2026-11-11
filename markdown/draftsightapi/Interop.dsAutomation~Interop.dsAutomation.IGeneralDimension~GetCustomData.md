---
title: "GetCustomData Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetCustomData.html"
---

# GetCustomData Method (IGeneralDimension)

Gets the specified custom data for the Dimension.

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

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~DeleteCustomData.html)
[IGeneralDimension::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~SetCustomData.html)
[IGeneralDimension::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Handle.html)

## Availability

DraftSight V1R1.2
