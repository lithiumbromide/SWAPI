---
title: "SetTransformAndSolve3 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetTransformAndSolve3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve3.html"
---

# SetTransformAndSolve3 Method (IComponent2)

Sets the transform and solves for the mates for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTransformAndSolve3( _
   ByVal XformIn As MathTransform, _
   ByVal ThisConfiguration As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim XformIn As MathTransform
Dim ThisConfiguration As System.Boolean
Dim value As System.Boolean

value = instance.SetTransformAndSolve3(XformIn, ThisConfiguration)
```

### C#

```csharp
System.bool SetTransformAndSolve3(
   MathTransform XformIn,
   System.bool ThisConfiguration
)
```

### C++/CLI

```cpp
System.bool SetTransformAndSolve3(
   MathTransform^ XformIn,
   System.bool ThisConfiguration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`: Pointer to the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object to use to set and solve
- `ThisConfiguration`: True to transform this configuration, false to transform all configurations

### Return Value

True if the transform was set and solved, false if not

## VBA Syntax

See [Component2::SetTransformAndSolve3](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetTransformAndSolve3.html).

## Remarks

If making multiple calls to this method, consider using [IDragOperator::Drag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~Drag.html), which is more efficient because it reuses the solver. However, DragOperator::Drag does not support clash detection or dynamic clearance.

The transform specified must be in relation to the root component. See [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html) or [IConfiguration::IGetRootComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html).

SOLIDWORKS moves the destination component, or any component above it in the assembly tree, so that the destination component's transform is set to the desired one. Transforming an object using this method can cause SOLIDWORKS to transform other mated or constrained objects.

After you have changed a component's transform, you can call [IAssemblyDoc::UpdateBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~UpdateBox.html) to avoid clipping in shaded display mode.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTotalTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::GetSpecificTransform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)
[IComponent2::Transform2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
