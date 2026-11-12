---
title: "Is3DInterconnectUpdateAvailable Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Is3DInterconnectUpdateAvailable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.html"
---

# Is3DInterconnectUpdateAvailable Property (IFeature)

Gets whether an update is available for this 3D Interconnect part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Is3DInterconnectUpdateAvailable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.Is3DInterconnectUpdateAvailable
```

### C#

```csharp
System.bool Is3DInterconnectUpdateAvailable {get;}
```

### C++/CLI

```cpp
property System.bool Is3DInterconnectUpdateAvailable {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if an update is available, false if not

## VBA Syntax

See [Feature::Is3DInterconnectUpdateAvailable](ms-its:sldworksapivb6.chm::/sldworks~Feature~Is3DInterconnectUpdateAvailable.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

If this property is true, use [IFeature::Update3DInterconnectModel](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.html) to update the imported feature or component.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
