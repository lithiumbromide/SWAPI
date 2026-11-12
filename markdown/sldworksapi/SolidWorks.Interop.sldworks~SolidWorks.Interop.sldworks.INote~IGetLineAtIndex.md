---
title: "IGetLineAtIndex Method (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IGetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IGetLineAtIndex.html"
---

# IGetLineAtIndex Method (INote)

Gets information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetLineAtIndex(Index)
```

### C#

```csharp
System.double IGetLineAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetLineAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired line where the index begins at 0

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[INote::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineAtIndex.html)
[INote::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetLineCount.html)
