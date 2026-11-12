---
title: "SetTransformAndSolve2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetTransformAndSolve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve2.html"
---

# SetTransformAndSolve2 Method (IComponent2)

Obsolete. Superseded by [IComponent2::SetTransformAndSolve3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetTransformAndSolve3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTransformAndSolve2( _
   ByVal XformIn As MathTransform _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim XformIn As MathTransform
Dim value As System.Boolean

value = instance.SetTransformAndSolve2(XformIn)
```

### C#

```csharp
System.bool SetTransformAndSolve2(
   MathTransform XformIn
)
```

### C++/CLI

```cpp
System.bool SetTransformAndSolve2(
   MathTransform^ XformIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XformIn`: Pointer to the [IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html) object to use to set and solve

### Return Value

True if the transform was set and solved, false if not

## VBA Syntax

See [Component2::SetTransformAndSolve2](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetTransformAndSolve2.html).

## Remarks

If making multiple calls to this method, consider using [IDragOperator::Drag](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragOperator~Drag.html), which is more efficient because it reuses the solver. However, DragOperator::Drag does not support clash detection or dynamic clearance.

The transform specified must be in relation to the root component. See [IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html) or [IConfiguration::IGetRootComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html).

SOLIDWORKS moves the destination component, or any component above it in the assembly tree, so that the destination component's transform is set to the desired one. Transforming an object using this method can cause SOLIDWORKS to transform other mated or constrained objects.

After you have changed a component's transform, you can call [IAssemblyDoc::UpdateBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~UpdateBox.html) to avoid clipping in shaded display mode.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetTotalTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetTotalTransform.html)
[IComponent2::Transform2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.html)
[IComponent2::GetSpecificTransform Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSpecificTransform.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
