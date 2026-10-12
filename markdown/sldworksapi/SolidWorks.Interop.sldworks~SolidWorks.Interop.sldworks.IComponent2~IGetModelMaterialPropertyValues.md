---
title: "IGetModelMaterialPropertyValues Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetModelMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetModelMaterialPropertyValues.html"
---

# IGetModelMaterialPropertyValues Method (IComponent2)

Gets the material properties of this lightweight component in the specified configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetModelMaterialPropertyValues( _
   ByVal ConfigName As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ConfigName As System.String
Dim value As System.Double

value = instance.IGetModelMaterialPropertyValues(ConfigName)
```

### C#

```csharp
System.double IGetModelMaterialPropertyValues(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.double IGetModelMaterialPropertyValues(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration

### Return Value

- in-process, unmanaged C++: Pointer to an array of 9 doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The contents of the returned array:

[ R, G, B, Ambient, Diffuse, Specularity, Shininess, Transparency, Emission ]

Valid values are between 0.0 and 1.0, inclusive. Multiply the R, G, and B values by 255 to obtain the red, green, and blue component values. Multiply the other values in the array by 100 to obtain percentages. If all values in the array are -1, then material property values were not assigned to this component, and the component has the same default properties as the user interface.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetModelMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelMaterialPropertyValues.html)
[IComponent2::GetMaterialPropertyValues2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
