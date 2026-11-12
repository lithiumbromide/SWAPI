---
title: "IsSupportedMatesAvailable Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "IsSupportedMatesAvailable"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable.html"
---

# IsSupportedMatesAvailable Property (IAssemblyDoc)

Gets whether this assembly contains mates that are supportive of a mate controller.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSupportedMatesAvailable As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.IsSupportedMatesAvailable
```

### C#

```csharp
System.bool IsSupportedMatesAvailable {get;}
```

### C++/CLI

```cpp
property System.bool IsSupportedMatesAvailable {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if mates supportive of a mate controller are available, false if not

## VBA Syntax

See [AssemblyDoc::IsSupportedMatesAvailable](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~IsSupportedMatesAvailable.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## Remarks

Supportive mate types are as defined by [swMateType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html).:

- swMateANGLE
- swMateDISTANCE
- swMatePATH
- swMateSLOT
- swMateWIDTH

The Mate Controller feature does not support path, width, or slot mates created with either a free or a center in slot constraint.

If this property is true, then use [IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.html) to collect the supportive mates in this assembly.

To create a mate controller, see the Remarks section of [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html).

For more information about the Mate Controller feature, see the **SOLIDWORKS Design user-interface help > Assemblies > Mates > Mate Controller** topic.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
