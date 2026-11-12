---
title: "IGetFirstCenterOfMass Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetFirstCenterOfMass"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetFirstCenterOfMass.html"
---

# IGetFirstCenterOfMass Method (IView)

Gets the first center of mass in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstCenterOfMass() As CenterOfMass
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As CenterOfMass

value = instance.IGetFirstCenterOfMass()
```

### C#

```csharp
CenterOfMass IGetFirstCenterOfMass()
```

### C++/CLI

```cpp
CenterOfMass^ IGetFirstCenterOfMass();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to [ICenterOfMass](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICenterOfMass.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetFirstCenterOfMass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstCenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
