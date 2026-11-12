---
title: "Transform2 Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "Transform2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html"
---

# Transform2 Property (IComponent2)

Gets or sets the component transform.

## Syntax

### Visual Basic (Declaration)

```vb
Property Transform2 As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As MathTransform

instance.Transform2 = value

value = instance.Transform2
```

### C#

```csharp
MathTransform Transform2 {get; set;}
```

### C++/CLI

```cpp
property MathTransform^ Transform2 {
   MathTransform^ get();
   void set (    MathTransform^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [Component2::Transform2](ms-its:sldworksapivb6.chm::/sldworks~Component2~Transform2.html).

## Examples

[Align Assembly Component to Assembly Origin and Planes (VBA)](Align_Assembly_Component_to_Assembly_Origin_and_Planes_Example_VB.htm)
[Combine Assembly Components into Part (VBA)](Combine_Assembly_Components_into_Part_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Transform Point from Component Space to Assembly Space (C#)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_CSharp.htm)
[Transform Point from Component Space to Assembly Space (VB.NET)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_VBNET.htm)
[Transform Point from Component Space to Assembly Space (VBA)](Transform_Point_from_Component_Space_to_Assembly_Space_Example_VB.htm)

## Remarks

This property affects the underlying model geometry and the display of the component.

You must specify the transform in relation to the root component. This also applies when there is an in-context edit in progress. The transform is still with respect to the root component of the active assembly document, not with respect to the root component of the edit target. See [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html) and [IConfiguration::IGetRootComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html).

The destination component, or any component above it in the assembly tree, is moved so that the destination component's transform is set to the desired one.

You can call [IModelDoc2::Rebuild](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Rebuild.html) with the swUpdateMates argument to rebuild the model after transforming a component. This is much faster than rebuilding all of the geometry for the model using the now obsolete IAssemblyDoc::EditRebuild.

This property lets you violate existing mate relationships. If you place a component at an invalid location based on the mate definitions, then IModelDoc2::Rebuild recalculates existing mate relationships and moves your components to the closest valid location.

After you change a component's transform, you can call [IAssemblyDoc::UpdateBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~UpdateBox.html) to avoid clipping in shaded display mode.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::PresentationTransform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~PresentationTransform.html)
[IComponent2::RemovePresentationTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~RemovePresentationTransform.html)
[IComponent2::SetTransformAndSolve2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.html)
[IComponent2::GetSpecificTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
