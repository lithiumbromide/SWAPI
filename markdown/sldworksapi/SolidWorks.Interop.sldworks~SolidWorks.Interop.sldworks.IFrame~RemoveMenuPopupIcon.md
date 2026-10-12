---
title: "RemoveMenuPopupIcon Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "RemoveMenuPopupIcon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenuPopupIcon.html"
---

# RemoveMenuPopupIcon Method (IFrame)

Removes an icon from a context-sensitive shortcut (popup) menu.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMenuPopupIcon( _
   ByVal Index As System.Integer, _
   ByVal DocType As System.Integer, _
   ByVal SelectType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim Index As System.Integer
Dim DocType As System.Integer
Dim SelectType As System.Integer
Dim value As System.Boolean

value = instance.RemoveMenuPopupIcon(Index, DocType, SelectType)
```

### C#

```csharp
System.bool RemoveMenuPopupIcon(
   System.int Index,
   System.int DocType,
   System.int SelectType
)
```

### C++/CLI

```cpp
System.bool RemoveMenuPopupIcon(
   System.int Index,
   System.int DocType,
   System.int SelectType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index value of the context-sensitive menu icon; index is 1-based
- `DocType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `SelectType`: [Selection type](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) from which to remove the context-sensitive menu icon

### Return Value

True if the icon is removed from the context-sensitive menu, false if not

## Remarks

This method is supported in C++ applications only.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenuPopupIcon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupIcon.html)
[IFrame::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem2.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::GetMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetMenu.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::IGetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
