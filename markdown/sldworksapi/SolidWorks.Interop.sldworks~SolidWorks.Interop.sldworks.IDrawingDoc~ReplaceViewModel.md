---
title: "ReplaceViewModel Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "ReplaceViewModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReplaceViewModel.html"
---

# ReplaceViewModel Method (IDrawingDoc)

Replaces the specified instances of a model in the specified drawing views.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReplaceViewModel( _
   ByVal NewModelPathName As System.String, _
   ByVal Views As System.Object, _
   ByVal Instances As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim NewModelPathName As System.String
Dim Views As System.Object
Dim Instances As System.Object
Dim value As System.Boolean

value = instance.ReplaceViewModel(NewModelPathName, Views, Instances)
```

### C#

```csharp
System.bool ReplaceViewModel(
   System.string NewModelPathName,
   System.object Views,
   System.object Instances
)
```

### C++/CLI

```cpp
System.bool ReplaceViewModel(
   System.String^ NewModelPathName,
   System.Object^ Views,
   System.Object^ Instances
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewModelPathName`: Full path and filename of the replacement model
- `Views`: Array of [IView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html)s in which to replace the model
- `Instances`: Array of [IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)s that are specific instances of the model to replace in the drawing

### Return Value

True if the model is replaced, false if not

## VBA Syntax

See [DrawingDoc::ReplaceViewModel](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~ReplaceViewModel.html).

## Examples

[Replace View Model (C#)](Replace_View_Model_Example_CSharp.htm)
[Replace View Model (VB.NET)](Replace_View_Model_Example_VBNET.htm)
[Replace View Model (VBA)](Replace_View_Model_Example_VB.htm)

## Remarks

This method corresponds to **Tools > Replace Model**.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertModelInPredefinedView Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertModelInPredefinedView.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
