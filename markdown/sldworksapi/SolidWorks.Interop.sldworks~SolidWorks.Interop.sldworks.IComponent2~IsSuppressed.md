---
title: "IsSuppressed Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsSuppressed"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSuppressed.html"
---

# IsSuppressed Method (IComponent2)

Gets whether this component is suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsSuppressed() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsSuppressed()
```

### C#

```csharp
System.bool IsSuppressed()
```

### C++/CLI

```cpp
System.bool IsSuppressed();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this component is suppressed, false if not

## VBA Syntax

See [Component2::IsSuppressed](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsSuppressed.html).

## Examples

[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)
[Get and Set Component's Suppression State (VBA)](Get_and_Set_Component_s_Suppression_State_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)

## Remarks

The suppression state of a component can vary based on the active configuration. You might want to use [IComponent2::GetSuppression](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetSuppression.html), which returns the specific suppression state of the component.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::LightweightAllResolved Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~LightweightAllResolved.html)
[IAssemblyDoc::SetComponentSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentSuppression.html)
[IComponent2::GetSuppression Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression.html)
[IComponent2::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSuppression2.html)
[IFeature::IsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.html)
[IFeature::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.html)
[IFeature::ISetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
