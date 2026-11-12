---
title: "ReadOnly Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "ReadOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ReadOnly.html"
---

# ReadOnly Property (IDocumentSpecification)

Gets or sets whether the model document is opened read-only or read-write.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReadOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.ReadOnly = value

value = instance.ReadOnly
```

### C#

```csharp
System.bool ReadOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ReadOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the model document is opened read-only, false if read-write

## VBA Syntax

See [DocumentSpecification::ReadOnly](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~ReadOnly.html).

## Examples

[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
