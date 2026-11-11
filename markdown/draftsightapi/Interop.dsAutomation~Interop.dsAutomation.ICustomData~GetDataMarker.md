---
title: "GetDataMarker Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetDataMarker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataMarker.html"
---

# GetDataMarker Method (ICustomData)

Gets the marker for the specified custom data element.

## Syntax

### Visual Basic

```vb
Sub GetDataMarker( _
   ByVal Index As System.Integer, _
   ByRef Marker As System.Integer _
)
```

### C#

```csharp
void GetDataMarker(
   System.int Index,
   out System.int Marker
)
```

### JScript

```
function GetDataMarker(
   Index : System.int,
   Marker : System.int
);
```

### Managed Extensions for C++

```
void GetDataMarker(
   System.int Index,
   [PARAMFLAG::Out] System.int Marker
)
```

### C++/CLI

```cpp
void GetDataMarker(
   System.int Index,
   [Out] System.int Marker
)
```

### Parameters

- `Index`: Index of the custom data element
- `Marker`: [Marker](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html#Marker) for the custom data element

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetDataType Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataType.html)

## Availability

DraftSight V1R1.2
