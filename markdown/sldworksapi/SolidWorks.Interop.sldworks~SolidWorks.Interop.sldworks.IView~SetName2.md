---
title: "SetName2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SetName2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetName2.html"
---

# SetName2 Method (IView)

Sets the name of this drawing view, as displayed in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName2( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Name As System.String
Dim value As System.Boolean

value = instance.SetName2(Name)
```

### C#

```csharp
System.bool SetName2(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool SetName2(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of drawing view

### Return Value

True if the name of the drawing view is set, false if not

## VBA Syntax

See [View::SetName2](ms-its:sldworksapivb6.chm::/sldworks~View~SetName2.html).

## Remarks

The drawing view name that you specify:

- must be unique in the FeatureManager design tree.
- not contain any of the SOLIDWORKS reserved special characters.

If either of these conditions is not met, then this method returns false and the name of the drawing view is not changed.

You cannot change the drawing view name for detail views and section views. If you attempt to do so, then false if returned and the drawing view name is not changed.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetName2.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
