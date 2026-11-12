---
title: "BreakLink Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "BreakLink"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~BreakLink.html"
---

# BreakLink Method (IFeature)

Breaks the link to third-party native CAD parts and assemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Function BreakLink( _
   ByVal AllComponents As System.Boolean, _
   ByVal Silent As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim AllComponents As System.Boolean
Dim Silent As System.Boolean
Dim value As System.Integer

value = instance.BreakLink(AllComponents, Silent)
```

### C#

```csharp
System.int BreakLink(
   System.bool AllComponents,
   System.bool Silent
)
```

### C++/CLI

```cpp
System.int BreakLink(
   System.bool AllComponents,
   System.bool Silent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AllComponents`: True to break the link for all subcomponents within a top-level subassembly, false to not (see **Remarks**)
- `Silent`: True to suppress dialog windows, false to not

### Return Value

Error codes as defined in [sw3DInterconnectImportErrors_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DInterconnectImportErrors_e.html)

## VBA Syntax

See [Feature::BreakLink](ms-its:sldworksapivb6.chm::/sldworks~Feature~BreakLink.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

By default, breaking a link of an assembly component breaks the links of all instances of that component.

After you break a link, all references to the original CAD file are lost. You can no longer change the entities to transfer from the original file or update the SOLIDWORKS model with changes from the third-party authoring application.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
