---
title: "EmphasizeOutline Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "EmphasizeOutline"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~EmphasizeOutline.html"
---

# EmphasizeOutline Property (IView)

Gets or sets whether the outlines of section views are emphasized in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property EmphasizeOutline As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

instance.EmphasizeOutline = value

value = instance.EmphasizeOutline
```

### C#

```csharp
System.bool EmphasizeOutline {get; set;}
```

### C++/CLI

```cpp
property System.bool EmphasizeOutline {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the outlines of section views are outlined, false if not

## VBA Syntax

See [View::EmphasizeOutline](ms-its:sldworksapivb6.chm::/Sldworks~View~EmphasizeOutline.html).

## Examples

[Create Section View and Get Some Data (C#)](Create_Section_View_and_Get_Some_Data_Example_CSharp.htm)
[Create Section View and Get Some Data (VB.NET)](Create_Section_View_and_Get_Some_Data_Example_VBNET.htm)
[Create Section View and Get Some Data (VBA)](Create_Section_View_and_Get_Some_Data_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
