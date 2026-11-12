---
title: "GetByteData Method (ICustomData)"
project: ""
interface: "ICustomData"
member: "GetByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetByteData.html"
---

# GetByteData Method (ICustomData)

Gets the specified custom data element whose data type is a binary array.

## Syntax

### Visual Basic

```vb
Function GetByteData( _
   ByVal Index As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetByteData(
   System.int Index
)
```

### JScript

```
function GetByteData(
   Index : System.int
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetByteData(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetByteData(
   System.int Index
)
```

### Parameters

- `Index`: Index of the custom data element

### Return Value

Binary array (see **Remarks**)

## Examples

[Add, Modify, and Remove Custom Data (C#)](Add_Modify_Remove_Custom_Data_Example_CSharp.htm)
[Add, Modify, and Remove Custom Data (VB.NET)](Add_Modify_Remove_Custom_Data_Example_VBNET.htm)
[Add, Modify, and Remove Custom Data (VBA)](Add_Modify_Remove_Custom_Data_Example_VBA.htm)
[Add and Modify Custom Data (JavaScript)](Add_and_Modify_Custom_Data_Example_JS.htm)

## Remarks

Binary data for custom data is organized into variable-length chunks. The maximum length of each chunk is 127 bytes. If a binary array larger than 127 bytes was passed, then that data was not added. If an application requires more than 127 bytes of binary data, then the application must organize the data into multiple chunks.

Call [ICustomData::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.ICustomData~GetDataCount.html) before calling this method to determine a valid value for Index.

## See Also

[ICustomData Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomData.html)
[ICustomData Members](Interop.dsAutomation~Interop.dsAutomation.ICustomData_members.html)
[ICustomData::InsertByteData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~InsertByteData.html)
[ICustomData::SetByteData Method](Interop.dsAutomation~Interop.dsAutomation.ICustomData~SetByteData.html)

## Availability

DraftSight V1R1.2
