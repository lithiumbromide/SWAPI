---
title: "SetupSheet6 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetupSheet6"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.html"
---

# SetupSheet6 Method (IDrawingDoc)

Sets up the specified drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetupSheet6( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal TemplateIn As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal TemplateName As System.String, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal PropertyViewName As System.String, _
   ByVal RemoveModifiedNotes As System.Boolean, _
   ByVal ZoneLeftMargin As System.Double, _
   ByVal ZoneRightMargin As System.Double, _
   ByVal ZoneTopMargin As System.Double, _
   ByVal ZoneBottomMargin As System.Double, _
   ByVal ZoneRow As System.Integer, _
   ByVal ZoneCol As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Integer
Dim TemplateIn As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim FirstAngle As System.Boolean
Dim TemplateName As System.String
Dim Width As System.Double
Dim Height As System.Double
Dim PropertyViewName As System.String
Dim RemoveModifiedNotes As System.Boolean
Dim ZoneLeftMargin As System.Double
Dim ZoneRightMargin As System.Double
Dim ZoneTopMargin As System.Double
Dim ZoneBottomMargin As System.Double
Dim ZoneRow As System.Integer
Dim ZoneCol As System.Integer
Dim value As System.Boolean

value = instance.SetupSheet6(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height, PropertyViewName, RemoveModifiedNotes, ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, ZoneBottomMargin, ZoneRow, ZoneCol)
```

### C#

```csharp
System.bool SetupSheet6(
   System.string Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.string TemplateName,
   System.double Width,
   System.double Height,
   System.string PropertyViewName,
   System.bool RemoveModifiedNotes,
   System.double ZoneLeftMargin,
   System.double ZoneRightMargin,
   System.double ZoneTopMargin,
   System.double ZoneBottomMargin,
   System.int ZoneRow,
   System.int ZoneCol
)
```

### C++/CLI

```cpp
System.bool SetupSheet6(
   System.String^ Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.String^ TemplateName,
   System.double Width,
   System.double Height,
   System.String^ PropertyViewName,
   System.bool RemoveModifiedNotes,
   System.double ZoneLeftMargin,
   System.double ZoneRightMargin,
   System.double ZoneTopMargin,
   System.double ZoneBottomMargin,
   System.int ZoneRow,
   System.int ZoneCol
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the sheet to set up
- `PaperSize`: Size of paper as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html); valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone
- `TemplateIn`: Template as defined in [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)
- `Scale1`: Scale numerator
- `Scale2`: Scale denominator
- `FirstAngle`: True for first angle projection, false for third angle projection
- `TemplateName`: Name of custom template with full directory path; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateCustom
- `Width`: Paper width; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes_e.swDwgPapersUserDefined
- `Height`: Paper height; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes_e.swDwgPapersUserDefined
- `PropertyViewName`: Name of view containing the model from which to get custom property values
- `RemoveModifiedNotes`: True to delete modified notes, false to not
- `ZoneLeftMargin`: Zone area left margin; distance from drawing sheet's left edge
- `ZoneRightMargin`: Zone area right margin; distance from drawing sheet's right edge
- `ZoneTopMargin`: Zone area top margin; distance from drawing sheet's top edge
- `ZoneBottomMargin`: Zone area bottom margin; distance from drawing sheet's bottom edge
- `ZoneRow`: Number of zone rows in the zone area of this sheet (see **Remarks**)
- `ZoneCol`: Number of zone columns in the zone area of this sheet (see **Remarks**)

### Return Value

True if drawing sheet setup is successful, false if not

## VBA Syntax

See [DrawingDoc::SetupSheet6](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetupSheet6.html).

## Examples

[Create Drawing Sheet Zones (VBA)](Create_Drawing_Sheet_Zones_Example_VB.htm)
[Create Drawing Sheet Zones (VB.NET)](Create_Drawing_Sheet_Zones_Example_VBNET.htm)
[Create Drawing Sheet Zones (C#)](Create_Drawing_Sheet_Zones_Example_CSharp.htm)
[Modify Multiple Drawing Sheets Setups (C#)](Modify_Multiple_Drawing_Sheets_Setups_Example_CSharp.htm)
[Modify Multiple Drawing Sheets Setups (VB.NET)](Modify_Multiple_Drawing_Sheets_Setups_Example_VBNET.htm)
[Modify Multiple Drawing Sheets Setups (VBA)](Modify_Multiple_Drawing_Sheets_Setups_Example_VB.htm)

## Remarks

After calling this method, call [IModelDoc2::ForceRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html) to update any changes to first angle/third angle projections in the drawing views.

If you specify a different filename for TemplateName than what is currently being used by SOLIDWORKS, then SOLIDWORKS updates the sheet format.

The drawing sheet can be set up with zones that annotations in other views can reference. Each zone is referenced by an alphanumeric label that is defined using the Zone Editor. See the SOLIDWORKS Help for more information about drawing sheet zones.

Multiplying ZoneRow by ZoneCol equals the total number of zones in the zone area of this drawing sheet. The zone area is specified by ZoneLeftMargin, ZoneRightMargin, ZoneTopMargin, and ZoneBottomMargin.

To modify the setups of multiple drawing sheets with just one call to IDrawingDoc::SetupSheet6, call [IDrawingDoc::SetSelectedSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetSheetsSelected.html) before calling IDrawingDoc::SetupSheet6.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetEditSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html)
[IDrawingDoc::GetSheetCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html)
[IDrawingDoc::GetSheetNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::NewSheet4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet4.html)
[IDrawingDoc::PasteSheet Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~PasteSheet.html)
[IDrawingDoc::SheetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
[IDrawingDoc::ReorderSheets Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.html)
[ISheet::GetDrawingZone Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~GetDrawingZone.html)
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
