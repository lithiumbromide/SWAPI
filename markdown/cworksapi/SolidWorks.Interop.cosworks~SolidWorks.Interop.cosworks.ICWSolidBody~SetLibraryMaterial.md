---
title: "SetLibraryMaterial Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWSolidBody)

Obsolete. Superseded by [ICWSolidBody::SetLibraryMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial2.html).

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
Dim instance As ICWSolidBody
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

- `SLibWithPathName`: Path to the material library folder
- `SMaterialName`: Material name

### Return Value

0 if material library and name are set, 1 if not

## VBA Syntax

See [CWSolidBody::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~SetLibraryMaterial.html).

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWSolidBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetDefaultMaterial.html)
[ICWSolidBody::GetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetSolidBodyMaterial.html)
[ICWSolidBody::SetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetSolidBodyMaterial.html)
[ICWSolidBody::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
