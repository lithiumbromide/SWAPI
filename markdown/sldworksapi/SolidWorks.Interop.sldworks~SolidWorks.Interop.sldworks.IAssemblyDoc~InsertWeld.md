---
title: "InsertWeld Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertWeld"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld.html"
---

# InsertWeld Method (IAssemblyDoc)

Obsolete. Do not use. Superseded by [IFeatureManager::InsertCosmeticWeldBead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertWeld( _
   ByVal Type As System.String, _
   ByVal Shape As System.String, _
   ByVal TopDelta As System.Double, _
   ByVal BottomDelta As System.Double, _
   ByVal Radius As System.Double, _
   ByVal Part As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Type As System.String
Dim Shape As System.String
Dim TopDelta As System.Double
Dim BottomDelta As System.Double
Dim Radius As System.Double
Dim Part As System.String

instance.InsertWeld(Type, Shape, TopDelta, BottomDelta, Radius, Part)
```

### C#

```csharp
void InsertWeld(
   System.string Type,
   System.string Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.string Part
)
```

### C++/CLI

```cpp
void InsertWeld(
   System.String^ Type,
   System.String^ Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.String^ Part
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Weld bead type
- `Shape`: Surface shape
- `TopDelta`: Distance for the top surface delta, if appropriate
- `BottomDelta`: Distance for the bottom surface delta, if appropriate
- `Radius`: Weld radius, if appropriate
- `Part`: Path and filename for the part used for the weld; this file is created and merged into your assembly

## VBA Syntax

See [AssemblyDoc::InsertWeld](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertWeld.html).

## Remarks

For the most up-to-date list of available types and shapes, see **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym**.

To programmatically select the top, stop, and contact faces for the weld bead and pass them as arrays, use [IAssemblyDoc::InsertWeld2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~InsertWeld2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
