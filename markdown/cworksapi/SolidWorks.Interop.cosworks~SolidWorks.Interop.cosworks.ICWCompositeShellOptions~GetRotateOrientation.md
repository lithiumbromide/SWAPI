---
title: "GetRotateOrientation Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "GetRotateOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetRotateOrientation.html"
---

# GetRotateOrientation Method (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::GetRotateOrientation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetRotateOrientation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotateOrientation( _
   ByVal DispEntity As System.Object, _
   ByRef BRotateOri As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DispEntity As System.Object
Dim BRotateOri As System.Integer
Dim value As System.Integer

value = instance.GetRotateOrientation(DispEntity, BRotateOri)
```

### C#

```csharp
System.int GetRotateOrientation(
   System.object DispEntity,
   out System.int BRotateOri
)
```

### C++/CLI

```cpp
System.int GetRotateOrientation(
   System.Object^ DispEntity,
   [Out] System.int BRotateOri
)
```

### Parameters

- `DispEntity`: Face on which to rotate the ply stripes
- `BRotateOri`: 1 to rotate the stripes by 90°, 0 to not

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::GetRotateOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~GetRotateOrientation.html).

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsSurfaceMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::SetRotateOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetRotateOrientation.html)
[ICWCompositeShellOptions::RotateZeroDegreeReference Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~RotateZeroDegreeReference.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
