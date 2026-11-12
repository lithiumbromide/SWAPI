---
title: "IsLocked Method (IEdmBomCell)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmBomCell"
member: "IsLocked"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell~IsLocked.html"
---

# IsLocked Method (IEdmBomCell)

Gets whether the file associated with this BOM cell is checked out and can be edited.

## Syntax

### Visual Basic

```vb
Function IsLocked() As System.Boolean
```

### C#

```csharp
System.bool IsLocked()
```

### C++/CLI

```cpp
System.bool IsLocked();
```

### Return Value

True if the file associated with this BOM cell is available for editing, false if not

## Examples

See the [IEdmBomCell](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html) examples.

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmBomCell Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell.html)
[IEdmBomCell Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmBomCell_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
