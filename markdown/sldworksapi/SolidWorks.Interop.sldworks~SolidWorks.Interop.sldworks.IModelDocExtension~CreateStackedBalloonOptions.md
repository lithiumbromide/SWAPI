---
title: "CreateStackedBalloonOptions Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateStackedBalloonOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html"
---

# CreateStackedBalloonOptions Method (IModelDocExtension)

Creates an object that stores options for stacked balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateStackedBalloonOptions() As StackedBalloonOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As StackedBalloonOptions

value = instance.CreateStackedBalloonOptions()
```

### C#

```csharp
StackedBalloonOptions CreateStackedBalloonOptions()
```

### C++/CLI

```cpp
StackedBalloonOptions^ CreateStackedBalloonOptions();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html)

## VBA Syntax

See [ModelDocExtension::CreateStackedBalloonOptions](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateStackedBalloonOptions.html).

## Examples

[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)
[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)
[Insert BOM Table and Stacked Balloon (C#)](Insert_BOM_Table_and_Stacked_Balloon_Example_CSharp.htm)

## Remarks

To create a stack of balloons:

1. Select an item to create the first balloon of the stack.
2. Call this method to create an [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) object.
3. Set the properties on the IStackedBalloonOptions object.
4. Pass the IStackedBalloonOptions object in a call to [IModelDocExtension::InsertStackedBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html).
5. Select one or more items to add one or more balloons to the stack.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.html)
[IDrawingDoc::CreateAutoBalloonOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAutoBalloonOptions.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
