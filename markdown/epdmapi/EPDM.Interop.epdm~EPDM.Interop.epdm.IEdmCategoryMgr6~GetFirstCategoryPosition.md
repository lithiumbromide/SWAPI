---
title: "GetFirstCategoryPosition Method (IEdmCategoryMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCategoryMgr6"
member: "GetFirstCategoryPosition"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetFirstCategoryPosition.html"
---

# GetFirstCategoryPosition Method (IEdmCategoryMgr6)

Starts an enumeration of the categories in the vault.

## Syntax

### Visual Basic

```vb
Function GetFirstCategoryPosition() As IEdmPos5
```

### C#

```csharp
IEdmPos5 GetFirstCategoryPosition()
```

### C++/CLI

```cpp
IEdmPos5^ GetFirstCategoryPosition();
```

### Return Value

[IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the first category in the list

## Examples

See the [IEdmCategoryMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6.html) examples.

## Remarks

After calling this method, call [IEdmCategoryMgr6::GetNextCategory](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetNextCategory.html).

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmCategoryMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6.html)
[IEdmCategoryMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
