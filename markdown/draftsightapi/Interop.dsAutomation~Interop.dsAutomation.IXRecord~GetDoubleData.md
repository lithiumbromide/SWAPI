---
title: "GetDoubleData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetDoubleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDoubleData.html"
---

# GetDoubleData Method (IXRecord)

Gets the specified XRecord data element whose data type is a double.

## Syntax

### Visual Basic

```vb
Function GetDoubleData( _
   ByVal Index As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetDoubleData(
   System.int Index
)
```

### JScript

```
function GetDoubleData(
   Index : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetDoubleData(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetDoubleData(
   System.int Index
)
```

### Parameters

- `Index`: Index of XRecord data element to get (see **Remarks**)

### Return Value

Double

## Examples

[Create and Remove Dictionaries (C#)](Create_and_Remove_Dictionaries_Example_CSharp.htm)
[Create and Remove Dictionaries (VB.NET)](Create_and_Remove_Dictionaries_Example_VBNET.htm)
[Create and Remove Dictionaries (VBA)](Create_and_Remove_Dictionaries_Example_VBA.htm)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertDoubleData.html)
[IXRecord::SetDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetDoubleData.html)

## Availability

DraftSight V1R4.0
