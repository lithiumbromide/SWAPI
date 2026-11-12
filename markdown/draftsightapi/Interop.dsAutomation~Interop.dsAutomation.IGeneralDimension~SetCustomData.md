---
title: "SetCustomData Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~SetCustomData.html"
---

# SetCustomData Method (IGeneralDimension)

Sets the custom data for the Dimension.

## Syntax

### Visual Basic

```vb
Sub SetCustomData( _
   ByVal ApplicationName As System.String, _
   ByVal CustomData As CustomData _
)
```

### C#

```csharp
void SetCustomData(
   System.string ApplicationName,
   CustomData CustomData
)
```

### JScript

```
function SetCustomData(
   ApplicationName : System.String,
   CustomData : CustomData
);
```

### Managed Extensions for C++

```
void SetCustomData(
   System.string* ApplicationName,
   CustomData* CustomData
)
```

### C++/CLI

```cpp
void SetCustomData(
   System.String^ ApplicationName,
   CustomData^ CustomData
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)
- `CustomData`: [Custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~DeleteCustomData.html)
[IGeneralDimension::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetCustomData.html)
[IGeneralDimension::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~Handle.html)

## Availability

DraftSight V1R1.2
