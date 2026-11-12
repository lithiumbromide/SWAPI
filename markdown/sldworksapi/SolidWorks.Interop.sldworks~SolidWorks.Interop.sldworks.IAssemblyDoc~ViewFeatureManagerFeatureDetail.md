---
title: "ViewFeatureManagerFeatureDetail Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ViewFeatureManagerFeatureDetail"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerFeatureDetail.html"
---

# ViewFeatureManagerFeatureDetail Method (IAssemblyDoc)

Obsolete. Superseded by [IFeatureManager::ShowFeatureDetails](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~ShowFeatureDetails.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ViewFeatureManagerFeatureDetail( _
   ByVal Detail As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Detail As System.Boolean

instance.ViewFeatureManagerFeatureDetail(Detail)
```

### C#

```csharp
void ViewFeatureManagerFeatureDetail(
   System.bool Detail
)
```

### C++/CLI

```cpp
void ViewFeatureManagerFeatureDetail(
   System.bool Detail
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Detail`: True to show feature detail, false to hide it

## VBA Syntax

See [AssemblyDoc::ViewFeatureManagerFeatureDetail](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ViewFeatureManagerFeatureDetail.html).

## Remarks

This method affects the FeatureManager design tree view of the current configuration of the assembly. It does not affect other configurations.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ViewFeatureManagerByDependencies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerByDependencies.html)
[IAssemblyDoc::ViewFeatureManagerByFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ViewFeatureManagerByFeatures.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
