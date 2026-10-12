---
title: "InsertModelInPredefinedView Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertModelInPredefinedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView.html"
---

# InsertModelInPredefinedView Method (IDrawingDoc)

Inserts the model into the predefined drawing views in the active drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertModelInPredefinedView( _
   ByVal ModelName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim ModelName As System.String
Dim value As System.Boolean

value = instance.InsertModelInPredefinedView(ModelName)
```

### C#

```csharp
System.bool InsertModelInPredefinedView(
   System.string ModelName
)
```

### C++/CLI

```cpp
System.bool InsertModelInPredefinedView(
   System.String^ ModelName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModelName`: Name of the model to insert into the predefined drawing views in the active drawing sheet

### Return Value

True if the model is inserted, false if not

## VBA Syntax

See [DrawingDoc::InsertModelInPredefinedView](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertModelInPredefinedView.html).

## Remarks

| If you... | Then... |
| --- | --- |
| Preselect drawing views | This method inserts the model in those predefined drawing views. |
| Do not preselect any drawing views | This method inserts the model in all predefined views in the drawing. |
| Specify an empty filename | SOLIDWORKS prompts the user for the desired model's filename. |
| Specify a filename | SOLIDWORKS inserts that model into the predefined drawing views, without displaying any dialogs. |

If the model is not already open, SOLIDWORKS attempts to open it hidden.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateView.html)
[IDrawingDoc::CreateViewport3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.html)
[IDrawingDoc::GetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetFirstView.html)
[IDrawingDoc::HideShowDrawingViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~HideShowDrawingViews.html)
[IDrawingDoc::IGetFirstView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetFirstView.html)
[IDrawingDoc::SuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SuppressView.html)
[IDrawingDoc::UnsuppressView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~UnsuppressView.html)
[IDrawingDoc::ActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html)
[IDrawingDoc::IActiveDrawingView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.html)
[IDrawingDoc::ReplaceViewModel Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReplaceViewModel.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
