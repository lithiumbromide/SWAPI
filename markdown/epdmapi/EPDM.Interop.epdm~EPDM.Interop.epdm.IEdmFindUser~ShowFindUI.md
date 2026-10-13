---
title: "ShowFindUI Method (IEdmFindUser)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmFindUser"
member: "ShowFindUI"
kind: "method"
source: "epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~ShowFindUI.html"
---

# ShowFindUI Method (IEdmFindUser)

Displays the Find User dialog box so the user can enter search criteria and select users from the result list.

## Syntax

### Visual Basic

```vb
Function ShowFindUI( _
   ByVal lParentWnd As System.Integer, _
   ByVal bAllowMultiSelect As System.Boolean, _
   Optional ByVal bsCaption As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ShowFindUI(
   System.int lParentWnd,
   System.bool bAllowMultiSelect,
   System.string bsCaption
)
```

### C++/CLI

```cpp
System.bool ShowFindUI(
   System.int lParentWnd,
   System.bool bAllowMultiSelect,
   System.String^ bsCaption
)
```

### Parameters

- `lParentWnd`: Parent window handle of the search dialog box
- `bAllowMultiSelect`: True to permit the user to select more than one user in the search result, false to not
- `bsCaption`: Caption for the dialog box; "" to use the default, localized caption

### Return Value

True if a user is selected in the search result, false if the dialog box is canceled

## Examples

See the [IEdmFindUser](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html) examples.

## Remarks

Before calling this method, call [IEdmFindUser::SetPropt](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~SetPropt.html) to set the search criteria for finding users. The search criteria become the default values in the Find User dialog box that is launched when this method is called.

After successfully calling this method, the [IEdmFindUser.Result](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser~Result.html) property contains the users selected in the result list of the Find User dialog box.

SOLIDWORKS PDM Professional calls this function when you link a card button to the Find User command.

[Return codes](ReturnCodes.htm):

- S_OK: The method successfully executed.
- S_FALSE: An argument is invalid.

## See Also

[IEdmFindUser Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser.html)
[IEdmFindUser Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFindUser_members.html)

## Availability

SOLIDWORKS PDM Professional 2013
