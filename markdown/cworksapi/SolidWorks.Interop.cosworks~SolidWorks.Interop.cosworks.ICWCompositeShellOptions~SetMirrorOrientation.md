---
title: "SetMirrorOrientation Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "SetMirrorOrientation"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetMirrorOrientation.html"
---

# SetMirrorOrientation Method (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::SetMirrorOrientation2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetMirrorOrientation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMirrorOrientation( _
   ByVal DispEntity As System.Object, _
   ByVal BMirrorOri As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DispEntity As System.Object
Dim BMirrorOri As System.Integer
Dim value As System.Integer

value = instance.SetMirrorOrientation(DispEntity, BMirrorOri)
```

### C#

```csharp
System.int SetMirrorOrientation(
   System.object DispEntity,
   System.int BMirrorOri
)
```

### C++/CLI

```cpp
System.int SetMirrorOrientation(
   System.Object^ DispEntity,
   System.int BMirrorOri
)
```

### Parameters

- `DispEntity`: Face to which material orientation is applied
- `BMirrorOri`: 0 for clockwise ply angle direction, 1 for counter-clockwise ply angle direction

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::SetMirrorOrientation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~SetMirrorOrientation.html).

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsSurfaceMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetMirrorOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetMirrorOrientation.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
