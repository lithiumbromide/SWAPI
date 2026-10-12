---
title: "InsertLibraryFeature Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertLibraryFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertLibraryFeature.html"
---

# InsertLibraryFeature Method (IModelDoc2)

Obsolete. See **Remarks**.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertLibraryFeature( _
   ByVal LibFeatPartNameIn As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim LibFeatPartNameIn As System.String

instance.InsertLibraryFeature(LibFeatPartNameIn)
```

### C#

```csharp
void InsertLibraryFeature(
   System.string LibFeatPartNameIn
)
```

### C++/CLI

```cpp
void InsertLibraryFeature(
   System.String^ LibFeatPartNameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LibFeatPartNameIn`: Name of the library feature

## VBA Syntax

See [ModelDoc2::InsertLibraryFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertLibraryFeature.html).

## Remarks

See [Library Features and LibraryFeatureData Objects](sldworksapiprogguide.chm::/OVERVIEW/Library_Features_and_LibraryFeatureData_Objects.htm).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
