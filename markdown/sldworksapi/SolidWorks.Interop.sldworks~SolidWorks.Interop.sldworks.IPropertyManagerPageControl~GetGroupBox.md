---
title: "GetGroupBox Method (IPropertyManagerPageControl)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageControl"
member: "GetGroupBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~GetGroupBox.html"
---

# GetGroupBox Method (IPropertyManagerPageControl)

Gets the PropertyManager group box to which this control belongs.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGroupBox() As PropertyManagerPageGroup
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageControl
Dim value As PropertyManagerPageGroup

value = instance.GetGroupBox()
```

### C#

```csharp
PropertyManagerPageGroup GetGroupBox()
```

### C++/CLI

```cpp
PropertyManagerPageGroup^ GetGroupBox();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[PropertyManager page group box](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageGroup.html) or NULL if the control is not in a PropertyManager group box

## VBA Syntax

See [PropertyManagerPageControl::GetGroupBox](ms-its:sldworksapivb6.chm::/Sldworks~PropertyManagerPageControl~GetGroupBox.html).

## See Also

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.html)
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
