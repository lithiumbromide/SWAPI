---
title: "AddToolbar4 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddToolbar4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar4.html"
---

# AddToolbar4 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::AddToolbar5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddToolbar5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddToolbar4( _
   ByVal Cookie As System.Integer, _
   ByVal Title As System.String, _
   ByVal SmallBitmapImage As System.String, _
   ByVal LargeBitmapImage As System.String, _
   ByVal MenuPositionForToolbar As System.Integer, _
   ByVal DocumentType As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim Title As System.String
Dim SmallBitmapImage As System.String
Dim LargeBitmapImage As System.String
Dim MenuPositionForToolbar As System.Integer
Dim DocumentType As System.Integer
Dim value As System.Integer

value = instance.AddToolbar4(Cookie, Title, SmallBitmapImage, LargeBitmapImage, MenuPositionForToolbar, DocumentType)
```

### C#

```csharp
System.int AddToolbar4(
   System.int Cookie,
   System.string Title,
   System.string SmallBitmapImage,
   System.string LargeBitmapImage,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

### C++/CLI

```cpp
System.int AddToolbar4(
   System.int Cookie,
   System.String^ Title,
   System.String^ SmallBitmapImage,
   System.String^ LargeBitmapImage,
   System.int MenuPositionForToolbar,
   System.int DocumentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Resource ID of the toolbar; this is the same cookie that you specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `Title`: Title of the toolbar
- `SmallBitmapImage`: Bitmap file to use for the small bitmap for the toolbar (see Remarks)
- `LargeBitmapImage`: Bitmap file to use for the large bitmap for the toolbar (see Remarks)
- `MenuPositionForToolbar`: Not used (SOLIDWORKS always puts toolbar names in alphabetical order)
- `DocumentType`: Bitwise values indicating what frame window types should have this toolbar's name added to the View > Toolbars menu; values from [swDocTemplateTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

### Return Value

Toolbar ID for use with other methods or -1 if not created

## VBA Syntax

See [SldWorks::AddToolbar4](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddToolbar4.html).

## Examples

[Create Toolbars (C++)](Create_Toolbars_Example_CPlusPlus_COM.htm)

## Remarks

For information about using this method with the [ISwAddin](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin.html) object, see [Using ISwAddin to Create a SOLIDWORKS Add-in](sldworksAPIProgGuide.chm::/OVERVIEW/Using_SwAddin_to_Create_a_SOLIDWORKS_Addin.htm).

This method:

- Only operates properly when the application is implemented as a DLL and not as an .exe.
- Adds the toolbar name to the View > Toolbars menu.
- Only creates the toolbar and passes the image for the buttons to SOLIDWORKS. To add functionality, use [ISldWorks::AddToolbarCommand2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddToolbarCommand2.html).

The bitmap images should contain the bitmaps for each of the buttons, including separators, in the toolbar as a single bitmap. For a small bitmap, the image for each button must be 16x16; for a large bitmap, it must be 24x24. The bitmaps should use a 256-color palette.

If either SmallBitmapImage or LargeBitmapImage is null or empty, then the provided image is scaled to create the appropriately sized bitmap for the other argument.

NOTES:

- When your add-in is unloaded, you must call [ISldWorks::RemoveToolbar2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveToolbar2.html) to remove this toolbar.
- If you want the toolbar to show up in specific locations only, do not use the now obsolete ISldWorks::ShowToolbar2 method. If your application uses that method, your application ignores the DocumentType argument. ISldWorks::ShowToolbar2 assumes that the application is controlling the visibility state of the toolbar, and not the user. This means that the toolbar will be available in all locations.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
[ISldWorks::DragToolbarButton Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DragToolbarButton.html)
[ISldWorks::GetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarDock2.html)
[ISldWorks::GetToolbarState2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetToolbarState2.html)
[ISldWorks::HideToolbar2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~HideToolbar2.html)
[ISldWorks::SetToolbarDock2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetToolbarDock2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
