---
title: "Extension Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Extension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Extension.html"
---

# Extension Property (IModelDoc2)

Gets the [IModelDocExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html) object, which also allows access to the model document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Extension As ModelDocExtension
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As ModelDocExtension

value = instance.Extension
```

### C#

```csharp
ModelDocExtension Extension {get;}
```

### C++/CLI

```cpp
property ModelDocExtension^ Extension {
   ModelDocExtension^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IModelDocExtension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html) object

## VBA Syntax

See [ModelDoc2::Extension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Extension.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Names of Bodies in Multibody Part (VBA)](Get_Names_of_Bodies_in_MultiBody_Part_Example_VB.htm)
[Insert Wrap Feature (VBA)](Insert_Wrap_Feature_Example_VB.htm)
[Use Persistent Reference (VBA)](Use_Persistent_Reference_Example_VB.htm)
[Create Equation-driven Curve (C#)](Create_Equation-driven_Curve_Example_CSharp.htm)
[Create Equation-driven Curve (VB.NET)](Create_Equation-driven_Curve_Example_VBNET.htm)
[Create Equation-driven Curve (VBA)](Create_Equation-driven_Curve_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
