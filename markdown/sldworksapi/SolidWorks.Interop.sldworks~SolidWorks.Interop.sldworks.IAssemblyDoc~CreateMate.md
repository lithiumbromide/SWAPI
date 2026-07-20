---
title: "CreateMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CreateMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html"
---

# CreateMate Method (IAssemblyDoc)

Creates a mate with the specified feature data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateMate( _
   ByVal MateData As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim MateData As System.Object
Dim value As System.Object

value = instance.CreateMate(MateData)
```

### C#

```csharp
System.object CreateMate(
   System.object MateData
)
```

### C++/CLI

```cpp
System.Object^ CreateMate(
   System.Object^ MateData
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `MateData`: Mate-specific object (see

Remarks

)

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See

[AssemblyDoc::CreateMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CreateMate.html)

.

## Examples

See the Example sections of the interfaces listed in Remarks.

## Remarks

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html)is the base interface for the following mate-specific interfaces (an asterisk indicates that pre-selection of mate entities during mate creation is supported):

- [IAngleMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData.html)
- [ICamFollowerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData.html)

  *
- [ICoincidentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.html)

  *
- [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html)

  *
- [IDistanceMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData.html)
- [IGearMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData.html)

  *
- [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.html)

  *
- [ILinearCouplerMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.html)
- [ILockMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.html)

  *
- [IParallelMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.html)

  *
- [IPerpendicularMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData.html)

  *
- [IProfileCenterMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html)
- [IRackPinionMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData.html)

  *
- [IScrewMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData.html)

  *
- [ISlotMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData.html)

  *
- [ISymmetricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html)
- [ITangentMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData.html)

  *
- [IUniversalJointMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData.html)

  *
- [IWidthMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html)

To create a standard, advanced, or mechanical mate:

1. Use

  [IAssemblyDoc::CreateMateData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMateData.html)

  to access a MateFeatureData object.
2. Set the general properties of the MateFeatureData object.
3. Cast the MateFeatureData object to one of the mate-specific objects.
4. Follow specific instructions in the Remarks of the mate-specific interface, set specific properties of the mate-specific object, and/or pre-select entities to mate for asterisked interfaces above.
5. Call this method, passing in the mate-specific object.

To create:

- Misaligned concentric mates, use

  [IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.html)

  .
- Cylindrical distance mates, use

  [IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html)

  .

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

[IAssemblyDoc::AutoMateRepair Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
