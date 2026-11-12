---
title: "Show2 Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "Show2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.html"
---

# Show2 Method (IPropertyManagerPage2)

Shows the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function Show2( _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Options As System.Integer
Dim value As System.Integer

value = instance.Show2(Options)
```

### C#

```csharp
System.int Show2(
   System.int Options
)
```

### C++/CLI

```cpp
System.int Show2(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Options as defined in [swPropertyManagerPageShowOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageShowOptions_e.html)

### Return Value

Status as defined by [swPropertyManagerPageStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageStatus_e.html)

## VBA Syntax

See [PropertyManagerPage2::Show2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~Show2.html).

## Examples

See the [IPropertyManagerPage2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html) examples.

## Remarks

If another PropertyManager page is already displayed and that page is receptive to being stacked upon, then setting swPropertyManagerPageShowOptions_e to swPropertyManagerPageShowOptions_StackPage will stack your PropertyManager page on it. When the user closes your PropertyManager page, the previous PropertyManager page is shown automatically.

**NOTE:** Typically SOLIDWORKS does not stack PropertyManager pages, and in the couple instances where SOLIDWORKS does, it is an agreement between the PropertyManager pages. The first PropertyManager page agrees that it can be stacked upon and allows the other known PropertyManager page to stack upon it. The mechanism is not a case of one PropertyManager page allowing any other generic PropertyManager page to be stacked upon it. It is assumed that the two pages are in agreement about what is going on and deal with it.

Using the API to stack ProertyManager pages is the same -- an add-in is the owner of both PropertyManager pages and knows what is going on and deals with it. The concept of an API PropertyManager page wanting to know if it can stack upon the currently displayed PropertyManager page, whatever it might be, does not work because of the assumption that the first API PropertyManager page has knowledge of and allows another API PropertyManager page to stack on it.

If the PropertyManager page is locked, then stacking PropertyManager pages is not allowed. A PropertyManager page is locked if the Options argument of [ISldWorks::CreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CreatePropertyManagerPage.html) or [ISldWorks::ICreatePropertyManagerPage](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ICreatePropertyManagerPage.html) was set to swPropertyManagerOptions_LockedPage when the PropertyManager page was created.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.html)
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html)
[IPropertyManagerPage2::Close Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.html)
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
