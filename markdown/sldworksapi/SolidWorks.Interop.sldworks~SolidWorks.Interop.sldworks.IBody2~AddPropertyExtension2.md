---
title: "AddPropertyExtension2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "AddPropertyExtension2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~AddPropertyExtension2.html"
---

# AddPropertyExtension2 Method (IBody2)

Adds a property extension to this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddPropertyExtension2( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim PropertyExtension As System.Object
Dim value As System.Integer

value = instance.AddPropertyExtension2(PropertyExtension)
```

### C#

```csharp
System.int AddPropertyExtension2(
   System.object PropertyExtension
)
```

### C++/CLI

```cpp
System.int AddPropertyExtension2(
   System.Object^ PropertyExtension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropertyExtension`: Value of the property extension to add to this body (see **Remarks**)

### Return Value

Size of the array to which the property extension value is added

## VBA Syntax

See [Body2::AddPropertyExtension2](ms-its:sldworksapivb6.chm::/sldworks~Body2~AddPropertyExtension2.html).

## Remarks

To use this method:

1. Declare the variable.
2. Assign the variable a value: float, integer, or string.
3. Call this method to add the value to the body.

The 1-based array is a first-in-last-out structured list, whose size is used by [IBody2::GetPropertyExtension2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetPropertyExtension2.html) to access the property extension.

**NOTE**: SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::ResetPropertyExtension2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ResetPropertyExtension2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
