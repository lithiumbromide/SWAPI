---
title: "GetIsBound Method (IEnvironment)"
project: "SOLIDWORKS API Help"
interface: "IEnvironment"
member: "GetIsBound"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment~GetIsBound.html"
---

# GetIsBound Method (IEnvironment)

Gets whether the specified geometric tolerance symbol is bound.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetIsBound( _
   ByVal SymId As System.String, _
   ByRef Retval As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEnvironment
Dim SymId As System.String
Dim Retval As System.Boolean

instance.GetIsBound(SymId, Retval)
```

### C#

```csharp
void GetIsBound(
   System.string SymId,
   out System.bool Retval
)
```

### C++/CLI

```cpp
void GetIsBound(
   System.String^ SymId,
   [Out] System.bool Retval
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SymId`: Name of the geometric tolerance symbol formatted as:

  <`LibraryName-SymbolName`>

  where `LibraryName` and `SymbolName` are in the SOLIDWORKS text file **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym****.**

  NOTE: You must include the right- and left-angle brackets and separate `LibraryName` and `SymbolName` with a hyphen; for example, <MOD-DEG>.
- `Retval`: True if the geometric tolerance symbol is bound, false if not

## VBA Syntax

See [Environment::GetIsBound](ms-its:sldworksapivb6.chm::/sldworks~Environment~GetIsBound.html).

## Examples

See the [IEnvironment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html) examples.

## Remarks

Bound controls the horizontal spacing of a geometric tolerance symbol within a row of text in notes and dimensions.

## See Also

[IEnvironment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment.html)
[IEnvironment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnvironment_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
