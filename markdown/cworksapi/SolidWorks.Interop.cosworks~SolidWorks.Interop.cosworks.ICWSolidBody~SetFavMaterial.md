---
title: "SetFavMaterial Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SetFavMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetFavMaterial.html"
---

# SetFavMaterial Method (ICWSolidBody)

Obsolete. Superseded by [ICWSolidBody::SetFavMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetFavMaterial2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavMaterial( _
   ByVal NFav As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim NFav As System.Integer
Dim value As System.Integer

value = instance.SetFavMaterial(NFav)
```

### C#

```csharp
System.int SetFavMaterial(
   System.int NFav
)
```

### C++/CLI

```cpp
System.int SetFavMaterial(
   System.int NFav
)
```

### Parameters

- `NFav`: 1 <= index of material in favorites list <= 100 (see **Remarks**)

### Return Value

0 if material applied successfully, 1 if not

## VBA Syntax

See [CWSolidBody::SetFavMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~SetFavMaterial.html).

## Remarks

The list of material favorites appears when you right-click a component in the Simulation study tree and click **Apply Favorite Material**.

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWSolidBody::SetSolidBodyMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetSolidBodyMaterial.html)
[ICWSolidBody::SetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
