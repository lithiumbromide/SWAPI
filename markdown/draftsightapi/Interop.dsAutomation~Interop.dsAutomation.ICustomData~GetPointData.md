---
title: "GetPointData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetPointData.html"
---

# GetPointData Method (ICustomData)

Gets the specified custom data element whose value is a point.

## Syntax

### Visual Basic

```vb
Sub GetPointData( _
   ByVal Index As System.Integer, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPointData(
   System.int Index,
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPointData(
   Index : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPointData(
   System.int Index,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPointData(
   System.int Index,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
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
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::SetPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetPointData.html)
[ICustomData::InsertPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertPointData.html)

## Availability

DraftSight V1R1.2
