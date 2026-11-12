---
title: "GetOrientationName Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetOrientationName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetOrientationName.html"
---

# GetOrientationName Method (IView)

Gets the predefined name of this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOrientationName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

value = instance.GetOrientationName()
```

### C#

```csharp
System.string GetOrientationName()
```

### C++/CLI

```cpp
System.String^ GetOrientationName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Predefined name of view or an empty string for unnamed views

## VBA Syntax

See [View::GetOrientationName](ms-its:sldworksapivb6.chm::/Sldworks~View~GetOrientationName.html).

## Remarks

This method returns the orientation (predefined) name of the view; e.g., *Front, *Top, *Isometric, or a user-defined view name defined in the model. This method returns an empty string ("") for section views, detail views, projected views, and unfolded views.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
