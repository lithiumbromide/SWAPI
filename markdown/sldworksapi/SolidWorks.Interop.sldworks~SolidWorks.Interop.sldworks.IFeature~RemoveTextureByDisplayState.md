---
title: "RemoveTextureByDisplayState Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "RemoveTextureByDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTextureByDisplayState.html"
---

# RemoveTextureByDisplayState Method (IFeature)

Removes texture from this feature in the specified display state.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveTextureByDisplayState( _
   ByVal DisplayStateName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim DisplayStateName As System.String
Dim value As System.Boolean

value = instance.RemoveTextureByDisplayState(DisplayStateName)
```

### C#

```csharp
System.bool RemoveTextureByDisplayState(
   System.string DisplayStateName
)
```

### C++/CLI

```cpp
System.bool RemoveTextureByDisplayState(
   System.String^ DisplayStateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateName`: Display state name

### Return Value

True to remove texture from the feature, false to not

## VBA Syntax

See [Feature::RemoveTextureByDisplayState](ms-its:sldworksapivb6.chm::/sldworks~Feature~RemoveTextureByDisplayState.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::SetTextureByDisplayState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTextureByDisplayState.html)
[IFeature::SetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetTexture.html)
[IFeature::RemoveTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~RemoveTexture.html)
[IFeature::GetTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTexture.html)
[IModelDocExtension::CreateTexture Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateTexture.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
