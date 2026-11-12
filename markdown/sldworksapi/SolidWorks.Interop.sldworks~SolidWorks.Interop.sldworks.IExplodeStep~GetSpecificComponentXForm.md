---
title: "GetSpecificComponentXForm Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetSpecificComponentXForm"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetSpecificComponentXForm.html"
---

# GetSpecificComponentXForm Method (IExplodeStep)

Gets the transformation matrix of the specified component in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSpecificComponentXForm( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetSpecificComponentXForm(Index)
```

### C#

```csharp
System.object GetSpecificComponentXForm(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetSpecificComponentXForm(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of a component in the selection list

### Return Value

Transformation matrix array of 16 doubles

## VBA Syntax

See [ExplodeStep::GetSpecificComponentXForm](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetSpecificComponentXForm.html).

## Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html) to get a valid value for Index.

For regular explode steps, this method works just like [IExplodeStep::GetComponentXform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.html) to get the transformation of the entire explode step. This method also works for radial explode steps by getting the transformation of an individual radial explode component.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
