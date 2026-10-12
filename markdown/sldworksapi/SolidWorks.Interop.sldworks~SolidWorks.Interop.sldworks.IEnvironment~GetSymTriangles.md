---
title: "GetSymTriangles Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymTriangles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymTriangles.html"
---

# GetSymTriangles Method (IEnvironment)

Gets an array that defines all triangles in the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymTriangles( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymTriangles(SymId)
```

### C#

```csharp
System.object GetSymTriangles(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymTriangles(
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

See [Environment::GetSymTriangles](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymTriangles.html).

## Remarks

The size of the array returned by this method is based on the number of triangles in this geometric tolerance symbol. You can determine this number using the return value triangle count from [IEnvironment::GetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html).

The format of the returned data is an array of doubles:

retval[0] x coordinate of triangle point 1

retval[1] y coordinate of triangle point 1

retval[2] z coordinate of triangle point 1

retval[3] x coordinate of triangle point 2

retval[4] y coordinate of triangle point 2

retval[5] z coordinate of triangle point 2

retval[6] x coordinate of triangle point 3

retval[7] y coordinate of triangle point 3

retval[8] z coordinate of triangle point 3

retval[9] Boolean returned as a double that describes if the triangle is filled

retval[10] describes the [line type](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineTypes_e.html) of the triangle

where this set of data repeats itself for each triangle in the specified geometric tolerance symbol.

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[IEnvironment::IGetSymTriangles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTriangles.html)
