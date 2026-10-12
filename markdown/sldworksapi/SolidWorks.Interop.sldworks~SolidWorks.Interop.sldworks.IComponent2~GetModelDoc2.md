---
title: "GetModelDoc2 Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetModelDoc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2.html"
---

# GetModelDoc2 Method (IComponent2)

Gets the model document for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelDoc2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetModelDoc2()
```

### C#

```csharp
System.object GetModelDoc2()
```

### C++/CLI

```cpp
System.Object^ GetModelDoc2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [Component2::GetModelDoc2](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetModelDoc2.html).

## Examples

[Get Selected Objects and types in Assembly (VBA)](Get_Selected_Objects_and_Types_in_Assembly_Example_VB.htm)
[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)

## Remarks

This method might return Nothing or null if:

- a component is suppressed or lightweight.
- the component ID is not loaded into memory by SOLIDWORKS.

For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

When you use the IModelDoc2 object of a component, you do not have access to whatever uniqueness might exist for this instance of the assembly IComponent2. This occurs because the IModelDoc2 object goes back to the saved part file. By comparison, the IComponent2 object gathers information at the assembly level. This allows IComponent2 objects to recognize assembly-level changes made to a component instance (for example, assembly-level features and material changes).

In addition, the IModelDoc2 object returned from this method represents the last-saved state. If the component part is currently open, then the IModelDoc2 object represents the state of the opened document. For example, if the component part is not open and it was last saved in the default configuration, then IComponent2::GetModelDoc2
returns a IModelDoc2 pointer representing that state. To get access to other configuration information (such as features and configuration properties), you must activate the part and show the desired configuration using [IModelDoc2::ShowConfiguration2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html).

Unlike the previous version of this method ([IConfiguration::GetRootComponent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc.html)), this version of this method can handle the root component of an assembly.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IsRoot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsRoot.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
