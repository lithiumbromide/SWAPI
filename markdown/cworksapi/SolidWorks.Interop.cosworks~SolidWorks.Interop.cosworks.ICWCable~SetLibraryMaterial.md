---
title: "SetLibraryMaterial Method (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWCable)

Sets the material for this cable.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLibraryMaterial( _
   ByVal SMaterialLibPathWithName As System.String, _
   ByVal SMaterialName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable
Dim SMaterialLibPathWithName As System.String
Dim SMaterialName As System.String

instance.SetLibraryMaterial(SMaterialLibPathWithName, SMaterialName)
```

### C#

```csharp
void SetLibraryMaterial(
   System.string SMaterialLibPathWithName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
void SetLibraryMaterial(
   System.String^ SMaterialLibPathWithName,
   System.String^ SMaterialName
)
```

### Parameters

- `SMaterialLibPathWithName`: Full pathname of the material library (see **Remarks**)
- `SMaterialName`: Name of material in the library

## VBA Syntax

See [CWCable::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~SetLibraryMaterial.html).

## Examples

See the [ICWCable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html) example.

## Remarks

The material library is `install_dir`**\lang\**`lang`**\sldmaterials\solidworks materials.sldmat**.

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
