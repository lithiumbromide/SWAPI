---
title: "Bodies Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "Bodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Bodies.html"
---

# Bodies Property (IView)

Gets or sets the bodies of a multibody part to show in the drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

instance.Bodies = value

value = instance.Bodies
```

### C#

```csharp
System.object Bodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) of a multibody part

## VBA Syntax

See [View::Bodies](ms-its:sldworksapivb6.chm::/sldworks~View~Bodies.html).

## Examples

[Set Body for View (C#)](Set_Body_for_View_Example_CSharp.htm)
[Set Body for View (VB.NET)](Set_Body_for_View_Example_VBNET.htm)
[Set Body for View (VBA)](Set_Body_for_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBodiesCount.html)
[IView::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetBodies.html)
[IView::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISetBodies.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
