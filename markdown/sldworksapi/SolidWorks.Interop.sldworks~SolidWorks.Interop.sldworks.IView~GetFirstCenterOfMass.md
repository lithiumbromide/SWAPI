---
title: "GetFirstCenterOfMass Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstCenterOfMass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterOfMass.html"
---

# GetFirstCenterOfMass Method (IView)

Gets the first center of mass in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstCenterOfMass() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstCenterOfMass()
```

### C#

```csharp
System.object GetFirstCenterOfMass()
```

### C++/CLI

```cpp
System.Object^ GetFirstCenterOfMass();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ICenterOfMass](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterOfMass.html)

## VBA Syntax

See [View::GetFirstCenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstCenterOfMass.html).

## Examples

[Get Centers of Mass in Drawing Views (VBA)](Get_Centers_of_Mass_in_Drawing_Views_Example_VB.htm)
[Get Centers of Mass in Drawing Views (VB.NET)](Get_Centers_of_Mass_in_Drawing_Views_Example_VBNET.htm)
[Get Centers of Mass in Drawing Views (C#)](Get_Centers_of_Mass_in_Drawing_Views_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IGetFirstCenterOfMass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
