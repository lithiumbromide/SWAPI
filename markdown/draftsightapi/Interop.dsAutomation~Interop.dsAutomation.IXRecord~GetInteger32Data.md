---
title: "GetInteger32Data Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetInteger32Data"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetInteger32Data.html"
---

# GetInteger32Data Method (IXRecord)

Gets the specified XRecord data element whose data type is a signed 32-bit integer, also called Int32.

## Syntax

### Visual Basic

```vb
Function GetInteger32Data( _
   ByVal Index As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetInteger32Data(
   System.int Index
)
```

### JScript

```
function GetInteger32Data(
   Index : System.int
) : System.int;
```

### Managed Extensions for C++

```
System.int GetInteger32Data(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetInteger32Data(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

Int32

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertInteger32Data.html)
[IXRecord::SetInteger32Data Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetInteger32Data.html)

## Availability

DraftSight V1R4.0
