---
title: "SetupSheet5 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetupSheet5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet5.html"
---

# SetupSheet5 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::SetupSheet6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet6.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetupSheet5( _
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
   ByVal RemoveModifiedNotes As System.Boolean _
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
Dim value As System.Boolean

value = instance.SetupSheet5(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height, PropertyViewName, RemoveModifiedNotes)
```

### C#

```csharp
System.bool SetupSheet5(
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
   System.bool RemoveModifiedNotes
)
```

### C++/CLI

```cpp
System.bool SetupSheet5(
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
   System.bool RemoveModifiedNotes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name for the sheet
- `PaperSize`: Size of paper if using swDwgTemplateNone as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `TemplateIn`: Template as defined in [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)
- `Scale1`: Scale numerator
- `Scale2`: Scale denominator
- `FirstAngle`: True for first angle projection, false otherwise
- `TemplateName`: Name of custom template with full directory path if using swDwgTemplateCustom
- `Width`: Paper width; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize is set to swDwgPaperSizes_e.swDwgPapersUserDefined
- `Height`: Paper height if TemplateIn is set to swDwgTemplateNone or swDwgPapersUserDefined
- `PropertyViewName`: Name of view containing the model from which to get custom property values
- `RemoveModifiedNotes`: True to delete modified notes, false to not

## VBA Syntax

See [DrawingDoc::SetupSheet5](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetupSheet5.html).

## Remarks

Call [IModelDoc2::ForceRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html) after calling IDrawingDoc::SetupSheet5 to update any changes to first angle/third angle projections in the drawing views.

If you specify a different filename for TemplateName than what is currently being used by SOLIDWORKS, then SOLIDWORKS updates the sheet format.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html)
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html)
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.html)
[IDrawingDoc::IReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets.html)
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.html)
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
[IDrawingDoc::ReorderSheets](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.html)
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
