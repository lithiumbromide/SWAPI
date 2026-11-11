---
title: "InsertStringData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertStringData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertStringData.html"
---

# InsertStringData Method (IXRecord)

Inserts a string and marker at the specified index of the XRecord data element.

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

- `Index`: Index of the XRecord data element where to insert the string (see **Remarks**)
- `Marker`: Marker
- `Value`: String

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetStringData.html)
[IXRecord::SetStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetStringData.html)

## Availability

DraftSight V1R4.0
