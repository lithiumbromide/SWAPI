---
title: "GetStringData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetStringData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetStringData.html"
---

# GetStringData Method (IXRecord)

Gets the specified XRecord data element whose data type is a string.

## Syntax

### Visual Basic

```vb
Function GetStringData( _
   ByVal Index As System.Integer _
) As System.String
```

### C#

```csharp
System.string GetStringData(
   System.int Index
)
```

### JScript

```
function GetStringData(
   Index : System.int
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetStringData(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetStringData(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

String

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertStringData.html)
[IXRecord::SetStringData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetStringData.html)

## Availability

DraftSight V1R4.0
