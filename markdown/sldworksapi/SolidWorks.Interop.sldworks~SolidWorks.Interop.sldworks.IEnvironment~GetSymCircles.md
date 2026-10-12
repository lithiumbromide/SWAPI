---
title: "GetSymCircles Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymCircles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymCircles.html"
---

# GetSymCircles Method (IEnvironment)

Gets an array that defines all circles in the geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymCircles( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymCircles(SymId)
```

### C#

```csharp
System.object GetSymCircles(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymCircles(
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

See [Environment::GetSymCircles](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymCircles.html).

## Remarks

Each circle in the geometric tolerance symbol is defined by its radius and center point. The size of the array returned is based on the number of circles within this symbol. You can determine this number using the return value circle count from [IEnvironment::GetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html).

The format of return value is the following array of doubles (in this example, for the `i`th circle):

retval[4 * i] = radius

retval[4 * i + 1] = x coordinate of center point

retval[4 * i + 2] = y coordinate of center point

retval[4 * i + 3] = z coordinate of center point

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[IEnvironment::IGetSymCircles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymCircles.html)
