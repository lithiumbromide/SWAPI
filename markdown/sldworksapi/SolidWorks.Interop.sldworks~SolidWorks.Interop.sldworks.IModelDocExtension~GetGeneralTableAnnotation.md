---
title: "GetGeneralTableAnnotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetGeneralTableAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetGeneralTableAnnotation.html"
---

# GetGeneralTableAnnotation Method (IModelDocExtension)

Creates a general table annotation for SOLIDWORKS MBD 3D PDF.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGeneralTableAnnotation( _
   ByVal UseAnchorPoint As System.Boolean, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal TableTemplate As System.String, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UseAnchorPoint As System.Boolean
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim TableTemplate As System.String
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation

value = instance.GetGeneralTableAnnotation(UseAnchorPoint, X, Y, AnchorType, TableTemplate, Rows, Columns)
```

### C#

```csharp
TableAnnotation GetGeneralTableAnnotation(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.string TableTemplate,
   System.int Rows,
   System.int Columns
)
```

### C++/CLI

```cpp
TableAnnotation^ GetGeneralTableAnnotation(
   System.bool UseAnchorPoint,
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.String^ TableTemplate,
   System.int Rows,
   System.int Columns
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseAnchorPoint`: True to anchor the table by AnchorType and ignore any coordinates specified by X and Y, false to use the coordinates specified by X and Y
- `X`: X coordinate of this table annotation; valid only if UseAnchorPoint is false
- `Y`: Y coordinate of this table annotation; valid only if UseAnchorPoint is false
- `AnchorType`: Type of anchor as defined in [swBOMConfigurationAnchorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBOMConfigurationAnchorType_e.html); valid only if UseAnchorPoint is true, and TableTemplate is empty (see **Remarks**)
- `TableTemplate`: Path and file name of the general table template to use (see Remarks)
- `Rows`: Number of rows in the table annotation; valid only if TableTemplate is empty (see **Remarks**)
- `Columns`: Number of columns in the table annotation; valid only if TableTemplate is empty (see **Remarks**)

### Return Value

[ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)

## VBA Syntax

See [ModelDocExtension::GetGeneralTableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetGeneralTableAnnotation.html).

## Examples

[Create General Table Annotation for SOLIDWORKS MBD 3D PDF (C#)](Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_CSharp.htm)
[Create General Table Annotation for SOLIDWORKS MBD 3D PDF (VB.NET)](Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_VBNET.htm)
[Create General Table Annotation for SOLIDWORKS MBD 3D PDF (VBA)](Create_General_Table_for_SOLIDWORKS_3D_PDF_Example_VB.htm)

## Remarks

| If TableTemplate is... | Then this method.. |
| --- | --- |
| A valid path and file name | Ignores AnchorType, Rows, and Columns and creates a general table annotation based on TableTemplate. |
| Empty | Creates a general table annotation using the specified parameters except TableTemplate. |

This method creates an object for the specified table annotation, but it does not insert the table annotation in the model.

Use [IModelDocExtension::InsertGeneralTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertGeneralTableAnnotation.html) to create and insert a table annotation in the model.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
