---
title: "SetLibraryMaterial Method (ICWLinkageRod)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLinkageRod"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWLinkageRod)

Sets the specified library material for this linkage rod connector.

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
Dim instance As ICWLinkageRod
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

- `SMaterialLibPathWithName`: Material library path name
- `SMaterialName`: Material name

## VBA Syntax

See [CWLinkageRod::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLinkageRod~SetLibraryMaterial.html).

## Examples

See the [ICWLinkageRod](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html) examples

## See Also

[ICWLinkageRod Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod.html)
[ICWLinkageRod Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLinkageRod_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
