---
title: "MenuPinned Property (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "MenuPinned"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~MenuPinned.html"
---

# MenuPinned Property (IFrame)

Gets or sets whether the SOLIDWORKS main menu is pinned.

## Syntax

### Visual Basic (Declaration)

```vb
Property MenuPinned As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Boolean

instance.MenuPinned = value

value = instance.MenuPinned
```

### C#

```csharp
System.bool MenuPinned {get; set;}
```

### C++/CLI

```cpp
property System.bool MenuPinned {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to pin the SOLIDWORKS main menu, false to not

## VBA Syntax

See [Frame::MenuPinned](ms-its:sldworksapivb6.chm::/sldworks~Frame~MenuPinned.html).

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
