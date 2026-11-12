---
title: "Rollback Method (IEdmSerNoValue)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSerNoValue"
member: "Rollback"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoValue~Rollback.html"
---

# Rollback Method (IEdmSerNoValue)

Returns the allocated serial number to the serial number generator, so it can be allocated in the future.

## Syntax

### Visual Basic

```vb
Sub Rollback()
```

### C#

```csharp
void Rollback()
```

### C++/CLI

```cpp
void Rollback();
```

## Remarks

This method allows you to return generated numbers that you can not use. This helps to avoid gaps between serial numbers.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSerNoValue Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoValue.html)
[IEdmSerNoValue Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSerNoValue_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.4
