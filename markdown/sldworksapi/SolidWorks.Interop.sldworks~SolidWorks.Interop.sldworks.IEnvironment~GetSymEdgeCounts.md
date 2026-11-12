---
title: "GetSymEdgeCounts Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymEdgeCounts"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html"
---

# GetSymEdgeCounts Method (IEnvironment)

Gets an array that contains the number of lines, arcs, circles, text strings, and triangles in the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymEdgeCounts( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymEdgeCounts(SymId)
```

### C#

```csharp
System.object GetSymEdgeCounts(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymEdgeCounts(
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

Array (see **Remarks**)

## VBA Syntax

See [Environment::GetSymEdgeCounts](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymEdgeCounts.html).

## Examples

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html) examples.

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
[IEnvironment::IGetSymEdgeCounts Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymEdgeCounts.html)
[IEnvironment::GetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs.html)
[IEnvironment::GetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymCircles.html)
[IEnvironment::GetSymLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymLines.html)
[IEnvironment::GetSymText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymText.html)
[IEnvironment::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymTextPoints.html)
[IEnvironment::GetSymTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTriangles.html)
