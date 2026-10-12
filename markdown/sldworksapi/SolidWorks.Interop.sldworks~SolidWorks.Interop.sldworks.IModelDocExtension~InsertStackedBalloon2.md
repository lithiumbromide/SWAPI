---
title: "InsertStackedBalloon2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertStackedBalloon2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html"
---

# InsertStackedBalloon2 Method (IModelDocExtension)

Inserts a stack of balloons for selected items.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertStackedBalloon2( _
   ByVal BalloonOptions As StackedBalloonOptions _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim BalloonOptions As StackedBalloonOptions
Dim value As Note

value = instance.InsertStackedBalloon2(BalloonOptions)
```

### C#

```csharp
Note InsertStackedBalloon2(
   StackedBalloonOptions BalloonOptions
)
```

### C++/CLI

```cpp
Note^ InsertStackedBalloon2(
   StackedBalloonOptions^ BalloonOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BalloonOptions`: [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html)

### Return Value

[Note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDocExtension::InsertStackedBalloon2](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~InsertStackedBalloon2.html).

## Examples

[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)
[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)
[Insert BOM Table and Stacked Balloon (C#)](Insert_BOM_Table_and_Stacked_Balloon_Example_CSharp.htm)

## Remarks

To create a stack of balloons:

1. Select an item to insert the first balloon on the stack.
2. Call [IModelDocExtension::CreateStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html) to create an [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) object.
3. Set the properties on the IStackedBalloonOptions object.
4. Call this method using the IStackedBalloonOptions object in the BalloonOptions argument.
5. Select one or more items to add one or more balloons to the stack.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[INote::IsStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsStackedBalloon.html)
[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IModelDocExtension::InsertBOMBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html)
[IDrawingDoc::AutoBalloon5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.html)
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
