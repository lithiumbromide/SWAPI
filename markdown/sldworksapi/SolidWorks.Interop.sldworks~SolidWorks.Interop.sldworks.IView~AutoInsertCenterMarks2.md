---
title: "AutoInsertCenterMarks2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "AutoInsertCenterMarks2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks2.html"
---

# AutoInsertCenterMarks2 Method (IView)

Automatically inserts the specified center marks in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoInsertCenterMarks2( _
   ByVal InsertType As System.Integer, _
   ByVal InsertOption As System.Integer, _
   ByVal LinearSlotCenter As System.Boolean, _
   ByVal ArcSlotCenter As System.Boolean, _
   ByVal UseDocumentDefaults As System.Boolean, _
   ByVal Size As System.Double, _
   ByVal Gap As System.Double, _
   ByVal ExtendedLines As System.Boolean, _
   ByVal CenterLineFont As System.Boolean, _
   ByVal Angle As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim InsertType As System.Integer
Dim InsertOption As System.Integer
Dim LinearSlotCenter As System.Boolean
Dim ArcSlotCenter As System.Boolean
Dim UseDocumentDefaults As System.Boolean
Dim Size As System.Double
Dim Gap As System.Double
Dim ExtendedLines As System.Boolean
Dim CenterLineFont As System.Boolean
Dim Angle As System.Double
Dim value As System.Boolean

value = instance.AutoInsertCenterMarks2(InsertType, InsertOption, LinearSlotCenter, ArcSlotCenter, UseDocumentDefaults, Size, Gap, ExtendedLines, CenterLineFont, Angle)
```

### C#

```csharp
System.bool AutoInsertCenterMarks2(
   System.int InsertType,
   System.int InsertOption,
   System.bool LinearSlotCenter,
   System.bool ArcSlotCenter,
   System.bool UseDocumentDefaults,
   System.double Size,
   System.double Gap,
   System.bool ExtendedLines,
   System.bool CenterLineFont,
   System.double Angle
)
```

### C++/CLI

```cpp
System.bool AutoInsertCenterMarks2(
   System.int InsertType,
   System.int InsertOption,
   System.bool LinearSlotCenter,
   System.bool ArcSlotCenter,
   System.bool UseDocumentDefaults,
   System.double Size,
   System.double Gap,
   System.bool ExtendedLines,
   System.bool CenterLineFont,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `InsertType`: Features for which to insert center marks as defined in [swAutoInsertCenterMarkTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAutoInsertCenterMarkTypes_e.html)
- `InsertOption`: Center mark options as defined in [swCenterMarkConnectionLine_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCenterMarkConnectionLine_e.html)
- `LinearSlotCenter`: True to add center marks to slot centers, false to add them to slot ends
- `ArcSlotCenter`: True to add center marks to arc centers, false to add them to arc ends
- `UseDocumentDefaults`: True to use the display settings specified in [**Tools > Options > Document Properties > Centerlines/Center Marks**](ms-its:swconst.chm::/DP_CenterlinesCenterMarks.htm), false to use the display settings set by this method
- `Size`: Size of center mark; valid only if UseDocumentDefaults is false
- `Gap`: Size of gap between the center mark and extension line; valid only if UseDocumentDefaults is false and the **Tools > Options > Document Properties > Centerlines/Center Marks > Scale by view scale** check box is clear (see **Remarks**)
- `ExtendedLines`: True to extend lines from center mark points, false to not; valid only if UseDocumentDefaults is false
- `CenterLineFont`: True to use the centerline font, false to not; valid only if UseDocumentDefaults is false
- `Angle`: Rotation angle for the center mark; a positive angle rotates the center mark counterclockwise

### Return Value

True if successful, false if not

## VBA Syntax

See [View::AutoInsertCenterMarks2](ms-its:sldworksapivb6.chm::/sldworks~View~AutoInsertCenterMarks2.html).

## Examples

[Automatically Insert Center Marks (C#)](Auto_Insert_Center_Marks_Example_CSharp.htm)
[Automatically Insert Center Marks (VB.NET)](Auto_Insert_Center_Marks_Example_VBNET.htm)
[Automatically Insert Center Marks (VBA)](Auto_Insert_Center_Marks_Example_VB.htm)

## Remarks

Call this method on each active view in which you want to insert center marks.

Before calling this method:

1. Call [IDrawingDoc::ActivateView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActivateView.html) with the name of the view to activate.
2. Call [IDrawingDoc::ActiveDrawingView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html) to get a handle on the activated view.

Call [IDrawingDoc::InsertCenterMark3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertCenterMark3.html) if you want to insert one center mark in one view.

| To... | Call... |
| --- | --- |
| Get the Tools > Options > Document Properties > Centerlines/Center Marks > Scale by view scale setting | IModelDocExtension::GetUserPreferenceToggle swUserPreferenceToggle_e .swDetailingCenterMarkScaleByViewScale, swUserPreferenceOption_e .swDetailingNoOptionSpecified |
| Set the Tools > Options > Document Properties > Centerlines/Center Marks > Scale by view scale setting | IModelDocExtension::SetUserPreferenceToggle swUserPreferenceToggle_e.swDetailingCenterMarkScaleByViewScale, swUserPreferenceOption_e.swDetailingNoOptionSpecified, < value > |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCenterMarkCount2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkCount2.html)
[IView::GetCenterMarkInfo Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarkInfo.html)
[IView::GetCenterMarks Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCenterMarks.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
