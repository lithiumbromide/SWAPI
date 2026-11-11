---
title: "Delete Method (IXRecord)"
project: ""
interface: "IXRecord"
member: "Delete"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~Delete.html"
---

# Delete Method (IXRecord)

Deletes the specified XRecord data element.

## Syntax

### Visual Basic

```vb
Sub Delete( _
   ByVal Index As System.Integer _
)
```

### C#

```csharp
void Delete(
   System.int Index
)
```

### JScript

```
function Delete(
   Index : System.int
);
```

### Managed Extensions for C++

```
void Delete(
   System.int Index
)
```

### C++/CLI

```cpp
void Delete(
   System.int Index
)
```

### Parameters

- `Index`: Index of the XRecord data element to delete (see **Remarks**)

## Remarks

Before calling this method, call [IXRecord::GetDataCount](Interop.dsAutomation~Interop.dsAutomation.IXRecord~GetDataCount.html) to determine a valid value for Index.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)
[IXRecord::Empty Method ()](Interop.dsAutomation~Interop.dsAutomation.IXRecord~Empty.html)

## Availability

DraftSight V1R4.0
