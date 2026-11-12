---
title: "AddTo Method (IBalloonStack)"
project: "SOLIDWORKS API Help"
interface: "IBalloonStack"
member: "AddTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack~AddTo.html"
---

# AddTo Method (IBalloonStack)

Adds a balloon note to this balloon stack.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddTo( _
   ByVal UpperTextStyle As System.Integer, _
   ByVal UpperText As System.String, _
   ByVal LowerTextStyle As System.Integer, _
   ByVal LowerText As System.String _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonStack
Dim UpperTextStyle As System.Integer
Dim UpperText As System.String
Dim LowerTextStyle As System.Integer
Dim LowerText As System.String
Dim value As Note

value = instance.AddTo(UpperTextStyle, UpperText, LowerTextStyle, LowerText)
```

### C#

```csharp
Note AddTo(
   System.int UpperTextStyle,
   System.string UpperText,
   System.int LowerTextStyle,
   System.string LowerText
)
```

### C++/CLI

```cpp
Note^ AddTo(
   System.int UpperTextStyle,
   System.String^ UpperText,
   System.int LowerTextStyle,
   System.String^ LowerText
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperTextStyle`: Text style for the text of the balloon as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)
- `UpperText`: Text in the balloon
- `LowerTextStyle`: Text style for the text of the balloon as defined in [swBalloonTextContent_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html)
- `LowerText`: Text in the lower part of the balloon (when Style = swBS_SplitCirc)

### Return Value

[INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html)

## VBA Syntax

See [BalloonStack::AddTo](ms-its:sldworksapivb6.chm::/sldworks~BalloonStack~AddTo.html).

## Examples

[Add Balloon to Stacked Balloon (C#)](Add_Balloon_to_Stacked_Balloon_Example_CSharp.htm)
[Add Balloon to Stacked Balloon (VB.NET)](Add_Balloon_to_Stacked_Balloon_Example_VBNET.htm)
[Add Balloon to Stacked Balloon (VBA)](Add_Balloon_to_Stacked_Balloon_Example_VB.htm)

## Remarks

This method adds a balloon note that is attached to the preselected entity to this stack. It returns an INote object, which you can then use to access the note (for example, to set the font of the note text). The balloon style and size are the same as the initial balloon in this stack.

If the balloon style is split circle, this method uses both the lower and upper text arguments. If the balloon style is anything other than split circle, this method uses the upper text arguments and ignores the lower text arguments.

If the text style is item number or quantity, SOLIDWORKS uses the note text to determine the preselected entity that this note is attached to, and ignores the corresponding text argument. If the preselection is a location on the drawing instead of an entity, you must specify the text style and text.

Use [INote::GetBalloonStack](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote~GetBalloonStack.html) to get a balloon stack interface from an existing note.

## See Also

[IBalloonStack Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack.html)
[IBalloonStack Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html)
[INote::MakeStackedBalloon Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~MakeStackedBalloon.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
