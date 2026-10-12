---
title: "InsertWeld2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertWeld2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertWeld2.html"
---

# InsertWeld2 Method (IAssemblyDoc)

Obsolete. Do not use. Superseded by [IFeatureManager::InsertCosmeticWeldBead](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertWeld2( _
   ByVal Type As System.String, _
   ByVal Shape As System.String, _
   ByVal TopDelta As System.Double, _
   ByVal BottomDelta As System.Double, _
   ByVal Radius As System.Double, _
   ByVal Part As System.String, _
   ByVal TopFaces As System.Object, _
   ByVal StopFace As System.Object, _
   ByVal ContactFaces As System.Object _
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
Dim TopFaces As System.Object
Dim StopFace As System.Object
Dim ContactFaces As System.Object

instance.InsertWeld2(Type, Shape, TopDelta, BottomDelta, Radius, Part, TopFaces, StopFace, ContactFaces)
```

### C#

```csharp
void InsertWeld2(
   System.string Type,
   System.string Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.string Part,
   System.object TopFaces,
   System.object StopFace,
   System.object ContactFaces
)
```

### C++/CLI

```cpp
void InsertWeld2(
   System.String^ Type,
   System.String^ Shape,
   System.double TopDelta,
   System.double BottomDelta,
   System.double Radius,
   System.String^ Part,
   System.Object^ TopFaces,
   System.Object^ StopFace,
   System.Object^ ContactFaces
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
- `TopFaces`: Array of faces from which to measure the top surface delta
- `StopFace`: Array of faces that define the beginning and the end of the weld bead
- `ContactFaces`: Array of faces that are joined by the weld bead

## VBA Syntax

See [AssemblyDoc::InsertWeld2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertWeld2.html).

## Remarks

For the most up-to-date list of available types and shapes, see **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym**.

To create a weld bead by preselecting the top, stop, and contact faces, use [IAssemblyDoc::InsertWeld](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~InsertWeld.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IWeldBead Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead.html)
[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
