---
title: "SetDoubleData Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "SetDoubleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~SetDoubleData.html"
---

# SetDoubleData Method (IXRecord)

Sets the specified XRecord data element to a double.

## Syntax

### Visual Basic

```vb
Sub SetDoubleData( _
   ByVal Index As System.Integer, _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### JScript

```
function SetDoubleData(
   Index : System.int,
   Value : System.double
);
```

### Managed Extensions for C++

```
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### C++/CLI

```cpp
void SetDoubleData(
   System.int Index,
   System.double Value
)
```

### Parameters

- `Index`: Index of XRecord data type to set to a double (see **Remarks**)
- `Value`: Double

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::GetDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDoubleData.html)
[IXRecord::InsertDoubleData Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~InsertDoubleData.html)

## Availability

DraftSight V1R4.0
