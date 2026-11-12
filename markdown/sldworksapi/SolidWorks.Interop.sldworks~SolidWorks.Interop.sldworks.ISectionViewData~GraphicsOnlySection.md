---
title: "GraphicsOnlySection Property (ISectionViewData)"
project: "SOLIDWORKS API Help"
interface: "ISectionViewData"
member: "GraphicsOnlySection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GraphicsOnlySection.html"
---

# GraphicsOnlySection Property (ISectionViewData)

Gets or sets whether to generate a graphics-only section view.

## Syntax

### Visual Basic (Declaration)

```vb
Property GraphicsOnlySection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISectionViewData
Dim value As System.Boolean

instance.GraphicsOnlySection = value

value = instance.GraphicsOnlySection
```

### C#

```csharp
System.bool GraphicsOnlySection {get; set;}
```

### C++/CLI

```cpp
property System.bool GraphicsOnlySection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to generate a graphics-only section view, false to not

## VBA Syntax

See [SectionViewData::GraphicsOnlySection](ms-its:sldworksapivb6.chm::/sldworks~SectionViewData~GraphicsOnlySection.html).

## Examples

[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)
[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)

## Remarks

This property corresponds to the **Graphics-only section** check box on the Section View PropertyManager page.

When a section view is created, the model is rebuilt. If the model is very large and complex, rebuilding the model slows down the creation of the section view. This property indicates whether to rebuild the model when a section view is created. When this property is set to true:

- **Keep cap color** check box is selected and inactivated on the Section View PropertyManager page.
- [ISectionViewData::KeepCapColor](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISectionViewData~KeepCapColor.html) returns only true; setting to false is ignored.
- Model is not rebuilt, and the section view is quickly generated.

## See Also

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.html)
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
