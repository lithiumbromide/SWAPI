---
title: "InsertByteData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertByteData.html"
---

# InsertByteData Method (IXRecord)

Inserts a binary array and marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertByteData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal ByteArray As System.Object _
)
```

### C#

```csharp
void InsertByteData(
   System.int Index,
   System.int Marker,
   System.object ByteArray
)
```

### JScript

```
function InsertByteData(
   Index : System.int,
   Marker : System.int,
   ByteArray : System.Object
);
```

### Managed Extensions for C++

```
void InsertByteData(
   System.int Index,
   System.int Marker,
   System.Object* ByteArray
)
```

### C++/CLI

```cpp
void InsertByteData(
   System.int Index,
   System.int Marker,
   System.Object^ ByteArray
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert the binary array and marker (see **Remarks**)
- `Marker`: Marker
- `ByteArray`: Binary array

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetByteData.html)
[IXRecord::SetByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetByteData.html)

## Availability

DraftSight V1R4.0
