---
title: "FeatureRevolveCut2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "FeatureRevolveCut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureRevolveCut2.html"
---

# FeatureRevolveCut2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::FetureRevolveCut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FeatureRevolveCut2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureRevolveCut2( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Options As System.Integer
Dim value As System.Integer

value = instance.FeatureRevolveCut2(Angle, ReverseDir, Angle2, RevType, Options)
```

### C#

```csharp
System.int FeatureRevolveCut2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options
)
```

### C++/CLI

```cpp
System.int FeatureRevolveCut2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:
- `Options`:

## VBA Syntax

See [ModelDoc::FeatureRevolveCut2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~FeatureRevolveCut2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
