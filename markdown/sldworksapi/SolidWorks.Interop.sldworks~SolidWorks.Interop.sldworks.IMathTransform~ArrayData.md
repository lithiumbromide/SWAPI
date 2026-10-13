---
title: "ArrayData Property (IMathTransform)"
project: "SOLIDWORKS API Help"
interface: "IMathTransform"
member: "ArrayData"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~ArrayData.html"
---

# ArrayData Property (IMathTransform)

Gets and sets the array of 16 doubles for this transform.

## Syntax

### Visual Basic (Declaration)

```vb
Property ArrayData As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMathTransform
Dim value As System.Object

instance.ArrayData = value

value = instance.ArrayData
```

### C#

```csharp
System.object ArrayData {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ArrayData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of 16 doubles (see **Remarks**)

## VBA Syntax

See [MathTransform::ArrayData](ms-its:sldworksapivb6.chm::/sldworks~MathTransform~ArrayData.html).

## Examples

[Get Angle Between Plane and Line (VBA)](Get_Angle_Between_Plane_and_Line_Example_VB.htm)
[Get Coordinate System Transform (VBA)](Get_Coordinate_System_Transform_Example_VB.htm)
[Get Transform of Plane (VBA)](Get_Transform_of_Plane_Example_VB.htm)
[Get Transforms of Assembly Components (VBA)](Get_Transforms_of_Assembly_Components_Example_VB.htm)
[Get Patterned Cosmetic Thread Annotations Data (C#)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_CSharp.htm)
[Get Patterned Cosmetic Thread Annotations Data (VB.NET)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm)
[Get Patterned Cosmetic Thread Annotations Data (VBA)](Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm)

## Remarks

The first 9 elements define the 3x3 rotation matrix. The next 3 elements define the translation component. The next element defines the scaling component. The last 3 elements are unused.

The array data argument should be in a form that allows the direct calling of methods such as [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html).

## See Also

[IMathTransform Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.html)
[IMathTransform Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html)
[IMathTransform::IArrayData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform~IArrayData.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
