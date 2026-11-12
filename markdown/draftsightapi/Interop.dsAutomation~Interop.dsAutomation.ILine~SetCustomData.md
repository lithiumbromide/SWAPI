---
title: "SetCustomData Method (ILine)"
project: ""
interface: "ILine"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILine~SetCustomData.html"
---

# SetCustomData Method (ILine)

Sets the custom data for the Line.

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

[ILine Interface](Interop.dsAutomation~Interop.dsAutomation.ILine.html)
[ILine Members](Interop.dsAutomation~Interop.dsAutomation.ILine_members.html)
[ILine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~DeleteCustomData.html)
[ILine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ILine~GetCustomData.html)
[ILine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ILine~Handle.html)

## Availability

DraftSight V1R1.2
