---
title: "GetComponent Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent.html"
---

# GetComponent Method (IExplodeStep)

Gets the specified component in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponent( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetComponent(Index)
```

### C#

```csharp
System.object GetComponent(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetComponent(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of a component in this explode step

### Return Value

Specified [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html) in the explode step

## VBA Syntax

See [ExplodeStep::GetComponent](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetComponent.html).

## Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html) to get a valid value for Index.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponentName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.html)
[IExplodeStep::GetNumOfComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html)
[IExplodeStep::IGetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~IGetComponent.html)
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
