---
title: "IGetSymEdgeCounts Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "IGetSymEdgeCounts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymEdgeCounts.html"
---

# IGetSymEdgeCounts Method (IEnvironment)

Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSymEdgeCounts( _
   ByVal SymId As System.String _
) As System.Short
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Short

value = instance.IGetSymEdgeCounts(SymId)
```

### C#

```csharp
System.short IGetSymEdgeCounts(
   System.string SymId
)
```

### C++/CLI

```cpp
System.short IGetSymEdgeCounts(
   System.String^ SymId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymId`: Name of the geometric tolerance symbol formatted as:

  <`LibraryName-SymbolName`>

  where `LibraryName` and `SymbolName` are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.**

  NOTE: You must include the right- and left-angle brackets and separate `LibraryName` and `SymbolName` with a hyphen; for example, <MOD-DEG>.

### Return Value

- in-process, unmanaged C++: Pointer to an array of shorts (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Format of return information is the following array of short integers:

retval[0] = line count

retval[1] = arc count

retval[2] = circle count

retval[3] = text count

retval[4] = triangle count

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[IEnvironment::GetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html)
[IEnvironment::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymArcs.html)
[IEnvironment::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymCircles.html)
[IEnvironment::IGetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymLines.html)
[IEnvironment::IGetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTextPoints.html)
[IEnvironment::IGetSymTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTriangles.html)
