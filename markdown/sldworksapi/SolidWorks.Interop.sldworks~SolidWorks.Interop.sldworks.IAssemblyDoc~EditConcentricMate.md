---
title: "EditConcentricMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EditConcentricMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditConcentricMate.html"
---

# EditConcentricMate Method (IAssemblyDoc)

Edits a misaligned concentric mate.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditConcentricMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal ConcentricPositionType As System.Integer, _
   ByVal ConcentricToleranceCheck As System.Boolean, _
   ByVal ConcentricToleranceValue As System.Double, _
   ByRef ErrorStatus As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim AlignFromEnum As System.Integer
Dim ConcentricPositionType As System.Integer
Dim ConcentricToleranceCheck As System.Boolean
Dim ConcentricToleranceValue As System.Double
Dim ErrorStatus As System.Integer

instance.EditConcentricMate(AlignFromEnum, ConcentricPositionType, ConcentricToleranceCheck, ConcentricToleranceValue, ErrorStatus)
```

### C#

```csharp
void EditConcentricMate(
   System.int AlignFromEnum,
   System.int ConcentricPositionType,
   System.bool ConcentricToleranceCheck,
   System.double ConcentricToleranceValue,
   out System.int ErrorStatus
)
```

### C++/CLI

```cpp
void EditConcentricMate(
   System.int AlignFromEnum,
   System.int ConcentricPositionType,
   System.bool ConcentricToleranceCheck,
   System.double ConcentricToleranceValue,
   [Out] System.int ErrorStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AlignFromEnum`: Type of mate alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)
- `ConcentricPositionType`: Misaligned concentric mate position as defined in [swConcentricAlignmentType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConcentricAlignmentType_e.html)
- `ConcentricToleranceCheck`: True to override the deviation, false to have SOLIDWORKS calculate the deviation
- `ConcentricToleranceValue`: Maximum deviation; valid only when ConcentricToleranceCheck is true
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

## VBA Syntax

See [AssemblyDoc::EditConcentricMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EditConcentricMate.html).

## Examples

See the [IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.html) examples.

## Remarks

Select these entities before calling this method:

- Two entities that define the misaligned concentric mate
- Misaligned concentric mate

A parent non-misaligned (i.e., standard) concentric mate must already exist for the selected misaligned concentric mate. If a suitable parent concentric mate does not exist, then the selected misaligned concentric mate changes to a standard concentric mate. You can also change a misaligned concentric mate to a standard concentric mate using [IAssemblyDoc::EditMate4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.html).

After calling IAssemblyDoc::EditConcentricMate, call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::AddConcentricMateWithTolerance Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.html)
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
