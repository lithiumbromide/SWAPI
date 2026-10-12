---
title: "AddToRecentDocumentList Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "AddToRecentDocumentList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~AddToRecentDocumentList.html"
---

# AddToRecentDocumentList Property (IDocumentSpecification)

Gets or sets whether to add the opened document to the Recent Documents list.

## Syntax

### Visual Basic (Declaration)

```vb
Property AddToRecentDocumentList As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Integer

instance.AddToRecentDocumentList = value

value = instance.AddToRecentDocumentList
```

### C#

```csharp
System.int AddToRecentDocumentList {get; set;}
```

### C++/CLI

```cpp
property System.int AddToRecentDocumentList {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Recent Document list actions as defined by [swAddToRecentDocumentList_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAddToRecentDocumentList_e.html)

## VBA Syntax

See [DocumentSpecification::AddToRecentDocumentList](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~AddToRecentDocumentList.html).

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)

## Availability

SOLIDWORKS 2022 SP03, Revision Number 30.3
