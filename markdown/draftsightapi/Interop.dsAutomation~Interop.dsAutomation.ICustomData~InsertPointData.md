---
title: "InsertPointData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertPointData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertPointData.html"
---

# InsertPointData Method (ICustomData)

Inserts a point and a marker at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertPointData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void InsertPointData(
   System.int Index,
   System.int Marker,
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function InsertPointData(
   Index : System.int,
   Marker : System.int,
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void InsertPointData(
   System.int Index,
   System.int Marker,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void InsertPointData(
   System.int Index,
   System.int Marker,
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `Index`: Index where to insert custom data
- `Marker`: [Marker](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html#Marker) for the custom data element
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
[ICustomData::GetPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetPointData.html)
[ICustomData::SetPointData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetPointData.html)

## Availability

DraftSight V1R1.2
