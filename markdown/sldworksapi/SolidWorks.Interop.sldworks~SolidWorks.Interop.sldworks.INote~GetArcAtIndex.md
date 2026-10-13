---
title: "GetArcAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcAtIndex.html"
---

# GetArcAtIndex Method (INote)

Gets information for the specified arc in this note.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArcAtIndex(Index)
```

### C#

```csharp
System.object GetArcAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArcAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired arc where the index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Note::GetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetArcAtIndex.html).

## Remarks

Return value is an array of doubles:

[ LineType, StartPt[3], EndPt[3], CenterPt[3], RotDir ]

where :

| LineType | Line type. Valid returns are defined in swLineTypes_e . A LineType is a combination of a line style and line weight. |
| --- | --- |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the start point. |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the end point. If the arc is closed, then this is the same point as the StartPt . |
| CenterPt[3] | Array of 3 doubles (X,Y,Z) describing the center point. |
| RotDir | Rotational direction (CW = -1, CCW = 1) |

The data returned from this method is in terms of document apace.

| If the document containing this note is... | Then the coordinates returned are based on the... |
| --- | --- |
| Drawing | Sheet origin |
| Part or assembly | Model origin |

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetArcAtIndex.html)
[INote::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetArcCount.html)
