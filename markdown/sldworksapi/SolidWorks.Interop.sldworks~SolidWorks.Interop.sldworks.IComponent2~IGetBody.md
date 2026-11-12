---
title: "IGetBody Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetBody.html"
---

# IGetBody Method (IComponent2)

Gets the body that belongs to this instance of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As Body2

value = instance.IGetBody()
```

### C#

```csharp
Body2 IGetBody()
```

### C++/CLI

```cpp
Body2^ IGetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

## Examples

[Enumerate Bodies (C++)](Enumerate_Bodies_Example_CPlusPlus_COM.htm)

## Remarks

This method returns a valid IBody2 object only for fully resolved components that reference an [IPartDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc.html). For the root component, lightweight components or components that reference an AssemblyDoc, this method returns a NULL body object. However, if a component is in a multibody part, then this method returns the first body.

For COM applications, this method returns the status code ITF_E_COMPONENTNOTRESOLVED.

This method is different from the IPartDoc::Body method in that it recognizes assembly-level features and returns that information based on the component instance. IPartDoc::Body never recognizes assembly-level features because the feature information is kept with the assembly, not propagated down to the part file.

For example, if PartABC is added to an assembly twice, then changes to that IPartDoc object would affect both instances of the assembly IComponent2. Likewise, querying information from that IPartDoc object will not recognize changes in the assembly that may have altered only one of the components (for example, an assembly-level feature was added to one of the components). However, the component object recognizes the two instances of PartABC as two distinct IComponent2 objects and returns its information from the assembly level.

For example, one assembly configuration might have an assembly-level feature that cuts a hole through each of the components in the assembly. Using this method on each of the assembly components returns the body of each component with the hole feature that was applied in this particular configuration. If you switch to the configuration
without the assembly-level hole and re-traverse the IComponent2 objects, then calling this method for each component returns the IBody2 object without the hole feature because it was applied in the other configuration.

For more information on lightweight components, see [IComponent2::GetSuppression](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetSuppression.html), [IComponent2::SetSuppression2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetSuppression2.html), and [IAssemblyDoc::ResolveAllLightWeightComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~ResolveAllLightWeightComponents.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBody.html)
[IComponent2::GetBodies3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetBodies3.html)
[IComponent2::EnumBodies2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~EnumBodies2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
