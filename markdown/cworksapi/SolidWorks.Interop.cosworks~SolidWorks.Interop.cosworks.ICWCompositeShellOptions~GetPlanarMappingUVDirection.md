---
title: "GetPlanarMappingUVDirection Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "GetPlanarMappingUVDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetPlanarMappingUVDirection.html"
---

# GetPlanarMappingUVDirection Method (ICWCompositeShellOptions)

Gets the reference plane used to calculate the ply angle direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPlanarMappingUVDirection( _
   ByRef DUVDir As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim DUVDir As System.Object
Dim value As System.Integer

value = instance.GetPlanarMappingUVDirection(DUVDir)
```

### C#

```csharp
System.int GetPlanarMappingUVDirection(
   out System.object DUVDir
)
```

### C++/CLI

```cpp
System.int GetPlanarMappingUVDirection(
   [Out] System.Object^ DUVDir
)
```

### Parameters

- `DUVDir`: Reference plane used to calculate ply angle direction:

  - XY plane
  - ZX plane
  - YZ plane
  - Current view
  - Face or edge

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::GetPlanarMappingUVDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~GetPlanarMappingUVDirection.html).

## Remarks

This method is valid only if [ICWCompositeShellOptions::MappingType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~MappingType.html) is set to [swsCompositeShellOptionsMappingType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsMappingType_e.html).swsCompositeShellOptionsPlanarMapping.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::SetPlanarMappingUVDirection Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlanarMappingUVDirection.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
