---
title: "GetButtonImages Method (IEdmMenu5)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmMenu5"
member: "GetButtonImages"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5~GetButtonImages.html"
---

# GetButtonImages Method (IEdmMenu5)

Gets the toolbar-button images of a range of commands.

## Syntax

### Visual Basic

```vb
Sub GetButtonImages( _
   ByVal hDestImageList As System.Integer, _
   ByVal eState As EdmButtonState, _
   ByVal poItemIDArray() As System.Integer _
)
```

### C#

```csharp
void GetButtonImages(
   System.int hDestImageList,
   EdmButtonState eState,
   System.int[] poItemIDArray
)
```

### C++/CLI

```cpp
void GetButtonImages(
   System.int hDestImageList,
   EdmButtonState eState,
   System.array<int>^ poItemIDArray
)
```

### Parameters

- `hDestImageList`: Handle of the image list (HIMAGELIST) to which to add images; the images are appended at the end of the list
- `eState`: State of buttons to get as defined in [EdmButtonState](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmButtonState.html)
- `poItemIDArray`: Array of menu command IDs for which to get images

## Remarks

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: One of the arguments is invalid.

## See Also

[IEdmMenu5 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5.html)
[IEdmMenu5 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu5_members.html)
[IEdmMenu6::GetItems Method ()](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmMenu6~GetItems.html)

## Availability

Version 5.2 of SOLIDWORKS PDM Professional
