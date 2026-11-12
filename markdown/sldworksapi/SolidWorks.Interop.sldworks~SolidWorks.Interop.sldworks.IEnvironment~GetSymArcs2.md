---
title: "GetSymArcs2 Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymArcs2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymArcs2.html"
---

# GetSymArcs2 Method (IEnvironment)

Gets an array of information about all arcs in the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymArcs2( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymArcs2(SymId)
```

### C#

```csharp
System.object GetSymArcs2(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymArcs2(
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

See [Environment::GetSymArcs2](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymArcs2.html).

## Examples

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html) examples.

## Remarks

Each arc in the geometric tolerance symbol is defined by three points (center, arc start, and arc end), whether the arc is filled, and whether the chord joining the start and end points is drawn. The size of the array returned is based on the number of arcs within this geometric tolerance symbol. You can determine this number by calling [IEnvironment::GetSymEdgeCounts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html).

The return value contains the following array for each arc:

[ x coordinate of center point,

y coordinate of center point,

z coordinate of center point,

x coordinate of start point,

y coordinate of start point,

z coordinate of start point,

x coordinate of end point,

y coordinate of end point,

z coordinate of end point,

whether arch is filled,

whether the chord joining the start and end points is drawn ]

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)

## Availability

SOLIDWORKS 2015 SP01, Revision Number 23.1
