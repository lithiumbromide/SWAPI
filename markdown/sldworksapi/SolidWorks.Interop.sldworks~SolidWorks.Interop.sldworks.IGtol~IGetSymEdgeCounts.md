---
title: "IGetSymEdgeCounts Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetSymEdgeCounts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymEdgeCounts.html"
---

# IGetSymEdgeCounts Method (IGtol)

Gets an array of the number of lines, arcs and circles in the specified symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSymEdgeCounts( _
   ByVal SymIdx As System.Short _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Short

value = instance.IGetSymEdgeCounts(SymIdx)
```

### C#

```csharp
System.short IGetSymEdgeCounts(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.short IGetSymEdgeCounts(
   System.short SymIdx
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymIdx`: Indexed position of the symbol

### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Format of return information is the following array of short integers:

`retval`[0] = Line count

`retval`[1] = Arc count

`retval`[2] = Circle count

`retval`[3] = Text count

For more information, see [IGtol::IGetSymText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IGetSymText.html) and [IGtol::IGetSymTextPoints](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IGetSymTextPoints.html).

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymArcs.html)
[IGtol::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymCircles.html)
[IGtol::GetSymDesc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymDesc.html)
[IGtol::GetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymEdgeCounts.html)
[IGtol::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymLines.html)
[IGtol::GetSymName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymName.html)
[IGtol::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymText.html)
[IGtol::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetSymTextPoints.html)
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymCircles.html)
[IGtol::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html)
