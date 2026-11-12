---
title: "DeleteCustomData Method (ICircle)"
project: ""
interface: "ICircle"
member: "DeleteCustomData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICircle~DeleteCustomData.html"
---

# DeleteCustomData Method (ICircle)

Deletes the specified [custom data](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html) from the Circle.

## Syntax

### Visual Basic

```vb
Sub DeleteCustomData( _
   ByVal ApplicationName As System.String _
)
```

### C#

```csharp
void DeleteCustomData(
   System.string ApplicationName
)
```

### JScript

```
function DeleteCustomData(
   ApplicationName : System.String
);
```

### Managed Extensions for C++

```
void DeleteCustomData(
   System.string* ApplicationName
)
```

### C++/CLI

```cpp
void DeleteCustomData(
   System.String^ ApplicationName
)
```

### Parameters

- `ApplicationName`: Name of the custom data's registered application (see **Remarks**)

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## Remarks

Call [IDocument::GetRegisteredApplications](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetRegisteredApplications.html) to find out the names of the document's existing custom data.

## See Also

[ICircle Interface](Interop.dsAutomation~Interop.dsAutomation.ICircle.html)
[ICircle Members](Interop.dsAutomation~Interop.dsAutomation.ICircle_members.html)
[ICircle::GetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~GetCustomData.html)
[ICircle::SetCustomData Method](Interop.dsAutomation~Interop.dsAutomation.ICircle~SetCustomData.html)
[ICircle::Handle Property](Interop.dsAutomation~Interop.dsAutomation.IBlockInstance~Handle.html)

## Availability

DraftSight V1R1.2
