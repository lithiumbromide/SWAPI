---
title: "SetRotateOrientation Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "SetRotateOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetRotateOrientation.html"
---

# SetRotateOrientation Method (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::SetRotateOrientation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetRotateOrientation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRotateOrientation( _
   ByVal DispEntity As System.Object, _
   ByVal BRotateOri As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DispEntity As System.Object
Dim BRotateOri As System.Integer
Dim value As System.Integer

value = instance.SetRotateOrientation(DispEntity, BRotateOri)
```

### C#

```csharp
System.int SetRotateOrientation(
   System.object DispEntity,
   System.int BRotateOri
)
```

### C++/CLI

```cpp
System.int SetRotateOrientation(
   System.Object^ DispEntity,
   System.int BRotateOri
)
```

### Parameters

- `DispEntity`: Face on which to rotate the ply stripes
- `BRotateOri`: 1 to rotate the stripes by 90°, 0 to not

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::SetRotateOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~SetRotateOrientation.html).

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsSurfaceMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetRotateOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetRotateOrientation.html)
[ICWCompositeShellOptions::RotateZeroDegreeReference Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~RotateZeroDegreeReference.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
