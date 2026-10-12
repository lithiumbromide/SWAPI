---
title: "IGetComponent Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "IGetComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponent.html"
---

# IGetComponent Method (IExplodeStep)

Gets the specified component in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponent( _
   ByVal Index As System.Integer _
) As Component
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As Component

value = instance.IGetComponent(Index)
```

### C#

```csharp
Component IGetComponent(
   System.int Index
)
```

### C++/CLI

```cpp
Component^ IGetComponent(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the component in this explode step

### Return Value

Specified [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) in the explode step

## VBA Syntax

See [ExplodeStep::IGetComponent](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~IGetComponent.html).

## Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html) to get a valid value for Index.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent.html)
[IExplodeStep::GetComponentName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.html)
[IExplodeStep::GetNumOfComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
