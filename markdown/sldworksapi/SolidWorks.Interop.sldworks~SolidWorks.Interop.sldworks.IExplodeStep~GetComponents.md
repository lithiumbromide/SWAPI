---
title: "GetComponents Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html"
---

# GetComponents Method (IExplodeStep)

Gets the components of this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim value As System.Object

value = instance.GetComponents()
```

### C#

```csharp
System.object GetComponents()
```

### C++/CLI

```cpp
System.Object^ GetComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [ExplodeStep::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetComponents.html).

## Examples

See the [IExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html) examples.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponent.html)
[IExplodeStep::GetComponentName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.html)
[IExplodeStep::GetComponentXform Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentXform.html)
[IExplodeStep::SetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~SetComponents.html)
[IExplodeStep::GetNumOfComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
