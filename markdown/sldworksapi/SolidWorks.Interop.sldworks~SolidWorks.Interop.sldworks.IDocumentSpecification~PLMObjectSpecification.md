---
title: "PLMObjectSpecification Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "PLMObjectSpecification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~PLMObjectSpecification.html"
---

# PLMObjectSpecification Property (IDocumentSpecification)

Gets the specification of this [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PLMObjectSpecification As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Object

value = instance.PLMObjectSpecification
```

### C#

```csharp
System.object PLMObjectSpecification {get;}
```

### C++/CLI

```cpp
property System.Object^ PLMObjectSpecification {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.html)

## VBA Syntax

See [DocumentSpecification::PLMObjectSpecification](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~PLMObjectSpecification.html).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
