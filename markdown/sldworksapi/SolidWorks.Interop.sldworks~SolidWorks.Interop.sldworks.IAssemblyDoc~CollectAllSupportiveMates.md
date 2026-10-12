---
title: "CollectAllSupportiveMates Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CollectAllSupportiveMates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.html"
---

# CollectAllSupportiveMates Method (IAssemblyDoc)

Gets all mates supportive of a mate controller in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function CollectAllSupportiveMates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.CollectAllSupportiveMates()
```

### C#

```csharp
System.object CollectAllSupportiveMates()
```

### C++/CLI

```cpp
System.Object^ CollectAllSupportiveMates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [AssemblyDoc::CollectAllSupportiveMates](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CollectAllSupportiveMates.html).

## Examples

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html) examples.

## Remarks

This method is valid only if [IAssemblyDoc::IsSupportedMatesAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable.html) is true.

To create a mate controller, see the Remarks section of [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.html).

For more information about the Mate Controller feature, see the **SOLIDWORKS Design user-interface help > Assemblies > Mates > Mate Controller** topic.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
