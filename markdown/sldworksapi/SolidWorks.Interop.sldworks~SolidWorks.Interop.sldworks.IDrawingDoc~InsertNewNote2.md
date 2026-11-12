---
title: "InsertNewNote2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertNewNote2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote2.html"
---

# InsertNewNote2 Method (IDrawingDoc)

Creates a new note in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertNewNote2( _
   ByVal UpperText As System.String, _
   ByVal LowerText As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short, _
   ByVal Angle As System.Double, _
   ByVal BalloonStyle As System.Short, _
   ByVal BalloonFit As System.Short, _
   ByVal UpperNoteContent As System.Short, _
   ByVal LowerNoteContent As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim UpperText As System.String
Dim LowerText As System.String
Dim NoLeader As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short
Dim Angle As System.Double
Dim BalloonStyle As System.Short
Dim BalloonFit As System.Short
Dim UpperNoteContent As System.Short
Dim LowerNoteContent As System.Short

instance.InsertNewNote2(UpperText, LowerText, NoLeader, BentLeader, ArrowStyle, LeaderSide, Angle, BalloonStyle, BalloonFit, UpperNoteContent, LowerNoteContent)
```

### C#

```csharp
void InsertNewNote2(
   System.string UpperText,
   System.string LowerText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.short UpperNoteContent,
   System.short LowerNoteContent
)
```

### C++/CLI

```cpp
void InsertNewNote2(
   System.String^ UpperText,
   System.String^ LowerText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.short UpperNoteContent,
   System.short LowerNoteContent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperText`: Upper text string to be put in the note
- `LowerText`: Unused; pass an empty string
- `NoLeader`: True does not add a leader line, false does
- `BentLeader`: True adds a bent leader line, false does not
- `ArrowStyle`: Arrowhead type as defined in [swArrowStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)
- `LeaderSide`: Leader line side as defined in [swLeaderSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)
- `Angle`: Text angle
- `BalloonStyle`: Balloon style type as defined in [swBalloonStyle_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html)
- `BalloonFit`: Balloon fit type as defined in [swBalloonFit_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html)
- `UpperNoteContent`: Unused; set to 0
- `LowerNoteContent`: Unused; set to 0

## VBA Syntax

See [DrawingDoc::InsertNewNote2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertNewNote2.html).

## Examples

Contact SOLIDWORKS API Support to obtain **Insert Note Leader at Sketch Point (VBA, VB.NET, and C#)**.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::CreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateCompoundNote.html)
[IDrawingDoc::CreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateText2.html)
[IDrawingDoc::ICreateCompoundNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateCompoundNote.html)
[IDrawingDoc::ICreateText2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateText2.html)
[IDrawingDoc::NewNote Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewNote.html)
[IDrawingDoc::InsertRevisionSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertRevisionSymbol.html)
[IDrawingDoc::InsertCircularNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCircularNotePattern.html)
[IDrawingDoc::InsertLinearNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertLinearNotePattern.html)
