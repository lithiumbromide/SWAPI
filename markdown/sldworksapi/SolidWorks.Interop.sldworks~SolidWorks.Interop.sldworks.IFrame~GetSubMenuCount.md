---
title: "GetSubMenuCount Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "GetSubMenuCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenuCount.html"
---

# GetSubMenuCount Method (IFrame)

Gets the number of submenus for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSubMenuCount( _
   ByVal DocType As System.Integer, _
   ByVal FullMenuName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim DocType As System.Integer
Dim FullMenuName As System.String
Dim value As System.Integer

value = instance.GetSubMenuCount(DocType, FullMenuName)
```

### C#

```csharp
System.int GetSubMenuCount(
   System.int DocType,
   System.string FullMenuName
)
```

### C++/CLI

```cpp
System.int GetSubMenuCount(
   System.int DocType,
   System.String^ FullMenuName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Type of document as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `FullMenuName`: Full name of the menu

### Return Value

Number of submenus

## VBA Syntax

See [Frame::GetSubMenuCount](ms-its:sldworksapivb6.chm::/sldworks~Frame~GetSubMenuCount.html).

## Remarks

Call this method before calling [IFrame::IGetSubMenus](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~IGetSubMenus.html) to get the size of the array.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)
[IFrame::RemoveMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.html)
[IFrame::RenameMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
