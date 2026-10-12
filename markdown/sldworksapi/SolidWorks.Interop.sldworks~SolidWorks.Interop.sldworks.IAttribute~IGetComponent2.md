---
title: "IGetComponent2 Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "IGetComponent2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetComponent2.html"
---

# IGetComponent2 Method (IAttribute)

Returns the component to which this attribute is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetComponent2() As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As Component2

value = instance.IGetComponent2()
```

### C#

```csharp
Component2 IGetComponent2()
```

### C++/CLI

```cpp
Component2^ IGetComponent2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [Attribute::IGetComponent2](ms-its:sldworksapivb6.chm::/sldworks~Attribute~IGetComponent2.html).

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::GetComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetComponent.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
