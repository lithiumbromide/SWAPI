---
title: "GetPropertyExtension Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IPartDoc)

Gets the specified property extension on this part document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim ID As System.Integer
Dim value As System.Object

value = instance.GetPropertyExtension(ID)
```

### C#

```csharp
System.object GetPropertyExtension(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ GetPropertyExtension(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: (Size of the array returned by [IPartDoc::AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~AddPropertyExtension.html)) - (Position of the property extension in the array) (see **Remarks**)

### Return Value

Value of the property extension

## VBA Syntax

See [PartDoc::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~GetPropertyExtension.html).

## Examples

[Add and Get Property Extensions (C#)](Add_and_Get_Property_Extension_Example_CSharp.htm)
[Add and Get Property Extensions (VB.NET)](Add_and_Get_Property_Extension_Example_VBNET.htm)
[Add and Get Property Extensions (VBA)](Add_and_Get_Property_Extension_Example_VB.htm)

## Remarks

IPartDoc::AddPropertyExtension adds property extensions to a last-in-first-out, 1-based array and returns the size of that array. See the examples in **Example**.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ResetPropertyExtension.html)
