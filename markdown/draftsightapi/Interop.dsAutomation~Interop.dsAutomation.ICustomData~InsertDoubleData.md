---
title: "InsertDoubleData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertDoubleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertDoubleData.html"
---

# InsertDoubleData Method (ICustomData)

Inserts a double value and a marker at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertDoubleData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### JScript

```
function InsertDoubleData(
   Index : System.int,
   Marker : System.int,
   Value : System.double
);
```

### Managed Extensions for C++

```
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### C++/CLI

```cpp
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### Parameters

- `Index`: Index where to insert the custom data
- `Marker`: [Marker](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html#Marker) for the custom data element
- `Value`: Double value

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
[ICustomData::GetDoubleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDoubleData.html)
[ICustomData::SetDoubleData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetDoubleData.html)

## Availability

DraftSight V1R1.2
