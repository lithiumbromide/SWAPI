---
title: "GetStatus Method (IEdmBatchUnlock2)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBatchUnlock2"
member: "GetStatus"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2~GetStatus.html"
---

# GetStatus Method (IEdmBatchUnlock2)

Gets the specified statuses for this unlock operation.

## Syntax

### Visual Basic

```vb
Function GetStatus( _
   ByVal lEdmUnlockStatusFlag As System.Integer _
) As System.Object
```

### C#

```csharp
System.object GetStatus(
   System.int lEdmUnlockStatusFlag
)
```

### C++/CLI

```cpp
System.Object^ GetStatus(
   System.int lEdmUnlockStatusFlag
)
```

### Parameters

- `lEdmUnlockStatusFlag`: Combination of [EdmUnlockStatusFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUnlockStatusFlag.html) bits

### Return Value

Array of statuses

## Examples

See the [IEdmBatchUnlock](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBatchUnlock2 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2.html)
[IEdmBatchUnlock2 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBatchUnlock2_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
