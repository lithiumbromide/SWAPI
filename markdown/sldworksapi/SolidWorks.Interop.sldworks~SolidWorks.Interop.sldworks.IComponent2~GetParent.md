---
title: "GetParent Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html"
---

# GetParent Method (IComponent2)

Gets the parent component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParent() As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As Component2

value = instance.GetParent()
```

### C#

```csharp
Component2 GetParent()
```

### C++/CLI

```cpp
Component2^ GetParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Parent [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [Component2::GetParent](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetParent.html).

## Examples

[Get Parent Component (VBA)](Get_Parent_Component_Example_VB.htm)
[Show Selected Components Only (VBA)](Only_Show_Selected_Components_Example_VB.htm)

## Remarks

If the component is the root component or a top-level component, then this method returns NULL.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::GetComponentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentCount.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IComponent2::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html)
[IComponent2::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetChildren.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)
[IConfiguration::IGetRootComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetRootComponent2.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)

## Availability

SOLIDWORKS 2001Plus SP5, Revision Number 10.5
