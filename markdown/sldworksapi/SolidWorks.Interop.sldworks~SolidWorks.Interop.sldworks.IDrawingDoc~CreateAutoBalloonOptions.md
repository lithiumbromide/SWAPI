---
title: "CreateAutoBalloonOptions Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateAutoBalloonOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html"
---

# CreateAutoBalloonOptions Method (IDrawingDoc)

Creates an object that stores auto balloon options.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAutoBalloonOptions() As AutoBalloonOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As AutoBalloonOptions

value = instance.CreateAutoBalloonOptions()
```

### C#

```csharp
AutoBalloonOptions CreateAutoBalloonOptions()
```

### C++/CLI

```cpp
AutoBalloonOptions^ CreateAutoBalloonOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html)

## VBA Syntax

See [DrawingDoc::CreateAutoBalloonOptions](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateAutoBalloonOptions.html).

## Examples

[Add Autoballoons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)
[Add Autoballoons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)
[Add Autoballoons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)

## Remarks

To automatically create BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call this method to create an [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) object.
3. Set the properties on the IAutoBalloonOptions object.
4. Pass the IAutoBalloonOptions object in a call to [IDrawingDoc::AutoBalloon5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon5.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IModelDocExtension::CreateBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.html)
[IModelDocExtension::CreateStackedBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
