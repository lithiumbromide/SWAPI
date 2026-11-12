---
title: "ICenterMark Interface"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html"
---

# ICenterMark Interface

Allows access to a center mark or center mark set in a [drawing view](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
```

### C#

```csharp
public interface ICenterMark
```

### C++/CLI

```cpp
public interface class ICenterMark
```

## VBA Syntax

See [CenterMark](ms-its:sldworksapivb6.chm::/sldworks~CenterMark.html).

## Examples

[Select All Center Marks (C#)](Select_All_Center_Marks_Example_CSharp.htm)
[Select All Center Marks (VB.NET)](Select_All_Center_Marks_Example_VBNET.htm)
[Select All Center Marks (VBA)](Select_All_Center_Marks_Example_VB.htm)
[Get and Set Center Mark Set (C#)](Get_and_Set_Center_Marks_Set_Example_CSharp.htm)
[Get and Set Center Mark Set (VB.NET)](Get_and_Set_Center_Marks_Set_Example_VBNET.htm)
[Get and Set Center Mark Set (VBA)](Get_and_Set_Center_Marks_Set_Example_VBA.htm)

## Remarks

Center marks are now annotations. Previously, center marks were features.

Use [ICenterMark::GetAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~GetAnnotation.html) to access the [IAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html) APIs. If you use [ISelectionMgr::GetSelectedObject6](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObject6.html) or [ISelectionMgr::GetSelectedObjectType3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.html) to retrieve center marks, then these values are returned:

- swSelCENTERMARKSSYMS = 100 for the center marks that are annotations
- swSelCENTERMARKS = 28 for the center marks that are features

Both methods retrieve the ICenterMark object.

| To... | Use... |
| --- | --- |
| Traverse center marks that are annotations | IView::GetFirstAnnotation3 , IAnnotation::GetNext3 or IView::GetFirstCenterMark , and ICenterMark::GetNext |
| Retrieve center marks that are features | IView::GetCenterMarkCount2 and IView::GetCenterMarks |

Center marks are displayed using the document's default display attribute settings. If you want the setting to be local to this symbol, then set the [ICenterMark::UseDocDisplaySettings](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~UseDocDisplaySettings.html) property to false and modify the [ICenterMark::ShowLines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~ShowLines.html), [ICenterMark::Size](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~Size.html), and [ICenterMark::CenterLineFont](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~CenterLineFont.html) properties as needed.

A center mark set is a linear or circular pattern.

## Accessors

[ICenterMark::GetNext Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterMark~GetNext.html)

[IDrawingDoc::InsertCenterMark3 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertCenterMark3.html)

[IView::GetCenterMarks](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetCenterMarks.html) and [IView::IGetCenterMarks Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetCenterMarks.html)

[IView::GetFirstCenterMark Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstCenterMark.html)

## Access Diagram

[CenterMark](SWObjectModel.pdf#CenterMark)

## See Also

[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IView::AutoInsertCenterMarks Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AutoInsertCenterMarks.html)
