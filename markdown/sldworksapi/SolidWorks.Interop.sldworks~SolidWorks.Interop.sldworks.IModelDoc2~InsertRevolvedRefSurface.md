---
title: "InsertRevolvedRefSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRevolvedRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRevolvedRefSurface.html"
---

# InsertRevolvedRefSurface Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertRevolvedRefSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertRevolvedRefSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRevolvedRefSurface( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer

instance.InsertRevolvedRefSurface(Angle, ReverseDir, Angle2, RevType)
```

### C#

```csharp
void InsertRevolvedRefSurface(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

### C++/CLI

```cpp
void InsertRevolvedRefSurface(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:

## VBA Syntax

See [ModelDoc2::InsertRevolvedRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRevolvedRefSurface.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
