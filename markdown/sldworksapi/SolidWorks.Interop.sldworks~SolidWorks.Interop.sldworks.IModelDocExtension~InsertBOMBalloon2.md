---
title: "InsertBOMBalloon2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertBOMBalloon2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertBOMBalloon2.html"
---

# InsertBOMBalloon2 Method (IModelDocExtension)

Inserts a BOM balloon for the selected item.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBOMBalloon2( _
   ByVal BalloonOptions As BalloonOptions _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim BalloonOptions As BalloonOptions
Dim value As Note

value = instance.InsertBOMBalloon2(BalloonOptions)
```

### C#

```csharp
Note InsertBOMBalloon2(
   BalloonOptions BalloonOptions
)
```

### C++/CLI

```cpp
Note^ InsertBOMBalloon2(
   BalloonOptions^ BalloonOptions
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BalloonOptions`: [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html)

### Return Value

[Note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [ModelDocExtension::InsertBOMBalloon2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertBOMBalloon2.html).

## Examples

[Insert and Show BOM Table and BOM Balloon (VBA)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VB.htm)
[Insert and Show BOM Table and BOM Balloon (VB.NET)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_VBNET.htm)
[Insert and Show BOM Table and BOM Balloon (C#)](Insert_and_Show_BOM_Table_and_BOM_Balloon_Example_CSharp.htm)

## Remarks

To create a single BOM balloon:

1. Select an item for which to create a BOM balloon.
2. Call [IModelDocExtension::CreateBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateBalloonOptions.html) to create an [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) object.
3. Set the properties on the IBalloonOptions object.
4. Call this method using the IBalloonOptions object in the BalloonOptions argument.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::InsertStackedBalloon2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html)
[IDrawingDoc::AutoBalloon5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon5.html)
[INote::GetBalloonOptions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBalloonOptions.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
