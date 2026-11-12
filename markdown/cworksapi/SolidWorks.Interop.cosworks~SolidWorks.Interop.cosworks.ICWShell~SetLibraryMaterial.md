---
title: "SetLibraryMaterial Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWShell)

Obsolete. Superseded by [ICWShell::SetLibraryMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterial( _
   ByVal SLibraryPathName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim SLibraryPathName As System.String
Dim SMaterialName As System.String
Dim value As System.Integer

value = instance.SetLibraryMaterial(SLibraryPathName, SMaterialName)
```

### C#

```csharp
System.int SetLibraryMaterial(
   System.string SLibraryPathName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.int SetLibraryMaterial(
   System.String^ SLibraryPathName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibraryPathName`: Path to the material library
- `SMaterialName`: Material name in the library

### Return Value

1 if library material library and name are set, 0 if not

## VBA Syntax

See [CWShell::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~SetLibraryMaterial.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetDefaultMaterial.html)
[ICWShell::GetShellMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetShellMaterial.html)
[ICWShell::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html)
[ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWShell::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
