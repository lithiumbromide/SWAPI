---
title: "State Property (IPropertyManagerPageCheckbox)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageCheckbox"
member: "State"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox~State.html"
---

# State Property (IPropertyManagerPageCheckbox)

Gets or sets the state of this check box.

## Syntax

### Visual Basic (Declaration)

```vb
Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageCheckbox
Dim value As System.Integer

instance.State = value

value = instance.State
```

### C#

```csharp
System.int State {get; set;}
```

### C++/CLI

```cpp
property System.int State {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

State of this check box as defined in [swPropertyManagerCheckboxState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerCheckboxState_e.html)

## VBA Syntax

See [PropertyManagerPageCheckbox::State](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageCheckbox~State.html).

## Examples

[Set Focus on PropertyManager Page Control (C#)](Set_Focus_on_PropertyManager_Page_Control_Example_CSharp.htm)
[Set Focus on PropertyManager Page Control (VB.NET)](Set_Focus_on_PropertyManager_Page_Control_Example_VBNET.htm)
[Set Focus on PropertyManager Page Control (VBA)](Set_Focus_on_PropertyManager_Page_Control_Example_VB.htm)

## Remarks

If you use this property to set the state of a check box, then you must use this property to modify the state of the check box.

## See Also

[IPropertyManagerPageCheckbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox.html)
[IPropertyManagerPageCheckbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
