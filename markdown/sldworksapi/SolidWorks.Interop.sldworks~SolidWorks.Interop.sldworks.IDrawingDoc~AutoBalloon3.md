---
title: "AutoBalloon3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutoBalloon3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon3.html"
---

# AutoBalloon3 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::AutoBalloon4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoBalloon3( _
   ByVal Layout As System.Integer, _
   ByVal IgnoreMultiple As System.Boolean, _
   ByVal Style As System.Integer, _
   ByVal Size As System.Integer, _
   ByVal UpperTextContent As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextContent As System.Integer, _
   ByVal LowerText As System.String, _
   ByVal Layername As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim IgnoreMultiple As System.Boolean
Dim Style As System.Integer
Dim Size As System.Integer
Dim UpperTextContent As System.Integer
Dim UpperText As System.String
Dim LowerTextContent As System.Integer
Dim LowerText As System.String
Dim Layername As System.String
Dim value As System.Object

value = instance.AutoBalloon3(Layout, IgnoreMultiple, Style, Size, UpperTextContent, UpperText, LowerTextContent, LowerText, Layername)
```

### C#

```csharp
System.object AutoBalloon3(
   System.int Layout,
   System.bool IgnoreMultiple,
   System.int Style,
   System.int Size,
   System.int UpperTextContent,
   System.string UpperText,
   System.int LowerTextContent,
   System.string LowerText,
   System.string Layername
)
```

### C++/CLI

```cpp
System.Object^ AutoBalloon3(
   System.int Layout,
   System.bool IgnoreMultiple,
   System.int Style,
   System.int Size,
   System.int UpperTextContent,
   System.String^ UpperText,
   System.int LowerTextContent,
   System.String^ LowerText,
   System.String^ Layername
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layout`: Layout style of the balloons as defined by [swBalloonLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonLayoutType_e.html) or specify -1 for this argument to use the document default layout style
- `IgnoreMultiple`: True to apply a balloon to only one instance of a component, false to apply balloons to all instances of that component
- `Style`: Style of the balloons as defined by [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html) or specify -1 to use the document default balloon style
- `Size`: Fit of balloon as defined by [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html) or specify -1 to use the document default balloon fit
- `UpperTextContent`: Upper-text content style as defined by [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html) or specify -1 to use the document default upper text content
- `UpperText`: Text for upper balloon
- `LowerTextContent`: Lower-text content style as defined by [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html) or specify -1 to use the document default lower text content

  **NOTE:** This and the next argument are only effective when Style is set to swBS_SplitCirc. See the SOLIDWORKS Help for additional details about autoballoons.
- `LowerText`: Text for lower balloon
- `Layername`: Name of the layer for this balloon

### Return Value

Array of newly created [notes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [DrawingDoc::AutoBalloon3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutoBalloon3.html).

## Examples

[Insert AutoBalloons (VBA)](Insert_AutoBalloons_Example_VB_AutoBallooon3_VB.htm)

## Remarks

This method automatically creates the BOM balloons for the selected drawing views. If a drawing sheet is selected, BOM balloons are automatically created for all of the drawing views on that drawing sheet.

| To get or set default values for... | Use... |
| --- | --- |
| Layout | IModelDocExtension::GetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified) - or - IModelDocExtension::SetUserPreferenceInteger (swUserPreferenceIntegerValue_e.swDetailingAutoBalloonLayout, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonLayoutType_e.< Value >) |
| Style | IModelDocExtension::GetUserPreferenceInteger((swUserPreferenceIntegerValue_e.swDetailingBOMBalloonStyle, swUserPreferenceOption_e.swDetailingNoOptionSpecified) - or - IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonFit_e.< Value >) |
| Size | IModelDocExtension::GetUserPreferenceInteger((swUserPreferenceIntegerValue_e.swDetailingBOMBalloonFit, swUserPreferenceOption_e.swDetailingNoOptionSpecified) - or - (swUserPreferenceIntegerValue_e.swDetailingBOMStackedBalloonFit, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonFit_e.< Value >) |
| UpperTextContent | IModelDocExtension::GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMUpperText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) - or - IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMUpperText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonTextContent_e.< Value >) |
| LowerTextContent | IModelDocExtension::GetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified) - or - IModelDocExtension::SetUserPreferenceInteger(swUserPreferenceIntegerValue_e.swDetailingBOMLowerText, swUserPreferenceOption_e.swDetailingNoOptionSpecified, swBalloonTextContent_e.< Value >) |

This method also allows you to get only the balloons just created.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IModelDocExtension::InsertBOMBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
