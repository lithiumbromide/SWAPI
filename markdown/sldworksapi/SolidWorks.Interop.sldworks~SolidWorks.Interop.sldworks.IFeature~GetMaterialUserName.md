---
title: "GetMaterialUserName Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName.html"
---

# GetMaterialUserName Method (IFeature)

Gets the material name for this feature, which is visible to the user.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterialUserName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.String

value = instance.GetMaterialUserName()
```

### C#

```csharp
System.string GetMaterialUserName()
```

### C++/CLI

```cpp
System.String^ GetMaterialUserName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Material user name property on this feature

## VBA Syntax

See [Feature::GetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetMaterialUserName.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.html)
[IFeature::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName.html)
[IFeature::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName.html)
