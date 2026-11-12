---
title: "AutoBalloon5 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutoBalloon5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.html"
---

# AutoBalloon5 Method (IDrawingDoc)

Automatically inserts BOM balloons in selected drawing views.

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoBalloon5( _
   ByVal BalloonOptions As AutoBalloonOptions _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim BalloonOptions As AutoBalloonOptions
Dim value As System.Object

value = instance.AutoBalloon5(BalloonOptions)
```

### C#

```csharp
System.object AutoBalloon5(
   AutoBalloonOptions BalloonOptions
)
```

### C++/CLI

```cpp
System.Object^ AutoBalloon5(
   AutoBalloonOptions^ BalloonOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BalloonOptions`: [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html)

### Return Value

Array of [INotes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [DrawingDoc::AutoBalloon5](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutoBalloon5.html).

## Examples

[Add Autoballoons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)
[Add Autoballoons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)
[Add Autoballoons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)

## Remarks

This method automatically inserts BOM balloons for bill of materials items in selected drawing views. If a drawing sheet is selected, BOM balloons are automatically inserted for all of the drawing views on that drawing sheet.

To automatically insert BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call [IDrawingDoc::CreateAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html) to create an [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) object.
3. Set the properties on the IAutoBalloonOptions object.
4. Call this method using the IAutoBalloonOptions object in the BalloonOptions argument.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IModelDocExtension::InsertBOMBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html)
[IModelDocExtension::InsertStackedBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
