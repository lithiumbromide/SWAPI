---
title: "IInsertProjectedSketch2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "IInsertProjectedSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IInsertProjectedSketch2.html"
---

# IInsertProjectedSketch2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::IInsertProjectedSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertProjectedSketch2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertProjectedSketch2( _
   ByVal Reverse As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Reverse As System.Integer
Dim value As Feature

value = instance.IInsertProjectedSketch2(Reverse)
```

### C#

```csharp
Feature IInsertProjectedSketch2(
   System.int Reverse
)
```

### C++/CLI

```cpp
Feature^ IInsertProjectedSketch2(
   System.int Reverse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reverse`:

## VBA Syntax

See [ModelDoc::IInsertProjectedSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~IInsertProjectedSketch2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
