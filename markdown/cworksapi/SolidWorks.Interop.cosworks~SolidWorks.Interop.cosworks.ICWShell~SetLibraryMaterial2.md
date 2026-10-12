---
title: "SetLibraryMaterial2 Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "SetLibraryMaterial2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial2.html"
---

# SetLibraryMaterial2 Method (ICWShell)

Sets the material library and material name for the shell.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterial2( _
   ByVal SLibraryPathName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim SLibraryPathName As System.String
Dim SMaterialName As System.String
Dim value As System.Boolean

value = instance.SetLibraryMaterial2(SLibraryPathName, SMaterialName)
```

### C#

```csharp
System.bool SetLibraryMaterial2(
   System.string SLibraryPathName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.bool SetLibraryMaterial2(
   System.String^ SLibraryPathName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibraryPathName`: Path to the material library
- `SMaterialName`: Material name in the library

### Return Value

-1 or true if library material library and name are set, 0 or false if not

## Examples

See the [ICWShell](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html) examples.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
