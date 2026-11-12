---
title: "AddPropertyExtension Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IPartDoc)

Adds a property extension to this part.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`: Value of the property extension to add to this part (see **Remarks**)

### Return Value

Size of the array to which the property extension value is added

## VBA Syntax

See [PartDoc::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~AddPropertyExtension.html).

## Examples

[Add and Get Property Extensions (C#)](Add_and_Get_Property_Extension_Example_CSharp.htm)
[Add and Get Property Extensions (VB.NET)](Add_and_Get_Property_Extension_Example_VBNET.htm)
[Add and Get Property Extensions (VBA)](Add_and_Get_Property_Extension_Example_VB.htm)

## Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the part.

The 1-based array is a first-in-last-out structured list, whose size is used by [IPartDoc::GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPropertyExtension.html) to access the property extension. See the examples in **Example**.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ResetPropertyExtension.html)
