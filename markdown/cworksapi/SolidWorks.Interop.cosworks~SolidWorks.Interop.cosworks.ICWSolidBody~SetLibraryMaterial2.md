---
title: "SetLibraryMaterial2 Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "SetLibraryMaterial2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial2.html"
---

# SetLibraryMaterial2 Method (ICWSolidBody)

Sets the material library for the solid body.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterial2( _
   ByVal SLibWithPathName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim SLibWithPathName As System.String
Dim SMaterialName As System.String
Dim value As System.Boolean

value = instance.SetLibraryMaterial2(SLibWithPathName, SMaterialName)
```

### C#

```csharp
System.bool SetLibraryMaterial2(
   System.string SLibWithPathName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.bool SetLibraryMaterial2(
   System.String^ SLibWithPathName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibWithPathName`: Path to the material library folder
- `SMaterialName`: Material name

### Return Value

-1 or true if material library and name are set, 0 or false if not

## Examples

See the [ICWSolidBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html) examples.

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
