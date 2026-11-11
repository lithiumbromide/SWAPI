---
title: "GetDataMarker Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "GetDataMarker"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataMarker.html"
---

# GetDataMarker Method (IXRecord)

Gets the marker for the specified XRecord data element.

## Syntax

### Visual Basic

```vb
Function GetDataMarker( _
   ByVal Index As System.Integer _
) As System.Integer
```

### C#

```csharp
System.int GetDataMarker(
   System.int Index
)
```

### JScript

```
function GetDataMarker(
   Index : System.int
) : System.int;
```

### Managed Extensions for C++

```
System.int GetDataMarker(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetDataMarker(
   System.int Index
)
```

### Parameters

- `Index`: Index of the XRecord data element to get (see **Remarks**)

### Return Value

Marker (see **Remarks**)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

Valid values for Marker range from 1 through 369. See the Remarks section in [IXRecord](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html) for details.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)

## Availability

DraftSight V1R4.0
