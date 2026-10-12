---
title: "IGetModelDoc Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetModelDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelDoc.html"
---

# IGetModelDoc Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetModelDoc() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As ModelDoc2

value = instance.IGetModelDoc()
```

### C#

```csharp
ModelDoc2 IGetModelDoc()
```

### C++/CLI

```cpp
ModelDoc2^ IGetModelDoc();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## Remarks

This method might return NULL if:

- a component is suppressed or lightweight.
- the component ID is not loaded into memory by SOLIDWORKS.

For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

When you use the IModelDoc2 object of a component, you do not have access to whatever uniqueness might exist for this instance of the assembly IComponent2. This occurs because the IModelDoc2 object goes back to the saved part file. By comparison, the IComponent2 object gathers information at the assembly level. This allows IComponent2 objects to recognize assembly-level changes made to a component instance (for example, assembly-level features and material changes).

In addition, the IModelDoc2 object returned from this method represents the last-saved state. If the component part is currently open, then the IModelDoc2 object represents the state of the opened document. For example, if the component part is not open and it was last saved in the default configuration, then IComponent2::GetModelDoc
returns a IModelDoc2 pointer representing that state. To get access to other configuration information (such as features and configuration properties), you must activate the part and show the desired configuration using [IModelDoc2::ShowConfiguration2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html).

If this component is the root component, then this method returns a NULL pointer. For more information, see [IConfiguration::IGetRootComponent2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetRootComponent2.html)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetModelDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
