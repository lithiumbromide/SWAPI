---
title: "CreateMassProperty2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateMassProperty2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty2.html"
---

# CreateMassProperty2 Method (IModelDocExtension)

Creates a mass properties object.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMassProperty2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.CreateMassProperty2()
```

### C#

```csharp
System.object CreateMassProperty2()
```

### C++/CLI

```cpp
System.Object^ CreateMassProperty2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)

## VBA Syntax

See [ModelDocExtension::CreateMassProperty2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CreateMassProperty2.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## Remarks

| If this document is a... | Then this method returns... |
| --- | --- |
| Part | A mass properties object with information about one or more bodies. Before calling this method, call IModelDocExtension::SelectByID2 to pre-select the bodies. You can also specify more bodies after calling this method by setting IMassProperty2::SelectedItems . |
| Assembly | A mass properties object with information about one or more components. Before calling this method, call IModelDocExtension::SelectByID2 to pre-select the components. You can also specify more components after calling this method by setting IMassProperty2::SelectedItems . Bodies from multibody part components cannot be selected for mass properties calculations. |
| Model that does not apply (e.g., a part with surface bodies only) | Null or Nothing. |

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
