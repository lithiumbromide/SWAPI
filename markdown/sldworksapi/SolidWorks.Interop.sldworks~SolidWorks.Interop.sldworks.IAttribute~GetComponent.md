---
title: "GetComponent Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetComponent.html"
---

# GetComponent Method (IAttribute)

Returns the component to which this attribute is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponent() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As System.Object

value = instance.GetComponent()
```

### C#

```csharp
System.object GetComponent()
```

### C++/CLI

```cpp
System.Object^ GetComponent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the component

## VBA Syntax

See [Attribute::GetComponent](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetComponent.html).

## Examples

[Cut Body in Half using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::IGetComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetComponent2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
