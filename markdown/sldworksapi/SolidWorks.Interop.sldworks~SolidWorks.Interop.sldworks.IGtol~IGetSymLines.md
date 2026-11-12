---
title: "IGetSymLines Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetSymLines"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html"
---

# IGetSymLines Method (IGtol)

Gets an array that defines all lines in the symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSymLines( _
   ByVal SymIdx As System.Short _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Double

value = instance.IGetSymLines(SymIdx)
```

### C#

```csharp
System.double IGetSymLines(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.double IGetSymLines(
   System.short SymIdx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymIdx`: Indexed position of the symbol

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Each line in the symbol is defined by two points.

Format of return information is the following array of doubles:

For the `i`th line:

`retval`[6 * `i` + 0] = X-coordinate of first point

`retval`[6 * `i` + 1] = Y-coordinate of first point

`retval`[6 * `i` + 2] = Z-coordinate of first point

`retval`[6 * `i` + 3] = X-coordinate of second point

`retval`[6 * `i` + 4] = Y-coordinate of second point

`retval`[6 * `i` + 5] = Z-coordinate of second point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymArcs.html)
[IGtol::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymCircles.html)
[IGtol::GetSymDesc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymDesc.html)
[IGtol::GetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymEdgeCounts.html)
[IGtol::GetSymName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymName.html)
[IGtol::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymText.html)
[IGtol::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymTextPoints.html)
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymCircles.html)
[IGtol::IGetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymEdgeCounts.html)
[IGtol::IGetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymText.html)
[IGtol::IGetTextPositionAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetTextPositionAtIndex.html)
