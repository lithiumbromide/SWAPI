---
title: "CreateBalloonOptions Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateBalloonOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.html"
---

# CreateBalloonOptions Method (IModelDocExtension)

Creates an object that stores BOM balloon options.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBalloonOptions() As BalloonOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As BalloonOptions

value = instance.CreateBalloonOptions()
```

### C#

```csharp
BalloonOptions CreateBalloonOptions()
```

### C++/CLI

```cpp
BalloonOptions^ CreateBalloonOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html)

## VBA Syntax

See [ModelDocExtension::CreateBalloonOptions](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateBalloonOptions.html).

## Examples

[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)
[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)

## Remarks

To create a single BOM balloon:

1. Select an item for which to create a BOM balloon.
2. Call this method to create an [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) object.
3. Set the properties on the IBalloonOptions object.
4. Pass the IBalloonOptions object in a call to [IModelDocExtension::InsertBOMBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateStackedBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html)
[IDrawingDoc::CreateAutoBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
