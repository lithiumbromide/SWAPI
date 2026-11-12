---
title: "DissolveLibraryFeature Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DissolveLibraryFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DissolveLibraryFeature.html"
---

# DissolveLibraryFeature Method (IModelDoc2)

Dissolves the selected library features.

## Syntax

### Visual Basic (Declaration)

```vb
Function DissolveLibraryFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.DissolveLibraryFeature()
```

### C#

```csharp
System.bool DissolveLibraryFeature()
```

### C++/CLI

```cpp
System.bool DissolveLibraryFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected library features are dissolved, false if not

## VBA Syntax

See [ModelDoc2::DissolveLibraryFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DissolveLibraryFeature.html).

## Remarks

This method dissolves all library features that are selected when it executes. Only the selected library features are dissolved, anything else selected is ignored.

To create a library feature, use [IModelDoc2::InsertLibraryFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertLibraryFeature.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ILibraryFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
