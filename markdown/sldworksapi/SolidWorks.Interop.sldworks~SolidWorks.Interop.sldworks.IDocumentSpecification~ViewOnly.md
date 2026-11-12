---
title: "ViewOnly Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "ViewOnly"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.html"
---

# ViewOnly Property (IDocumentSpecification)

Gets or sets whether to open the assembly document in Large Design Review mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.ViewOnly = value

value = instance.ViewOnly
```

### C#

```csharp
System.bool ViewOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewOnly {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to open the assembly in Large Design Review mode, false to not

## VBA Syntax

See [DocumentSpecification::ViewOnly](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~ViewOnly.html).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IConfiguration::LargeDesignReviewMark Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~LargeDesignReviewMark.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
