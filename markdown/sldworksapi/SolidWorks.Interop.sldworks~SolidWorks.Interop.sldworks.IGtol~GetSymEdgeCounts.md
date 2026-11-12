---
title: "GetSymEdgeCounts Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetSymEdgeCounts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymEdgeCounts.html"
---

# GetSymEdgeCounts Method (IGtol)

Gets an array of the number of lines, arcs and circles in the specified symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymEdgeCounts( _
   ByVal SymIdx As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Object

value = instance.GetSymEdgeCounts(SymIdx)
```

### C#

```csharp
System.object GetSymEdgeCounts(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.Object^ GetSymEdgeCounts(
   System.short SymIdx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymIdx`: Indexed position of the symbol

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Gtol::GetSymEdgeCounts](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetSymEdgeCounts.html).

## Remarks

Format of return information is the following array of short integers:

`retval`[0] = Line count

`retval`[1] = Arc count

`retval`[2] = Circle count

`retval`[3] = Text count

For more information, see [IGtol::GetSymText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetSymText.html) and [IGtol::GetSymTextPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~GetSymTextPoints.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymArcs.html)
[IGtol::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymCircles.html)
[IGtol::GetSymDesc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymDesc.html)
[IGtol::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymLines.html)
[IGtol::GetSymName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymName.html)
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymCircles.html)
[IGtol::IGetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymEdgeCounts.html)
[IGtol::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html)
[IGtol::IGetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymText.html)
[IGtol::IGetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymTextPoints.html)
