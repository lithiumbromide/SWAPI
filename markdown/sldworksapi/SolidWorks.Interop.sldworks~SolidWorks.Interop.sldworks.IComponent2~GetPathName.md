---
title: "GetPathName Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetPathName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.html"
---

# GetPathName Method (IComponent2)

Gets the full path name for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetPathName()
```

### C#

```csharp
System.string GetPathName()
```

### C++/CLI

```cpp
System.String^ GetPathName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Full path name for this component, including the filename

## VBA Syntax

See [Component2::GetPathName](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetPathName.html).

## Examples

[Get Component for Selected Entity (VBA)](Get_Component_for_Selected_Entity_Example_VB.htm)
[Get Components Properties in Drawing View (VBA)](Get_Components_Properties_in_Drawing_View_Example_VB.htm)
[Get Part for Corresponding Component (VBA)](Get_Part_for_Corresponding_Component_Example_VB.htm)
[Make Assembly Components Lightweight (VBA)](Make_Assembly_Components_Lightweight_Example_VB.htm)
[Set All Assembly Components Lightweight or Resolved (VBA)](Set_All_Assembly_Components_Lightweight_or_Resolved_Example_VB.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)

## Remarks

The underlying document for this component might not have been loaded into memory if the component is lightweight or suppressed. In this situation, [IComponent2::GetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetModelDoc.html) or [IComponent2::IGetModelDoc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetModelDoc.html) may return NULL and the file and path name returned by this method will be the As-Saved file and path name for the IComponent2.

This method does not apply search criteria or look in the current working directory for the component file reference if the component is lightweight or suppressed.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IModelDoc2::GetPathName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPathName.html)
[IComponent2::GetImportedPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetImportedPath.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
