---
title: "SetByteData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "SetByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetByteData.html"
---

# SetByteData Method (ICustomData)

Sets the specified custom data element whose data type is a binary array.

## Syntax

### Visual Basic

```vb
Sub SetByteData( _
   ByVal Index As System.Integer, _
   ByVal ByteArray As System.Object _
)
```

### C#

```csharp
void SetByteData(
   System.int Index,
   System.object ByteArray
)
```

### JScript

```
function SetByteData(
   Index : System.int,
   ByteArray : System.Object
);
```

### Managed Extensions for C++

```
void SetByteData(
   System.int Index,
   System.Object* ByteArray
)
```

### C++/CLI

```cpp
void SetByteData(
   System.int Index,
   System.Object^ ByteArray
)
```

### Parameters

- `Index`: Index of the custom data element
- `ByteArray`: Binary array of doubles

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Binary data for custom data is organized into variable-length chunks. The maximum length of each chunk is 127 bytes. If a binary array larger than 127 bytes is passed, then that data is not added. If an application requires more than 127 bytes of binary data, then the application must organize the data into multiple chunks.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)

## Availability

DraftSight V1R1.2
