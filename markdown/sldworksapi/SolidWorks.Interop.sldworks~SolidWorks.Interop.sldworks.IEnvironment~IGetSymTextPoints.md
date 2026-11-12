---
title: "IGetSymTextPoints Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "IGetSymTextPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTextPoints.html"
---

# IGetSymTextPoints Method (IEnvironment)

Gets an array that defines all text points in the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSymTextPoints( _
   ByVal SymId As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Double

value = instance.IGetSymTextPoints(SymId)
```

### C#

```csharp
System.double IGetSymTextPoints(
   System.string SymId
)
```

### C++/CLI

```cpp
System.double IGetSymTextPoints(
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

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The size of the array returned is based on the number of text pieces within this geometric tolerance symbol. You can determine this number using the return value text count from [IEnvironment::IGetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment~IGetSymEdgeCounts.html).

The return value is an array of doubles as follows:

retval[0] x coordinate of text 1

retval[1] y coordinate of text 1

retval[2] z coordinate of text 1

retval[3] x coordinate of text 2

retval[4] y coordinate of text 2

retval[5] z coordinate of text 2

retval[ (n*3-3)] X coordinate of text n

retval[ (n*3-2)] Y coordinate of text n

retval[ (n*3-1)] Z coordinate of text n

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
[IEnvironment::GetSymTextPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~IGetSymTextPoints.html)
