---
title: "Update3DInterconnectModel Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Update3DInterconnectModel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Update3DInterconnectModel.html"
---

# Update3DInterconnectModel Method (IFeature)

Updates the model for this 3D Interconnect part or assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function Update3DInterconnectModel() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.Update3DInterconnectModel()
```

### C#

```csharp
System.bool Update3DInterconnectModel()
```

### C++/CLI

```cpp
System.bool Update3DInterconnectModel();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if model updated successfully, false if not

## VBA Syntax

See [Feature::Update3DInterconnectModel](ms-its:sldworksapivb6.chm::/sldworks~Feature~Update3DInterconnectModel.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

Before calling this method, use [IFeature::Is3DInterconnectUpdateAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Is3DInterconnectUpdateAvailable.html) to determine whether an update is available.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
