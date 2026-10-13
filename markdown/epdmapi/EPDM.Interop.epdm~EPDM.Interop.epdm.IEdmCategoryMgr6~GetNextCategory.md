---
title: "GetNextCategory Method (IEdmCategoryMgr6)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmCategoryMgr6"
member: "GetNextCategory"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetNextCategory.html"
---

# GetNextCategory Method (IEdmCategoryMgr6)

Gets the next category in the enumeration.

## Syntax

### Visual Basic

```vb
Function GetNextCategory( _
   ByVal poPos As IEdmPos5 _
) As IEdmCategory6
```

### C#

```csharp
IEdmCategory6 GetNextCategory(
   IEdmPos5 poPos
)
```

### C++/CLI

```cpp
IEdmCategory6^ GetNextCategory(
   IEdmPos5^ poPos
)
```

### Parameters

- `poPos`: [IEdmPos5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5.html); position of the next category in the list

### Return Value

[IEdmCategory6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategory6.html)

## Examples

See the [IEdmCategoryMgr6](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6.html) examples.

## Remarks

To obtain the position of the first category in the list, call [IEdmCategoryMgr6::GetFirstCategoryPosition](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6~GetFirstCategoryPosition.html).

After calling this method the first time, poPos is automatically incremented every time it is called. Call this method repeatedly to obtain the rest of the categories.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- E_EDM_END_OF_LIST: No more categories can be accessed.

## See Also

[IEdmCategoryMgr6 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6.html)
[IEdmCategoryMgr6 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCategoryMgr6_members.html)

## Availability

SOLIDWORKS PDM Professional Version 6.0
