---
title: "SetByteData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetByteData.html"
---

# SetByteData Method (IXRecord)

Sets the specified XRecord data element to a binary array.

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

- `Index`: Index of XRecord data element to set to a binary array (see **Remarks**)
- `ByteArray`: Binary array

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetByteData.html)
[IXRecord::InsertByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertByteData.html)

## Availability

DraftSight V1R4.0
