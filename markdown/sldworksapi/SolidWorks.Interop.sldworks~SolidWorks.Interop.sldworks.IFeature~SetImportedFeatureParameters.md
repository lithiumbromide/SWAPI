---
title: "SetImportedFeatureParameters Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetImportedFeatureParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.html"
---

# SetImportedFeatureParameters Method (IFeature)

Sets the data object for this 3D Interconnect part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetImportedFeatureParameters( _
   ByVal DataObj As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim DataObj As System.Object
Dim value As System.Integer

value = instance.SetImportedFeatureParameters(DataObj)
```

### C#

```csharp
System.int SetImportedFeatureParameters(
   System.object DataObj
)
```

### C++/CLI

```cpp
System.int SetImportedFeatureParameters(
   System.Object^ DataObj
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DataObj`: [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)

### Return Value

Error codes as defined in [sw3DInterconnectImportErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

## VBA Syntax

See [Feature::SetImportedFeatureParameters](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetImportedFeatureParameters.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

Before calling this method, use [IFeature::Is3DInterconnectFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.html) to ensure that this is a 3D Interconnect feature.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
