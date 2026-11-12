---
title: "Result Property (IEdmFindUser)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: "Result"
kind: "property"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~Result.html"
---

# Result Property (IEdmFindUser)

Gets the result of the last search for users.

## Syntax

### Visual Basic

```vb
ReadOnly Property Result As IEdmEnum
```

### C#

```csharp
IEdmEnum Result {get;}
```

### C++/CLI

```cpp
property IEdmEnum^ Result {
   IEdmEnum^ get();
}
```

### Property Value

[IEdmEnum](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnum.html) (see Remarks)

## Examples

See the [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html) examples.

## Remarks

If [IEdmFindUser::ShowFindUI](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~ShowFindUI.html) is called, this property contains only the users that were selected in the search dialog box's result list.

## See Also

[IEdmFindUser Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
