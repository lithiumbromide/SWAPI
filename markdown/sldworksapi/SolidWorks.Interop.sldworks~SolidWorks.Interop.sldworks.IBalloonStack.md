---
title: "IBalloonStack Interface"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html"
---

# IBalloonStack Interface

Allows access to the properties that apply to a balloon stack, such as the direction of the stack.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IBalloonStack
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
```

### C#

```csharp
public interface IBalloonStack
```

### C++/CLI

```cpp
public interface class IBalloonStack
```

## VBA Syntax

See [BalloonStack](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack.html).

## Examples

[Add Balloon to Stacked Balloon (C#)](Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm)
[Add Balloon to Stacked Balloon (VB.NET)](Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm)
[Add Balloon to Stacked Balloon (VBA)](Add_Balloon_to_Stacked_Balloon_Example_VB.htm)

## Remarks

Each of the notes in a balloon stack are individual notes. You must use the [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) interface to get and set properties of individual notes, such as the text itself.

## Accessors

[INote::GetBalloonStack Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetBalloonStack.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonStack|c310'

## Access Diagram

[BalloonStack](SWObjectModel.pdf#BalloonStack)

## See Also

[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::InsertStackedBalloon Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertStackedBalloon.html)
