---
title: "InsertNewNote Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertNewNote"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertNewNote.html"
---

# InsertNewNote Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertNewNote2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertNewNote2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertNewNote( _
   ByVal Text As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BalloonNote As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Text As System.String
Dim NoLeader As System.Boolean
Dim BalloonNote As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short

instance.InsertNewNote(Text, NoLeader, BalloonNote, BentLeader, ArrowStyle, LeaderSide)
```

### C#

```csharp
void InsertNewNote(
   System.string Text,
   System.bool NoLeader,
   System.bool BalloonNote,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide
)
```

### C++/CLI

```cpp
void InsertNewNote(
   System.String^ Text,
   System.bool NoLeader,
   System.bool BalloonNote,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`:
- `NoLeader`:
- `BalloonNote`:
- `BentLeader`:
- `ArrowStyle`:
- `LeaderSide`:

## VBA Syntax

See [DrawingDoc::InsertNewNote](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertNewNote.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
