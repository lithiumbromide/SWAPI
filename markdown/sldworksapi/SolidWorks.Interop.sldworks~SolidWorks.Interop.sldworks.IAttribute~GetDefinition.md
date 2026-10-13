---
title: "GetDefinition Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetDefinition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetDefinition.html"
---

# GetDefinition Method (IAttribute)

Gets the definition of this attribute.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefinition() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As System.Object

value = instance.GetDefinition()
```

### C#

```csharp
System.object GetDefinition()
```

### C++/CLI

```cpp
System.Object^ GetDefinition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the attribute definition

## VBA Syntax

See [Attribute::GetDefinition](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetDefinition.html).

## Remarks

SOLIDWORKS generates all attribute instances from an [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object. The object is the mold that gives the attribute its parameters and default values.

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::IGetDefinition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetDefinition.html)
