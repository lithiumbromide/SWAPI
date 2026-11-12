---
title: "InsertNewNote3 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertNewNote3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertNewNote3.html"
---

# InsertNewNote3 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertNewNote3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertNewNote3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertNewNote3( _
   ByVal UpperText As System.String, _
   ByVal NoLeader As System.Boolean, _
   ByVal BentLeader As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderSide As System.Short, _
   ByVal Angle As System.Double, _
   ByVal BalloonStyle As System.Short, _
   ByVal BalloonFit As System.Short, _
   ByVal SmartArrow As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim UpperText As System.String
Dim NoLeader As System.Boolean
Dim BentLeader As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderSide As System.Short
Dim Angle As System.Double
Dim BalloonStyle As System.Short
Dim BalloonFit As System.Short
Dim SmartArrow As System.Boolean

instance.InsertNewNote3(UpperText, NoLeader, BentLeader, ArrowStyle, LeaderSide, Angle, BalloonStyle, BalloonFit, SmartArrow)
```

### C#

```csharp
void InsertNewNote3(
   System.string UpperText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.bool SmartArrow
)
```

### C++/CLI

```cpp
void InsertNewNote3(
   System.String^ UpperText,
   System.bool NoLeader,
   System.bool BentLeader,
   System.short ArrowStyle,
   System.short LeaderSide,
   System.double Angle,
   System.short BalloonStyle,
   System.short BalloonFit,
   System.bool SmartArrow
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperText`:
- `NoLeader`:
- `BentLeader`:
- `ArrowStyle`:
- `LeaderSide`:
- `Angle`:
- `BalloonStyle`:
- `BalloonFit`:
- `SmartArrow`:

## VBA Syntax

See [ModelDoc::InsertNewNote3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertNewNote3.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
