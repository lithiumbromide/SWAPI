---
title: "InsertBomTable Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "InsertBomTable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertBomTable.html"
---

# InsertBomTable Method (IView)

Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBomTable( _
   ByVal Template As System.String, _
   ByVal Xloc As System.Double, _
   ByVal Yloc As System.Double, _
   ByRef Errors As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Template As System.String
Dim Xloc As System.Double
Dim Yloc As System.Double
Dim Errors As System.Integer
Dim value As System.Object

value = instance.InsertBomTable(Template, Xloc, Yloc, Errors)
```

### C#

```csharp
System.object InsertBomTable(
   System.string Template,
   System.double Xloc,
   System.double Yloc,
   out System.int Errors
)
```

### C++/CLI

```cpp
System.Object^ InsertBomTable(
   System.String^ Template,
   System.double Xloc,
   System.double Yloc,
   [Out] System.int Errors
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Template`: File name of the template to use to create this BOM
- `Xloc`: X coordinate of the location of the BOM
- `Yloc`: Y coordinate of the location of the BOM
- `Errors`: Status of the BOM creation operation as defined in [swBOMConfigurationCreationErrors_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationCreationErrors_e.html)

### Return Value

[BOM table](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html)

## VBA Syntax

See [View::InsertBomTable](ms-its:sldworksapivb6.chm::/sldworks~View~InsertBomTable.html).

## Remarks

This method creates a default BOM table at the specified location, using the given template. There are some user preferences that control the default appearance of the table; set them before calling this method to create a BOM that looks like you want it to look. See:

- [ISldWorks::SetUserPreferenceToggle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceToggle.html) values swBOMConfigurationLocked, swBOMConfigurationUseDocumentFont, swBOMConfigurationUseSummaryInfo, swBOMConfigurationAlignBottom, swBOMContentsDisplayAtTop, swBOMControlIdFromAssembly, swBOMControlMissingRows, and swBOMControlSplitTable
- [ISldWorks::SetUserPreferenceIntegerValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceIntegerValue.html) values swBOMConfigurationAnchorType, swBOMConfigurationWhatToShow, swBOMControlMissingRowDisplay, and swBOMControlSplitDirection
- [ISldWorks::SetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~SetUserPreferenceDoubleValue.html) value swBOMControlSplitHeight

The Template argument is the full path name of the BOM template to use in creating this BOM. If you specify only a file name with no directory, SOLIDWORKS looks for it in install_dir\lang\local language. If the file name is blank, the template uses the **bomtemp.xls** file in that directory.

The Xloc and Yloc arguments are the (X,Y) drawing location where the BOM is anchored. To get the drawing origin from the drawing view origin, use [IView::GetXform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetXform.html) or [IView::IGetXform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetXform.html). To get the drawing view extents on the drawing, use [IView::GetOutline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetOutline.html) or [IView::IGetOutline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetOutline.html).

If the BOM creation fails, the Dispatch pointer that is returned is null or nothing. If you want more information about why the operation failed, use the Errors argument. You can pass null or nothing as the Errors argument if you are not interested in the specific information.

**NOTE:** Use [IView::InsertBomTable2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~InsertBomTable2.html) to insert a BOM using SOLIDWORKS table functionality.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IInsertBomTable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IInsertBomTable.html)
[IView::GetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOM.html)
[IView::GetKeepLinkedToBOMName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetKeepLinkedToBOMName.html)
[IView::SetKeepLinkedToBOM Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetKeepLinkedToBOM.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
