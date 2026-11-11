---
title: "InsertDoubleData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "InsertDoubleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertDoubleData.html"
---

# InsertDoubleData Method (IXRecord)

Inserts a double and marker at the specified index of the XRecord data element.

## Syntax

### Visual Basic

```vb
Sub InsertDoubleData( _
   ByVal Index As System.Integer, _
   ByVal Marker As System.Integer, _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### JScript

```
function InsertDoubleData(
   Index : System.int,
   Marker : System.int,
   Value : System.double
);
```

### Managed Extensions for C++

```
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### C++/CLI

```cpp
void InsertDoubleData(
   System.int Index,
   System.int Marker,
   System.double Value
)
```

### Parameters

- `Index`: Index of the XRecord data element where to insert the double (see **Remarks**)
- `Marker`: Marker
- `Value`: Double

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDoubleData.html)
[IXRecord::SetDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetDoubleData.html)

## Availability

DraftSight V1R4.0
