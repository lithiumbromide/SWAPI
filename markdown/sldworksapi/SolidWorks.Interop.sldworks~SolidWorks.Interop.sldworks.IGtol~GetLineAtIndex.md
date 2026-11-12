---
title: "GetLineAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetLineAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLineAtIndex.html"
---

# GetLineAtIndex Method (IGtol)

Gets the start and end information for the specified line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: Index of the desired line where the index begins at zero

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Gtol::GetLineAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetLineAtIndex.html).

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
[IGtol::GetLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetLineCount.html)
[IGtol::IGetLineAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetLineAtIndex.html)
