---
title: "InsertLinearNotePattern Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertLinearNotePattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertLinearNotePattern.html"
---

# InsertLinearNotePattern Method (IDrawingDoc)

Inserts a linear note pattern using the selected [note](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertLinearNotePattern( _
   ByVal NumX As System.Integer, _
   ByVal NumY As System.Integer, _
   ByVal SpacingX As System.Double, _
   ByVal SpacingY As System.Double, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim value As System.Boolean

value = instance.InsertLinearNotePattern(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances)
```

### C#

```csharp
System.bool InsertLinearNotePattern(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances
)
```

### C++/CLI

```cpp
System.bool InsertLinearNotePattern(
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.String^ DeleteInstances
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumX`: Total number of instances along the x axis, including the seed
- `NumY`: Total number of instances along the y axis, including the seed
- `SpacingX`: Spacing between pattern instances along the x axis
- `SpacingY`: Spacing between pattern instances along the y axis
- `AngleX`: Angle for direction 1 relative to the x axis
- `AngleY`: Angle for direction 2 relative to the y axis
- `DeleteInstances`: Number of instances to delete, passed as a string in the format "(a) (b) (c) "

### Return Value

True if the linear note pattern is created, false if not

## VBA Syntax

See [DrawingDoc::InsertLinearNotePattern](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertLinearNotePattern.html).

## Examples

[Insert Linear and Circular Note Patterns (C#)](Insert_Linear_and_Circular_Note_Patterns_Example_CSharp.htm)
[Insert Linear and Circular Note Patterns (VB.NET)](Insert_Linear_and_Circular_Note_Patterns_Example_VBNET.htm)
[Insert Linear and Circular Note Patterns (VBA)](Insert_Linear_and_Circular_Note_Patterns_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertCircularNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCircularNotePattern.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
