---
title: "SetThirdPartyPopupMenuState Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetThirdPartyPopupMenuState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetThirdPartyPopupMenuState.html"
---

# SetThirdPartyPopupMenuState Method (ISldWorks)

Sets whether to show or hide a third-party popup (shortcut) menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetThirdPartyPopupMenuState( _
   ByVal RegisterId As System.Integer, _
   ByVal IsActive As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim IsActive As System.Boolean
Dim value As System.Boolean

value = instance.SetThirdPartyPopupMenuState(RegisterId, IsActive)
```

### C#

```csharp
System.bool SetThirdPartyPopupMenuState(
   System.int RegisterId,
   System.bool IsActive
)
```

### C++/CLI

```cpp
System.bool SetThirdPartyPopupMenuState(
   System.int RegisterId,
   System.bool IsActive
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RegisterId`: ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html)
- `IsActive`: True to show the shortcut menu, false to hide it

### Return Value

True if shortcut menu is shown, false if it is hidden

## Remarks

This method is supported in C++ applications only.

Typical steps in creating and displaying your shortcut menu:

1. [Add menu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenu.html) and [add menu items](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddMenuItem4.html) to the SOLIDWORKS main menu bar for your shortcut menu, or [add an icon to a context-sensitive menu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenuPopupIcon.html) that displays your shortcut menu, or both.
2. [Register](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html) your shortcut menu.
3. [Add](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddItemToThirdPartyPopupMenu.html) your shortcut menu items.
4. [Show](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu.html) your shortcut menu at a specific location in the SOLIDWORKS graphics area, typically from a mouse event handler.
5. [Remove](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveItemFromThirdPartyPopupMenu.html) a menu item from your shortcut menu, if desired.
6. Toggle the visibility of your shortcut menu.
7. [Remove the shortcut menu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveMenu.html) from the SOLIDWORKS main menu bar and [remove the icon from the context-sensitive menu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html), if added.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
