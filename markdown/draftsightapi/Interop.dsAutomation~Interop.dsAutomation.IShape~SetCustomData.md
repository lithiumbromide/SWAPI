---
title: "SetCustomData Method (IShape)"
project: ""
interface: "IShape"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IShape~SetCustomData.html"
---

# SetCustomData Method (IShape)

Sets the custom data for the shape.

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

[IShape Interface](Interop.dsAutomation~Interop.dsAutomation.IShape.html)
[IShape Members](Interop.dsAutomation~Interop.dsAutomation.IShape_members.html)
[IShape::GetCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~GetCustomData.html)
[IShape::DeleteCustomData Method ()](Interop.dsAutomation~Interop.dsAutomation.IShape~DeleteCustomData.html)
[IShape::Handle Property ()](Interop.dsAutomation~Interop.dsAutomation.IShape~Handle.html)

## Availability

DraftSight V1R4.0
