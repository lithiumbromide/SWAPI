---
title: "SetCustomData Method (IPolyLine)"
project: ""
interface: "IPolyLine"
member: "SetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPolyLine~SetCustomData.html"
---

# SetCustomData Method (IPolyLine)

Sets the custom data for the 2D PolyLine.

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

[IPolyLine Interface](Interop.dsAutomation~Interop.dsAutomation.IPolyLine.html)
[IPolyLine Members](Interop.dsAutomation~Interop.dsAutomation.IPolyLine_members.html)
[IPolyLine::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~DeleteCustomData.html)
[IPolyLine::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~GetCustomData.html)
[IPolyLine::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IPolyLine~Handle.html)

## Availability

DraftSight V1R1.2
