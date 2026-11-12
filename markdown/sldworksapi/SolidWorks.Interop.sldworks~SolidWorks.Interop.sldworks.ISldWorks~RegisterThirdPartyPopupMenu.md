---
title: "RegisterThirdPartyPopupMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RegisterThirdPartyPopupMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.html"
---

# RegisterThirdPartyPopupMenu Method (ISldWorks)

Registers a third-party pop-up (shortcut) menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function RegisterThirdPartyPopupMenu() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Integer

value = instance.RegisterThirdPartyPopupMenu()
```

### C#

```csharp
System.int RegisterThirdPartyPopupMenu()
```

### C++/CLI

```cpp
System.int RegisterThirdPartyPopupMenu();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID of this third-party shortcut menu

## Examples

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

## Remarks

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
