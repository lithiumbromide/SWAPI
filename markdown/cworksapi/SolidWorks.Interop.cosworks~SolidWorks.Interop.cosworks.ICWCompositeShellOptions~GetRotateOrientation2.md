---
title: "GetRotateOrientation2 Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "GetRotateOrientation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetRotateOrientation2.html"
---

# GetRotateOrientation2 Method (ICWCompositeShellOptions)

Gets whether to rotate the stripes by 90° along the surface of the ply of the specified face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRotateOrientation2( _
   ByVal DispEntity As System.Object, _
   ByRef BRotateOri As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DispEntity As System.Object
Dim BRotateOri As System.Boolean
Dim value As System.Integer

value = instance.GetRotateOrientation2(DispEntity, BRotateOri)
```

### C#

```csharp
System.int GetRotateOrientation2(
   System.object DispEntity,
   out System.bool BRotateOri
)
```

### C++/CLI

```cpp
System.int GetRotateOrientation2(
   System.Object^ DispEntity,
   [Out] System.bool BRotateOri
)
```

### Parameters

- `DispEntity`: Face on which to rotate the ply stripes
- `BRotateOri`: -1 or true to rotate the stripes by 90°, 0 or false to not

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsSurfaceMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
