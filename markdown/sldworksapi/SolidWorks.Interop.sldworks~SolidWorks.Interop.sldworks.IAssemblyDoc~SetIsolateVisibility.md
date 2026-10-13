---
title: "SetIsolateVisibility Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetIsolateVisibility"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetIsolateVisibility.html"
---

# SetIsolateVisibility Method (IAssemblyDoc)

Sets the display characteristics of all of the components not selected to [isolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~Isolate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIsolateVisibility( _
   ByVal Option As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Option As System.Integer

instance.SetIsolateVisibility(Option)
```

### C#

```csharp
void SetIsolateVisibility(
   System.int Option
)
```

### C++/CLI

```cpp
void SetIsolateVisibility(
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Option`: Display characteristics of all of the components not selected to isolate as defined in [swIsolateVisibility_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swIsolateVisibility_e.html)

## VBA Syntax

See [AssemblyDoc::SetIsolateVisibility](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetIsolateVisibility.html).

## Examples

[Isolate Component (C#)](Isolate_Component_Example_CSharp.htm)
[Isolate Component (VB.NET)](Isolate_Component_Example_VBNET.htm)
[Isolate Component (VBA)](Isolate_Component_Example_VB.htm)

## Remarks

Before you [exit isolate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ExitIsolate.html), you can [save the display characteristics to a new display state](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SaveIsolate.html), which you can access from the ConfigurationManager. If you do not save before exiting isolate, then the display returns to its original state.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
