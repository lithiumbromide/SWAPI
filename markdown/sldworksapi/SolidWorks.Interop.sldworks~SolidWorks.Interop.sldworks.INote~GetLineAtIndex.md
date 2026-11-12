---
title: "GetLineAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineAtIndex.html"
---

# GetLineAtIndex Method (INote)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineAtIndex(Index)
```

### C#

```csharp
System.object GetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Zero-based index of the desired line

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Note::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Note~GetLineAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3]

where:

| lineType | = the line type. Refer to the swLineTypes_e enumeration. |
| --- | --- |
| startPt [3] | = the XYZ line start point |
| endPt [3] | = the XYZ line end point |

The data returned from this method is in terms of document space. If the document containing this note is a drawing, then the coordinates returned are based on the sheet origin. If the document is a part or assembly, then the coordinates are based on the model origin.

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineCount.html)
[INote::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLineAtIndex.html)
