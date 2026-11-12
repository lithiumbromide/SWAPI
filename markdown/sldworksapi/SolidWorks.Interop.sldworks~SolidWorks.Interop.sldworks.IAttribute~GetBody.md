---
title: "GetBody Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetBody.html"
---

# GetBody Method (IAttribute)

Gets the body to which this attribute is attached, if any.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As Body2

value = instance.GetBody()
```

### C#

```csharp
Body2 GetBody()
```

### C++/CLI

```cpp
Body2^ GetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Attribute::GetBody](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetBody.html).

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
