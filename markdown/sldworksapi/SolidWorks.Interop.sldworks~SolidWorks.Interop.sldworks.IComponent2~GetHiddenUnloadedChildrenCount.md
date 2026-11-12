---
title: "GetHiddenUnloadedChildrenCount Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetHiddenUnloadedChildrenCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html"
---

# GetHiddenUnloadedChildrenCount Method (IComponent2)

Gets the number of hidden children components of this component that were not loaded when an assembly was [opened selectively](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~Selective.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHiddenUnloadedChildrenCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetHiddenUnloadedChildrenCount()
```

### C#

```csharp
System.int GetHiddenUnloadedChildrenCount()
```

### C++/CLI

```cpp
System.int GetHiddenUnloadedChildrenCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of hidden children components of this component that were not loaded when an assembly was opened selectively

## VBA Syntax

See [Component2::GetHiddenUnloadedChildrenCount](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetHiddenUnloadedChildrenCount.html).

## Remarks

You can open an assembly with all components hidden except those that you select. The selected components are loaded lightweight. All other components become hidden and are not loaded into memory. This method returns the number of unloaded hidden children of this component. This method does not return the number of suppressed unloaded children components. Call [IComponent2::GetUnloadedComponentNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html) for that type of related information.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
