---
title: "Activate Method (IPropertyManagerPageTab)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageTab"
member: "Activate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab~Activate.html"
---

# Activate Method (IPropertyManagerPageTab)

Activates this tab in the PropertyManager page.

## Syntax

### Visual Basic (Declaration)

```vb
Function Activate() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageTab
Dim value As System.Boolean

value = instance.Activate()
```

### C#

```csharp
System.bool Activate()
```

### C++/CLI

```cpp
System.bool Activate();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if successful, false if not

## VBA Syntax

See [PropertyManagerPageTab::Activate](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageTab~Activate.html).

## Examples

[Activate PropertyManager Page Tab (VBA)](Activate_Property_Manager_Page_Tab_Example_VB.htm)
[Activate PropertyManager Page Tab (VB.NET)](Activate_Property_Manager_Page_Tab_Example_VBNET.htm)
[Activate PropertyManager Page Tab (C#)](Activate_Property_Manager_Page_Tab_Example_CSharp.htm)

## Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Show2.html) and [IPropertyManagerPage2::Close](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPageTab Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab.html)
[IPropertyManagerPageTab Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
