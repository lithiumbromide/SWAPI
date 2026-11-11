---
title: "GetDataType Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetDataType"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataType.html"
---

# GetDataType Method (IXRecord)

Gets the data type of the specified XRecord data element.

## Syntax

### Visual Basic

```vb
Function GetDataType( _
   ByVal Index As System.Integer _
) As dsCustomDataType_e
```

### C#

```csharp
dsCustomDataType_e GetDataType(
   System.int Index
)
```

### JScript

```
function GetDataType(
   Index : System.int
) : dsCustomDataType_e;
```

### Managed Extensions for C++

```
dsCustomDataType_e GetDataType(
   System.int Index
)
```

### C++/CLI

```cpp
dsCustomDataType_e GetDataType(
   System.int Index
)
```

### Parameters

- `Index`: Index of the XRecord data element whose data type to get (see **Remarks**)

### Return Value

Data type as defined in [dsCustomDataType_e](Interop.dsAutomation~Interop.dsAutomation.dsCustomDataType_e.html)

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Data types correspond to custom data types.

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)

## Availability

DraftSight V1R4.0
