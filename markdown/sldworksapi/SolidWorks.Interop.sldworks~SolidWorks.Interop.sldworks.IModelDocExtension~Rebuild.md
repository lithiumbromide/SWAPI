---
title: "Rebuild Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Rebuild"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Rebuild.html"
---

# Rebuild Method (IModelDocExtension)

Rebuilds the model in assembly and drawing documents and returns the status of the rebuild.

## Syntax

### Visual Basic (Declaration)

```vb
Function Rebuild( _
   ByVal Options As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Boolean

value = instance.Rebuild(Options)
```

### C#

```csharp
System.bool Rebuild(
   System.int Options
)
```

### C++/CLI

```cpp
System.bool Rebuild(
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Type of rebuild as defined in [swRebuildOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOptions_e.html)

### Return Value

True if the rebuild is successful, false if not

## VBA Syntax

See [ModelDocExtension::Rebuild](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Rebuild.html).

## Examples

[Rebuild an Assembly (VBA)](Rebuild_an_Assembly_Example_VB.htm)
[Rebuild an Assembly (VB.NET)](Rebuild_an_Assembly_Example_VBNET.htm)
[Rebuild an Assembly (C#)](Rebuild_an_Assembly_Example_CSharp.htm)

## Remarks

Use [IModelDoc2::GetType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetType.html) to check the type of document.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::EditRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html)
[IModelDoc2::ForceRebuild3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::EditRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~EditRebuildAll.html)
[IModelDocExtension::ForceRebuildAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ForceRebuildAll.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
