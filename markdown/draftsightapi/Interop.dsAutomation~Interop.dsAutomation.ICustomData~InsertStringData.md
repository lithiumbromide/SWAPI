---
title: "InsertStringData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertStringData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertStringData.html"
---

# InsertStringData Method (ICustomData)

Inserts a string and a marker at the specified index.

## Syntax

### Visual Basic

```vb
Sub InsertStringData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void InsertStringData(
   System.int Index,
   System.int Marker,
   System.string Value
)
```

### JScript

```
function InsertStringData(
   Index : System.int,
   Marker : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void InsertStringData(
   System.int Index,
   System.int Marker,
   System.string* Value
)
```

### C++/CLI

```cpp
void InsertStringData(
   System.int Index,
   System.int Marker,
   System.String^ Value
)
```

### Parameters

- `Index`: Index where to insert custom data
- `Marker`: [Marker](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html#Marker) for the custom data element
- `Value`: String

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
[ICustomData::GetStringData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetStringData.html)
[ICustomData::SetStringData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetStringData.html)

## Availability

DraftSight V1R1.2
