---
title: "GetSymText Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetSymText"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetSymText.html"
---

# GetSymText Method (IEnvironment)

Gets an array containing the text associated with the specified geometric tolerance symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSymText( _
   ByVal SymId As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim value As System.Object

value = instance.GetSymText(SymId)
```

### C#

```csharp
System.object GetSymText(
   System.string SymId
)
```

### C++/CLI

```cpp
System.Object^ GetSymText(
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

See [Environment::GetSymText](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetSymText.html).

## Remarks

You can use [IEnvironment::GetSymEdgeCounts](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnvironment~GetSymEdgeCounts.html) to determine how many text strings are in the specified geometric tolerance symbol. For example, passing <MOD-MMC> in SymID returns one text string ("M") and one circle.

The format of the return data is an array of strings. The size of the array returned is based on the number of text pieces in this symbol.

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)
