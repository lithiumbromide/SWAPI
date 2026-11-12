---
title: "GetMirrorOrientation2 Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "GetMirrorOrientation2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetMirrorOrientation2.html"
---

# GetMirrorOrientation2 Method (ICWCompositeShellOptions)

Gets the ply angle mirror orientation of this composite shell.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMirrorOrientation2( _
   ByVal DispEntity As System.Object, _
   ByRef BMirrorOri As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DispEntity As System.Object
Dim BMirrorOri As System.Boolean
Dim value As System.Integer

value = instance.GetMirrorOrientation2(DispEntity, BMirrorOri)
```

### C#

```csharp
System.int GetMirrorOrientation2(
   System.object DispEntity,
   out System.bool BMirrorOri
)
```

### C++/CLI

```cpp
System.int GetMirrorOrientation2(
   System.Object^ DispEntity,
   [Out] System.bool BMirrorOri
)
```

### Parameters

- `DispEntity`: Face to which material orientation is applied
- `BMirrorOri`: 0 or false for clockwise ply angle direction, -1 or true for counter-clockwise ply angle direction

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsSurfaceMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
