---
title: "IAutoBalloonOptions Interface"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html"
---

# IAutoBalloonOptions Interface

Allows access to auto balloon options.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAutoBalloonOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
```

### C#

```csharp
public interface IAutoBalloonOptions
```

### C++/CLI

```cpp
public interface class IAutoBalloonOptions
```

## VBA Syntax

See [AutoBalloonOptions](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions.html).

## Examples

[Add Auto Balloons to Drawing (VBA)](Add_Autoballoon_to_Face_Example_VB.htm)
[Add Auto Balloons to Drawing (VB.NET)](Add_Autoballoon_to_Face_Example_VBNET.htm)
[Add Auto Balloons to Drawing (C#)](Add_Autoballoon_to_Face_Example_CSharp.htm)

## Remarks

To automatically create BOM balloons:

1. Select one or more views or sheets for which to automatically create BOM balloons.
2. Call [IDrawingDoc::CreateAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html) to create IAutoBalloonOptions object.
3. Set the properties on IAutoBalloonOptions.
4. Pass IAutoBalloonOptions in a call to [IDrawingDoc::AutoBalloon5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon5.html).

## Accessors

[IDrawingDoc::CreateAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html)

## Access Diagram

[AutoBalloonOptions](SWObjectModel.pdf#AutoBalloonOptions)

## See Also

[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
