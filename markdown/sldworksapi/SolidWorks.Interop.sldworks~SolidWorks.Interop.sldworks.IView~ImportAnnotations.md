---
title: "ImportAnnotations Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ImportAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ImportAnnotations.html"
---

# ImportAnnotations Method (IView)

Imports the specified annotations into this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ImportAnnotations( _
   ByVal IncludeDesignAnnotations As System.Boolean, _
   ByVal IncludeCosmeticThreads As System.Boolean, _
   ByVal IncludeDimXpertAnnotations As System.Boolean, _
   ByVal IncludeHiddenFeatureItems As System.Boolean, _
   ByVal Include3DViewAnnotations As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim IncludeDesignAnnotations As System.Boolean
Dim IncludeCosmeticThreads As System.Boolean
Dim IncludeDimXpertAnnotations As System.Boolean
Dim IncludeHiddenFeatureItems As System.Boolean
Dim Include3DViewAnnotations As System.Boolean

instance.ImportAnnotations(IncludeDesignAnnotations, IncludeCosmeticThreads, IncludeDimXpertAnnotations, IncludeHiddenFeatureItems, Include3DViewAnnotations)
```

### C#

```csharp
void ImportAnnotations(
   System.bool IncludeDesignAnnotations,
   System.bool IncludeCosmeticThreads,
   System.bool IncludeDimXpertAnnotations,
   System.bool IncludeHiddenFeatureItems,
   System.bool Include3DViewAnnotations
)
```

### C++/CLI

```cpp
void ImportAnnotations(
   System.bool IncludeDesignAnnotations,
   System.bool IncludeCosmeticThreads,
   System.bool IncludeDimXpertAnnotations,
   System.bool IncludeHiddenFeatureItems,
   System.bool Include3DViewAnnotations
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `IncludeDesignAnnotations`: True to import design annotations, false to not
- `IncludeCosmeticThreads`: True to import cosmetic threads, false to not
- `IncludeDimXpertAnnotations`: True to import DimXpert annotations, false to not
- `IncludeHiddenFeatureItems`: True to import hidden feature items, false to not
- `Include3DViewAnnotations`: True to import 3D view annotations, false to not

## VBA Syntax

See

[View::ImportAnnotations](ms-its:sldworksapivb6.chm::/sldworks~View~ImportAnnotations.html)

.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2025 FCS, Revision Number 33
