---
title: "IGetLineAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.html"
---

# IGetLineAtIndex Method (IGtol)

Gets the start and end information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: 0-based index of the line

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles:

```vb
[ lineType, startPt[3], endPt[3] ]
```

where:

- lineType = the [line type](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html)
- startPt[3] = the XYZ line start point
- endPt[3] = the XYZ line end point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLineAtIndex.html)
[IGtol::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLineCount.html)
