---
title: "IGetDefinition Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "IGetDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.html"
---

# IGetDefinition Method (IAttribute)

Gets the definition of this attribute.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetDefinition() As AttributeDef
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As AttributeDef

value = instance.IGetDefinition()
```

### C#

```csharp
AttributeDef IGetDefinition()
```

### C++/CLI

```cpp
AttributeDef^ IGetDefinition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAttributeDef](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef.html)

## VBA Syntax

See [Attribute::IGetDefinition](ms-its:sldworksapivb6.chm::/sldworks~Attribute~IGetDefinition.html).

## Remarks

SOLIDWORKS generates all attribute instances from an [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object. The object is the mold that gives the attribute its parameters and default values.

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
