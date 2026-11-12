---
title: "IGetSubMenus Method (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "IGetSubMenus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~IGetSubMenus.html"
---

# IGetSubMenus Method (IFrame)

Gets the submenus for this frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSubMenus( _
   ByVal DocType As System.Integer, _
   ByVal FullMenuName As System.String, _
   ByVal NumSubMenus As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim DocType As System.Integer
Dim FullMenuName As System.String
Dim NumSubMenus As System.Integer
Dim value As System.String

value = instance.IGetSubMenus(DocType, FullMenuName, NumSubMenus)
```

### C#

```csharp
System.string IGetSubMenus(
   System.int DocType,
   System.string FullMenuName,
   System.int NumSubMenus
)
```

### C++/CLI

```cpp
System.String^ IGetSubMenus(
   System.int DocType,
   System.String^ FullMenuName,
   System.int NumSubMenus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Type of document as defined by [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `FullMenuName`: Full name of menu
- `NumSubMenus`: Number of submenus

### Return Value

- in-process, unmanaged C++: Pointer to an array of the names of the submenus of size NumSubMenus

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IFrame::GetSubMenuCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~GetSubMenuCount.html) before calling this method to get the size of the array.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[IFrame::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.html)
[IFrame::AddMenuItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)
[IFrame::AddMenuPopupItem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuPopupItem.html)
[IFrame::GetSubMenus Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~GetSubMenus.html)

## Availability

SoldiWorks 2003 FCS, Revision Number 11.0
