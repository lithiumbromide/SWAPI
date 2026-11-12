---
title: "InsertByteData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "InsertByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertByteData.html"
---

# InsertByteData Method (ICustomData)

Inserts the specified custom data element whose data type is a binary array.

## Syntax

### Visual Basic

```vb
Sub InsertByteData( _
   ByVal Index As System.Integer, _
   ByVal ByteArray As System.Object _
)
```

### C#

```csharp
void InsertByteData(
   System.int Index,
   System.object ByteArray
)
```

### JScript

```
function InsertByteData(
   Index : System.int,
   ByteArray : System.Object
);
```

### Managed Extensions for C++

```
void InsertByteData(
   System.int Index,
   System.Object* ByteArray
)
```

### C++/CLI

```cpp
void InsertByteData(
   System.int Index,
   System.Object^ ByteArray
)
```

### Parameters

- `Index`: Index where to insert the custom data
- `ByteArray`: Binary array of doubles (see **Remarks**)

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Binary data is organized into variable-length chunks. The maximum length of each chunk is 127 bytes. If a binary array larger than 127 bytes is passed, then the custom data is not added. If your application requires more than 127 bytes of binary data, then the application must organize the data into multiple chunks.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::GetByteData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetByteData.html)
[ICustomData::SetByteData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetByteData.html)

## Availability

DraftSight V1R1.2
