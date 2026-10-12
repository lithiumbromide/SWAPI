---
title: "GetPropertyExtension Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetPropertyExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPropertyExtension.html"
---

# GetPropertyExtension Method (IComponent2)

Gets the property extension on this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPropertyExtension( _
   ByVal ID As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
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

- `ID`: 0

### Return Value

Value of the property extension

## VBA Syntax

See [Component2::GetPropertyExtension](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetPropertyExtension.html).

## Remarks

SOLIDWORKS recommends that you use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html), [IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html), and [IParameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IParameter.html) interfaces instead of this method. These interfaces provide more flexibility.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::AddPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~AddPropertyExtension.html)
[IComponent2::ResetPropertyExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ResetPropertyExtension.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
