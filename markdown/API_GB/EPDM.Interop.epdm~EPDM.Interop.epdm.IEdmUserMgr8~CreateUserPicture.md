---
title: "CreateUserPicture Method (IEdmUserMgr8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr8"
member: "CreateUserPicture"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~CreateUserPicture.html"
---

# CreateUserPicture Method (IEdmUserMgr8)

Creates a picture of the user to display in a form.

## Syntax

### Visual Basic

```vb
Function CreateUserPicture( _
   ByVal hParent As System.Integer, _
   ByRef poDestRect As EdmRect, _
   ByVal oUserID As System.Object, _
   Optional ByVal poCallback As EdmCallback, _
   Optional ByVal lEdmUserPictureFlags As System.Integer _
) As IEdmImage
```

### C#

```csharp
IEdmImage CreateUserPicture(
   System.int hParent,
   ref EdmRect poDestRect,
   System.object oUserID,
   EdmCallback poCallback,
   System.int lEdmUserPictureFlags
)
```

### C++/CLI

```cpp
IEdmImage^ CreateUserPicture(
   System.int hParent,
   EdmRect% poDestRect,
   System.Object^ oUserID,
   EdmCallback^ poCallback,
   System.int lEdmUserPictureFlags
)
```

### Parameters

- `hParent`: Handle of parent window on which the picture should be drawn
- `poDestRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; bounding rectangle in which the picture should be drawn (see **Remarks**)
- `oUserID`: ID or login name of the user for which to create a picture
- `poCallback`: Optional pointer to a class that implements [IEdmCallback](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCallback.html) to receive progress information if the picture needs to be downloaded from an archive server
- `lEdmUserPictureFlags`: Combination of [EdmUserPictureFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserPictureFlag.html) bits

### Return Value

[IEdmImage](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmImage.html)

## Examples

See the [IEdmUserMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html) examples.

## Remarks

Call [IEdmUserMgr8::ShowUserPopup](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~ShowUserPopup.html) to display a popup window with user information.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmUserMgr8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html)
[IEdmUserMgr8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
