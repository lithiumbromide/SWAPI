---
title: "GetPropertyExtension Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IModelDoc2)

Gets the specified property extension on this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

- `ID`: (Size of the array returned by [IModelDoc2::AddPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddPropertyExtension.html)) - (Position of the property extension in the array)

### Return Value

Value of the property extension

## VBA Syntax

See [ModelDoc2::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetPropertyExtension.html).

## Remarks

IModelDoc2::AddPropertyExtension adds property extensions to a last-in-first-out, 1-based array and returns the size of that array.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetPropertyExtension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
