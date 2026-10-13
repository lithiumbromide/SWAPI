---
title: "GetSubMenus Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetSubMenus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html"
---

# GetSubMenus Method (IFrame)

Gets the submenus for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubMenus( _
   ByVal DocType As System.Integer, _
   ByVal FullMenuName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim DocType As System.Integer
Dim FullMenuName As System.String
Dim value As System.Object

value = instance.GetSubMenus(DocType, FullMenuName)
```

### C#

```csharp
System.object GetSubMenus(
   System.int DocType,
   System.string FullMenuName
)
```

### C++/CLI

```cpp
System.Object^ GetSubMenus(
   System.int DocType,
   System.String^ FullMenuName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Type of document as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `FullMenuName`: Full name of menu

### Return Value

Pointer to an array of the names of the submenus

## VBA Syntax

See [Frame::GetSubMenus](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetSubMenus.html).

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.html)
[IFrame::GetSubMenuCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
