---
title: "Scale2 Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "Scale2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2.html"
---

# Scale2 Property (IModelView)

Gets and sets the model view scale factor.

## Syntax

### Visual Basic (Declaration)

```vb
Property Scale2 As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Double

instance.Scale2 = value

value = instance.Scale2
```

### C#

```csharp
System.double Scale2 {get; set;}
```

### C++/CLI

```cpp
property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale factor

## VBA Syntax

See [ModelView::Scale2](ms-its:sldworksapivb6.chm::/sldworks~ModelView~Scale2.html).

## Examples

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)

## Remarks

If you want to zoom in by a factor of 2, then you should get the current scale using this method, multiply the return value by 2, and then pass that value back into this method, which will increase the model view scale.

Using data returned from this property along with information from [IModelView::Orientation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Orientation3.html) and [IModelView::Translation3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Translation3.html) should be multiplied in this order: orientation > scale > transform.

To map your coordinates from 3D space to the screen, use [IModelView::Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~Transform.html).

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.html)
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.html)
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.html)
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.html)
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.html)
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.html)

## Availability

SOLIDWORKS 99, datecode 1999207
