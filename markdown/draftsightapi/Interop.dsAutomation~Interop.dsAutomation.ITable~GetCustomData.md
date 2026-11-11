---
title: "GetCustomData Method (ITable)"
project: ""
interface: "ITable"
member: "GetCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetCustomData.html"
---

# GetCustomData Method (ITable)

Gets the specified custom data for the Table.

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

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::DeleteCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteCustomData.html)
[ITable::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ITable~SetCustomData.html)
[ITable::Handle Property](Interop.dsAutomation~Interop.dsAutomation.ITable~Handle.html)

## Availability

DraftSight V1R3.0
