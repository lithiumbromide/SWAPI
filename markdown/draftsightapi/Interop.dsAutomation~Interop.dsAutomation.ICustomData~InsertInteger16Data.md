---
title: "InsertInteger16Data Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertInteger16Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertInteger16Data.html"
---

# InsertInteger16Data Method (ICustomData)

Inserts a signed 16-bit integer, also called Int16, and a marker at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertInteger16Data( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### JScript

```
function InsertInteger16Data(
   Index : System.int,
   Marker : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### C++/CLI

```cpp
void InsertInteger16Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### Parameters

- `Index`: Index where to insert custom data
- `Marker`: [Marker](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html#Marker) for the custom data element
- `Value`: Int16 value

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
[ICustomData::GetInteger16Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetInteger16Data.html)
[ICustomData::SetInteger16Data Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetInteger16Data.html)

## Availability

DraftSight V1R1.2
