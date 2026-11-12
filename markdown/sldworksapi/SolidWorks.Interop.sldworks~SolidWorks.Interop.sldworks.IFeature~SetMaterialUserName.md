---
title: "SetMaterialUserName Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetMaterialUserName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName.html"
---

# SetMaterialUserName Method (IFeature)

Sets the material user name for this feature, which is visible to the user.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMaterialUserName( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetMaterialUserName(Name)
```

### C#

```csharp
System.bool SetMaterialUserName(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetMaterialUserName(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Material user name property for this feature

### Return Value

True if the material user name was set successfully, false if not

## VBA Syntax

See [Feature::SetMaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetMaterialUserName.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName.html)
[IFeature::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.html)
[IFeature::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName.html)
