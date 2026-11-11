---
title: "InsertInteger32Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertInteger32Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger32Data.html"
---

# InsertInteger32Data Method (IXRecord)

Inserts a signed 32-bit integer, also called Int32, and a marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertInteger32Data( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void InsertInteger32Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### JScript

```
function InsertInteger32Data(
   Index : System.int,
   Marker : System.int,
   Value : System.int
);
```

### Managed Extensions for C++

```
void InsertInteger32Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### C++/CLI

```cpp
void InsertInteger32Data(
   System.int Index,
   System.int Marker,
   System.int Value
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert an Int32 (see **Remarks**)
- `Marker`: Marker
- `Value`: Int32

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger32Data.html)
[IXRecord::SetInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger32Data.html)

## Availability

DraftSight V1R4.0
