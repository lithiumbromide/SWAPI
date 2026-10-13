---
title: "ShowUserPopup Method (IEdmUserMgr8)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmUserMgr8"
member: "ShowUserPopup"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~ShowUserPopup.html"
---

# ShowUserPopup Method (IEdmUserMgr8)

Displays a popup window with information about the specified user when the mouse hovers over the specified area of the specified window.

## Syntax

### Visual Basic

```vb
Sub ShowUserPopup( _
   ByVal hParent As System.Integer, _
   ByRef poTrackRect As EdmRect, _
   ByVal oUserID As System.Object _
)
```

### C#

```csharp
void ShowUserPopup(
   System.int hParent,
   ref EdmRect poTrackRect,
   System.object oUserID
)
```

### C++/CLI

```cpp
void ShowUserPopup(
   System.int hParent,
   EdmRect% poTrackRect,
   System.Object^ oUserID
)
```

### Parameters

- `hParent`: Handle of the parent window
- `poTrackRect`: [EdmRect](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmRect.html) structure; bounding rectangle of the area in the window that will trigger the mouse hover event
- `oUserID`: ID, login name, or full name of the user for which to display information in the popup window (see **Remarks**)

## Examples

See the [IEdmUserMgr8](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html) examples.

## Remarks

In the SOLIDWORKS PDM Professional user interface, whenever the mouse hovers over a user name, a popup window displays information about the user. The popup window displays until the mouse moves off the area containing the user name. Call this method to display a popup window when the mouse hovers over a user name in a Windows form.

If oUserID contains a full name that is not unique, the user to display is randomly selected by the system.

[IEdmUser10::SetUserDataEx](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUser10~SetUserDataEx.html) describes how to update the information displayed in the popup window.

Call [IEdmUserMgr8::CreateUserPicture](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8~CreateUserPicture.html) if you want to display the picture of a user in a Windows form.

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.
- E_INVALIDARG: One or more of the arguments are invalid.
- E_EDM_NOT_LOGGED_IN: You must log in to the vault before calling this method.

## See Also

[IEdmUserMgr8 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8.html)
[IEdmUserMgr8 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmUserMgr8_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
