---
title: "Checked Property (IPropertyManagerPageCheckbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCheckbox"
member: "Checked"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox~Checked.html"
---

# Checked Property (IPropertyManagerPageCheckbox)

Gets or sets this check box as selected.

## Syntax

### Visual Basic (Declaration)

```vb
Property Checked As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCheckbox
Dim value As System.Boolean

instance.Checked = value

value = instance.Checked
```

### C#

```csharp
System.bool Checked {get; set;}
```

### C++/CLI

```cpp
property System.bool Checked {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the check box is selected, false if not

## VBA Syntax

See [PropertyManagerPageCheckbox::Checked](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCheckbox~Checked.html).

## Examples

[Set Focus on PropertyManager Page Control (C#)](Set_Focus_on_PropertyManager_Page_Control_Example_CSharp.htm)
[Set Focus on PropertyManager Page Control (VB.NET)](Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm)
[Set Focus on PropertyManager Page Control (VBA)](Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm)

## See Also

[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.html)
[IPropertyManagerPageCheckbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision number 10.0
