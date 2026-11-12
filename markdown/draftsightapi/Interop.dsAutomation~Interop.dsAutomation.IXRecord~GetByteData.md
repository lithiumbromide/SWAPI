---
title: "GetByteData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetByteData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetByteData.html"
---

# GetByteData Method (IXRecord)

Gets the specified XRecord data element whose data type is a binary array.

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

- `Index`: Index of the XRecord data element to get (see **Remarks**)

### Return Value

Binary array

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::InsertByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertByteData.html)
[IXRecord::SetByteData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetByteData.html)

## Availability

DraftSight V1R4.0
