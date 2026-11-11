---
title: "GetCustomData Method (IImageDefinition)"
project: ""
interface: "IImageDefinition"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IImageDefinition~GetCustomData.html"
---

# GetCustomData Method (IImageDefinition)

Gets the specified custom data for the raster image definition.

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

[IImageDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition.html)
[IImageDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IImageDefinition_members.html)

## Availability

DraftSight 2020 SP0
