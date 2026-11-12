---
title: "DetailingMode Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "DetailingMode"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~DetailingMode.html"
---

# DetailingMode Property (IDocumentSpecification)

Gets or sets whether this drawing document is in detailing mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property DetailingMode As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.DetailingMode = value

value = instance.DetailingMode
```

### C#

```csharp
System.bool DetailingMode {get; set;}
```

### C++/CLI

```cpp
property System.bool DetailingMode {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if in detailing mode, false if not

## VBA Syntax

See [DocumentSpecification::DetailingMode](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~DetailingMode.html).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
