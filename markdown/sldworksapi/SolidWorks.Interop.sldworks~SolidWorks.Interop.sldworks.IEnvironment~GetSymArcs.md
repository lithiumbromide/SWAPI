---
title: "GetSymArcs Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymArcs"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs.html"
---

# GetSymArcs Method (IEnvironment)

Obsolete. Superseded by [IEnvironment::GetSymArcs2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymArcs( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymArcs(SymId)
```

### C#

```csharp
System.object GetSymArcs(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymArcs(
   System.String^ SymId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymId`: Name of the geometric tolerance symbol formatted as:

  <LibraryName-SymbolName>

  where LibraryName and SymbolName are a [pre-defined SOLIDWORKS symbol](sldworksAPIProgGuide.chm::/Miscellaneous/Geometric_Tolerance_Symbol_Libraries.htm) in the SOLIDWORKS text file **gtol.sym**, typically installed at **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english****.**

  NOTE: You must include the right- and left-angle brackets and separate LibraryName and SymbolName with a hyphen; for example, <MOD-DEG>.

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [Environment::GetSymArcs](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymArcs.html).

## Remarks

Each arc in the geometric tolerance symbol is defined by three points (center, arc start, and end). The size of the array returned is based on the number of arcs within this geometric tolerance symbol. You can determine this number using the return value arc count from [IEnvironment::GetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html).

The format of return value is the following array of doubles (in this example, for the `i`th arc):

retval[9 * i + 0] = x coordinate of center point

retval[9 * i + 1] = y coordinate of center point

retval[9 * i + 2] = z coordinate of center point

retval[9 * i + 3] = x coordinate of arc start point

retval[9 * i + 4] = y coordinate of arc start point

retval[9 * i + 5] = z coordinate of arc start point

retval[9 * i + 6] = x coordinate of arc end point

retval[9 * i + 7] = y coordinate of arc end point

retval[9 * i + 8] = z coordinate of arc end point

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[IEnvironment::IGetSymArcs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymArcs.html)
