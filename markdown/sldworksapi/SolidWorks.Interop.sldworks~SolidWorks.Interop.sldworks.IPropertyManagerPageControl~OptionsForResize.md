---
title: "OptionsForResize Property (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "OptionsForResize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~OptionsForResize.html"
---

# OptionsForResize Property (IPropertyManagerPageControl)

Gets or sets how to override the SOLIDWORKS default behavior when changing the width of a PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Property OptionsForResize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As System.Integer

instance.OptionsForResize = value

value = instance.OptionsForResize
```

### C#

```csharp
System.int OptionsForResize {get; set;}
```

### C++/CLI

```cpp
property System.int OptionsForResize {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Resize the PropertyManager page as defined in [swPropMgrPageControlOnResizeOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropMgrPageControlOnResizeOptions_e.html) (see **Remarks**)

## VBA Syntax

See [PropertyManagerPageControl::OptionsForResize](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageControl~OptionsForResize.html).

## Remarks

| If... | Then... |
| --- | --- |
| swControlOptionsOnResize_LockLeft specified | the control is locked in place relative to the left edge of the PropertyManager page. When the page width is changed, the control stays in place and its width does not change. |
| swControlOptionsOnResize_LockRight specified | the control is locked in place relative to the right edge of the PropertyManager page. When the page width is changed, the control shifts to the right, but its width does not change. |
| swControlOptionsOnResize_LockLeft and swControlOptionsOnResize_LockRight specified | the left edge of the control stays in place relative to the left edge and the right edge of the control stays in place relative to the right edge of the PropertyManager page, giving the effect that the control grows and shrinks with the PropertyManager page. |

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2008 SP4, Revision Number 16.4
