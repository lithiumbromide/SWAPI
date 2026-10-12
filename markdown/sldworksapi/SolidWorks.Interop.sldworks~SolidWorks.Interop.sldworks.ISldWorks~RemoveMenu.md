---
title: "RemoveMenu Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveMenu"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.html"
---

# RemoveMenu Method (ISldWorks)

Removes a menu item from the specified document frame.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveMenu( _
   ByVal DocType As System.Integer, _
   ByVal MenuItemString As System.String, _
   ByVal CallbackFcnAndModule As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim DocType As System.Integer
Dim MenuItemString As System.String
Dim CallbackFcnAndModule As System.String
Dim value As System.Boolean

value = instance.RemoveMenu(DocType, MenuItemString, CallbackFcnAndModule)
```

### C#

```csharp
System.bool RemoveMenu(
   System.int DocType,
   System.string MenuItemString,
   System.string CallbackFcnAndModule
)
```

### C++/CLI

```cpp
System.bool RemoveMenu(
   System.int DocType,
   System.String^ MenuItemString,
   System.String^ CallbackFcnAndModule
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DocType`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)
- `MenuItemString`: Menu string (e.g., submenuString@menuString)
- `CallbackFcnAndModule`: Callback function and module for this menu item as specified when the menu item was added; see [IFrame::AddMenuItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.html)

### Return Value

True if the menu item was removed successfully, false if not

## VBA Syntax

See [SldWorks::RemoveMenu](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveMenu.html).

## Remarks

When a menu item is added with [ISldWorks::AddMenuItem4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem4.html) or [IFrame::AddMenu](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFrame~AddMenu.html), the document type for which the menu appears is specified. The DocType argument for this method must match the one used when the menu was created.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetMenuStrings Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings.html)
[ISldWorks::AddMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.html)
[ISldWorks::AddMenuItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.html)
[ISldWorks::AddMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuPopupItem2.html)
[ISldWorks::RemoveFromMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromMenu.html)
[ISldWorks::RemoveFromPopupMenu Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFromPopupMenu.html)
[ISldWorks::RemoveMenuPopupItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenuPopupItem2.html)
