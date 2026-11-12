---
title: "SetLibraryMaterial Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWBeamBody)

Obsolete. Superseded by [ICWBeamBody::SetLibraryMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterial( _
   ByVal SLibWithPathName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim SLibWithPathName As System.String
Dim SMaterialName As System.String
Dim value As System.Integer

value = instance.SetLibraryMaterial(SLibWithPathName, SMaterialName)
```

### C#

```csharp
System.int SetLibraryMaterial(
   System.string SLibWithPathName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.int SetLibraryMaterial(
   System.String^ SLibWithPathName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibWithPathName`: Path to the material library
- `SMaterialName`: Material name in the library

### Return Value

1 if material library and library name are set, 0 if not

## VBA Syntax

See [CWBeamBody::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~SetLibraryMaterial.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::GetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetBeamBodyMaterial.html)
[ICWBeamBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetDefaultMaterial.html)
[ICWBeamBody::SetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetBeamBodyMaterial.html)
[ICWBeamBody::ICWMaterial Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMaterial.html)
[ICWBeamBody::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
