---
title: "Is3DInterconnectFeature Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Is3DInterconnectFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectFeature.html"
---

# Is3DInterconnectFeature Property (IFeature)

Gets whether this is a 3D Interconnect feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Is3DInterconnectFeature As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.Is3DInterconnectFeature
```

### C#

```csharp
System.bool Is3DInterconnectFeature {get;}
```

### C++/CLI

```cpp
property System.bool Is3DInterconnectFeature {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if this is a 3D Interconnect feature, false if not

## VBA Syntax

See [Feature::Is3DInterconnectFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~Is3DInterconnectFeature.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetImportedFeatureParameters Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetImportedFeatureParameters.html)
[IFeature::SetImportedFeatureParameters Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetImportedFeatureParameters.html)
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
