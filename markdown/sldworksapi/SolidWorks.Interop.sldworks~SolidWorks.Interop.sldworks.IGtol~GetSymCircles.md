---
title: "GetSymCircles Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetSymCircles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymCircles.html"
---

# GetSymCircles Method (IGtol)

Gets an array that defines all circles in the symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymCircles( _
   ByVal SymIdx As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Object

value = instance.GetSymCircles(SymIdx)
```

### C#

```csharp
System.object GetSymCircles(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.Object^ GetSymCircles(
   System.short SymIdx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymIdx`: Indexed position of the symbol

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetSymCircles](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetSymCircles.html).

## Remarks

Each circle in the symbol is defined by its radius and center point.

Format of return information is the following array of doubles.

For the `i`th circle:

`retval`[4 * `i`] = radius

`retval`[4 * `i` + 1] = X-coordinate of center point

`retval`[4 * `i` + 2] = Y-coordinate of center point

`retval`[4 * `i` + 3] = Z-coordinate of center point

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymArcs.html)
[IGtol::GetSymDesc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymDesc.html)
[IGtol::GetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymEdgeCounts.html)
[IGtol::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymLines.html)
[IGtol::GetSymName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymName.html)
[IGtol::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymText.html)
[IGtol::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymTextPoints.html)
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymCircles.html)
[IGtol::IGetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymEdgeCounts.html)
[IGtol::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html)
[IGtol::IGetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymText.html)
[IGtol::IGetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymTextPoints.html)
