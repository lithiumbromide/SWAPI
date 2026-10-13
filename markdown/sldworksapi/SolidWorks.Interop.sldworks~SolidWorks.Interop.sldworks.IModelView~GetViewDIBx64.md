---
title: "GetViewDIBx64 Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetViewDIBx64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIBx64.html"
---

# GetViewDIBx64 Method (IModelView)

Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetViewDIBx64() As System.Long
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Long

value = instance.GetViewDIBx64()
```

### C#

```csharp
System.long GetViewDIBx64()
```

### C++/CLI

```cpp
System.int64 GetViewDIBx64();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to DIBSECTION for image

## VBA Syntax

See [ModelView::GetViewDIBx64](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetViewDIBx64.html).

## Examples

[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

## Remarks

The image type and resolution can be controlled interactively under TIFF export options.

If TIFF export is set to screen, then the output from this method is based on the current screen resolution. If it's set to print, then the output is based on the DPI specified in the TIFF options dialog.

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS Design application and must be deleted by the caller. For more information, see the description of Bitmap structures and DIBSECTION in Microsoft Help.

**NOTE:** This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModeler::GetViewDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIB.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
