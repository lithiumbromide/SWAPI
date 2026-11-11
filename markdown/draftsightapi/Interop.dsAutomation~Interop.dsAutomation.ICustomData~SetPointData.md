---
title: "SetPointData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetPointData.html"
---

# SetPointData Method (ICustomData)

Sets the specified custom data element whose value is a point.

## Syntax

### Visual Basic

```vb
Sub SetPointData( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetPointData(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetPointData(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetPointData(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPointData(
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `Index`: Index of the custom data element
- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
**Add, Modify, and Remove Custom Data (VBA)**

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetPointData.html)
[ICustomData::InsertPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertPointData.html)

## Availability

DraftSight V1R1.2
