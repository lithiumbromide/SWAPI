---
title: "GetPropertyExtension2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetPropertyExtension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2.html"
---

# GetPropertyExtension2 Method (IBody2)

Gets the specified property extension on this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension2( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim ID As System.Integer
Dim value As System.Object

value = instance.GetPropertyExtension2(ID)
```

### C#

```csharp
System.object GetPropertyExtension2(
   System.int ID
)
```

### C++/CLI

```cpp
System.Object^ GetPropertyExtension2(
   System.int ID
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: (Size of the array returned by [IBody2::AddPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2.html)) - (Position of the property extension in the array)

### Return Value

Value of the property extension

## VBA Syntax

See [Body2::GetPropertyExtension2](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetPropertyExtension2.html).

## Remarks

IBody2::AddPropertyExtension2 adds property extensions to a last-in-first-out, 1-based array and returns the size of that array.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These three interfaces provide more flexibility.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ResetPropertyExtension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.html)
