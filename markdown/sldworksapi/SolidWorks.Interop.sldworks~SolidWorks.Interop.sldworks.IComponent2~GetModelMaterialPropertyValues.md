---
title: "GetModelMaterialPropertyValues Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetModelMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues.html"
---

# GetModelMaterialPropertyValues Method (IComponent2)

Gets the material properties of this lightweight component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelMaterialPropertyValues( _
   ByVal ConfigName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As System.Object

value = instance.GetModelMaterialPropertyValues(ConfigName)
```

### C#

```csharp
System.object GetModelMaterialPropertyValues(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.Object^ GetModelMaterialPropertyValues(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration

### Return Value

An array of 9 doubles (see **Remarks**)

## VBA Syntax

See [Component2::GetModelMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetModelMaterialPropertyValues.html).

## Examples

[Get Model Material Property Values (VBA)](Get_Model_Material_Property_Values_Example_VB.htm)
[Get Model Material Property Values (VB.NET)](Get_Model_Material_Property_Values_Example_VBNET.htm)
[Get Model Material Property Values (C#)](Get_Model_Material_Property_Values_Example_CSharp.htm)

## Remarks

The contents of the returned array:

[ R, G, B, Ambient, Diffuse, Specularity, Shininess, Transparency, Emission ]

Valid values are between 0.0 and 1.0, inclusive. Multiply the R, G, and B values by 255 to obtain the red, green, and blue component values. Multiply the other values in the array by 100 to obtain percentages. If all values in the array are -1, then material property values were not assigned to this component, and the component has the same default properties as the user interface.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)
[IComponent2::IGetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelMaterialPropertyValues.html)
[IComponent2::HasMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
