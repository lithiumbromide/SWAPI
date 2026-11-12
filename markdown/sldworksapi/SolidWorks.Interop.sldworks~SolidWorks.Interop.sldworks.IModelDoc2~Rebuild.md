---
title: "Rebuild Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Rebuild"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Rebuild.html"
---

# Rebuild Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::Rebuild](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~Rebuild.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub Rebuild( _
   ByVal Options As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Options As System.Integer

instance.Rebuild(Options)
```

### C#

```csharp
void Rebuild(
   System.int Options
)
```

### C++/CLI

```cpp
void Rebuild(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Type of rebuild as defined in [swRebuildOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOptions_e.html)

## VBA Syntax

See [ModelDoc2::Rebuild](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Rebuild.html).

## Remarks

Use [IModelDoc2::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html) to check the type of document.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
