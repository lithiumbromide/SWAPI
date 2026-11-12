---
title: "IGetSymTextPoints Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetSymTextPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymTextPoints.html"
---

# IGetSymTextPoints Method (IGtol)

Gets the text points for the specified symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSymTextPoints( _
   ByVal SymIdx As System.Short _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
Dim SymIdx As System.Short
Dim value As System.Double

value = instance.IGetSymTextPoints(SymIdx)
```

### C#

```csharp
System.double IGetSymTextPoints(
   System.short SymIdx
)
```

### C++/CLI

```cpp
System.double IGetSymTextPoints(
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

The size of the return array is based on the number of text pieces in this GTol, which you can determine using the return value from [IGtol::IGetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol~IGetSymEdgeCounts.html).

The format of the returned data is an array of doubles:

`retval`[0] - X location of text 1

`retval`[1] - Y location of text 1

`retval`[2] - Z location of text 1

`retval`[3] - X location of text 2

`retval`[4] - Y location of text 2

`retval`[5] - Z location of text 2

`retval`[ (n*3-3)] - X location of text n

`retval`[ (n*3-2)] - Y location of text n

`retval`[ (n*3-1)] - Z location of text n

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
[IGtol::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymArcs.html)
[IGtol::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymCircles.html)
[IGtol::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymLines.html)
[IGtol::IGetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetSymText.html)
