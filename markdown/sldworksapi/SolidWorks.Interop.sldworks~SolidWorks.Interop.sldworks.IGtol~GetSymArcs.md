---
title: "GetSymArcs Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetSymArcs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymArcs.html"
---

# GetSymArcs Method (IGtol)

Gets an array that defines all arcs in the symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymArcs( _
   ByVal SymIdx As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Object

value = instance.GetSymArcs(SymIdx)
```

### C#

```csharp
System.object GetSymArcs(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.Object^ GetSymArcs(
   System.short SymIdx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymIdx`: Indexed position of the symbol

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetSymArcs](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetSymArcs.html).

## Remarks

Each arc in the symbol is defined by three points: center, arc start, and arc end.

Format of return information is the following array of doubles:

For the `i`th arc:

`retval`[9 * `i` + 0] = X-coordinate of center point

`retval`[9 * `i` + 1] = Y-coordinate of center point

`retval`[9 * `i` + 2] = Z-coordinate of center point

`retval`[9 * `i` + 3] = X-coordinate of arc start point

`retval`[9 * `i` + 4] = Y-coordinate of arc start point

`retval`[9 * `i` + 5] = Z-coordinate of arc start point

`retval`[9 * `i` + 6] = X-coordinate of arc end point

`retval`[9 * `i` + 7] = Y-coordinate of arc end point

`retval`[9 * `i` + 8] = Z-coordinate of arc end point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymCircles.html)
[IGtol::GetSymDesc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymDesc.html)
[IGtol::GetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymEdgeCounts.html)
[IGtol::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymLines.html)
[IGtol::GetSymName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymName.html)
[IGtol::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymText.html)
[IGtol::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymTextPoints.html)
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html)
[IGtol::IGetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymText.html)
[IGtol::IGetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymTextPoints.html)
