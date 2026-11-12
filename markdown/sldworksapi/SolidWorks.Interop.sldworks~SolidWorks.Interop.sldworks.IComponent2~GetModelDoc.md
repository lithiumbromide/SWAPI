---
title: "GetModelDoc Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetModelDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc.html"
---

# GetModelDoc Method (IComponent2)

Obsolete. Superseded by [IComponent2::GetModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelDoc() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Object

value = instance.GetModelDoc()
```

### C#

```csharp
System.object GetModelDoc()
```

### C++/CLI

```cpp
System.Object^ GetModelDoc();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [Component2::GetModelDoc](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetModelDoc.html).

## Examples

[Change Material Properties (VBA)](Change_Material_Properties_Example_VB.htm)
[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)
[Get BOM Balloon Properties (C#)](Get_BOM_Balloon_Properties_Example_CSharp.htm)
[Get BOM Balloon Properties (VB.NET)](Get_BOM_Balloon_Properties_Example_VBNET.htm)
[Get BOM Balloon Properties (VBA)](Get_BOM_Balloon_Properties_Example_VB.htm)

## Remarks

This method might return Nothing or null if:

- a component is suppressed or lightweight.
- the component ID is not loaded into memory by SOLIDWORKS.

For more information on lightweight components, see [Work With Lightweight Components](sldworksAPIProgGuide.chm::/OVERVIEW/Work_with_Lightweight_Components.htm).

When you use the IModelDoc2 object of a component, you do not have access to whatever uniqueness might exist for this instance of the assembly IComponent2. This occurs because the IModelDoc2 object goes back to the saved part file. By comparison, the IComponent2 object gathers information at the assembly level. This allows IComponent2 objects to recognize assembly-level changes made to a component instance (for example, assembly-level features and material changes).

In addition, the IModelDoc2 object returned from this method represents the last-saved state. If the component part is currently open, then the IModelDoc2 object represents the state of the opened document. For example, if the component part is not open and it was last saved in the default configuration, then IComponent2::GetModelDoc
returns a IModelDoc2 pointer representing that state. To get access to other configuration information (such as features and configuration properties), you must activate the part and show the desired configuration using [IModelDoc2::ShowConfiguration2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ShowConfiguration2.html).

If this component is the root component, then this method returns a NULL pointer. For more information, see [IConfiguration::GetRootComponent.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetRootComponent.html)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IGetModelDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelDoc.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
