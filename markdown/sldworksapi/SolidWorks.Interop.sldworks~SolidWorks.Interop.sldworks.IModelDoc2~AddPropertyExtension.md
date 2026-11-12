---
title: "AddPropertyExtension Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AddPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddPropertyExtension.html"
---

# AddPropertyExtension Method (IModelDoc2)

Adds a property extension to this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

- `PropertyExtension`: Value of the property extension to add to the model (see **Remarks**)

### Return Value

Size of the array to which the property extension value is added

## VBA Syntax

See [ModelDoc2::AddPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AddPropertyExtension.html).

## Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the model.

The 1-based array is a first-in-last-out structured list, whose size is used by [IModelDoc2::GetPropertyExtension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPropertyExtension.html) to access the property extension..

**NOTE**: SOLIDWORKS recommends that you use [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) instead of this method. These interfaces provide more flexibility.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetPropertyExtension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
