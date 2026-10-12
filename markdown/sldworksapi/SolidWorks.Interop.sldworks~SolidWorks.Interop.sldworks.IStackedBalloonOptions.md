---
title: "IStackedBalloonOptions Interface"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html"
---

# IStackedBalloonOptions Interface

Allows access to stacked balloon options.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IStackedBalloonOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
```

### C#

```csharp
public interface IStackedBalloonOptions
```

### C++/CLI

```cpp
public interface class IStackedBalloonOptions
```

## VBA Syntax

See [StackedBalloonOptions](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions.html).

## Examples

[Insert BOM Table and Stacked Balloon (C#)](Insert_BOM_Table_and_Stacked_Balloon_Example_CSharp.htm)
[Insert BOM Table and Stacked Balloon (VB.NET)](Insert_BOM_Table_and_Stacked_Balloon_Example_VBNET.htm)
[Insert BOM Table and Stacked Balloon (VBA)](Insert_BOM_Table_and_Stacked_Balloon_Example_VB.htm)

## Remarks

To create a stack of balloons:

1. Select an item to create the first balloon in the stack.
2. Call [IModelDocExtension::CreateStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html) to create an IStackedBalloonOptions object.
3. Set the properties on the IStackedBalloonOptions object.
4. Pass the IStackedBalloonOptions object in a call to [IModelDocExtension::InsertStackedBalloon2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertStackedBalloon2.html).
5. Select one or more items to add to the stack.

## Accessors

[IModelDocExtension::CreateStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateStackedBalloonOptions.html)

## Access Diagram

[StackedBalloonOptions](SWObjectModel.pdf#StackedBalloonOptions)

## See Also

[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.html)
