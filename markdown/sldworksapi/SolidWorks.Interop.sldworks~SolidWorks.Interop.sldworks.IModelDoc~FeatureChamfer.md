---
title: "FeatureChamfer Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureChamfer.html"
---

# FeatureChamfer Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FeatureChamfer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureChamfer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureChamfer( _
   ByVal Width As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Flip As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Width As System.Double
Dim Angle As System.Double
Dim Flip As System.Boolean

instance.FeatureChamfer(Width, Angle, Flip)
```

### C#

```csharp
void FeatureChamfer(
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

### C++/CLI

```cpp
void FeatureChamfer(
   System.double Width,
   System.double Angle,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Width`:
- `Angle`:
- `Flip`:

## VBA Syntax

See [ModelDoc::FeatureChamfer](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureChamfer.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
